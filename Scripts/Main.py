import requests,re,time,math,random,os
from bs4 import BeautifulSoup
def Get_PostData(LoginUrl):
    '''
       获取登录参数
    '''
    Req_Class = requests.get(LoginUrl)#获取Get对象,准备那曲第一次Cookie
    Req_Cookies = Req_Class.cookies["JSESSIONID"]#获取请求Cookie
    Html_Text = Req_Class.text#获取源码
    Soup_Class = BeautifulSoup(Html_Text,"lxml")#转为Soup对象
    Tag_NameT = ('input[name="lt"]','input[name="execution"]','input[name="_eventId"]','input[name="rmShown"]')#标签元组
    Data_ValueL = []#值列表
    for Value in Tag_NameT:
        Data_V = Soup_Class.select(Value)[0]#获取TAG对象
        Regex_Class = re.compile(r'(?<=value=\").+(?=\"\/\>)')#编译正则表达式
        Data_ValueL.append(Regex_Class.findall(str(Data_V))[0])#获取参数加入列表
    return Data_ValueL,Req_Cookies

def Start_Login():
    '''
    开始登录
    
    '''
    ValueData,Req_Cookie = Get_PostData(LoginUrl)
    Post_data = {
        "username":#####,#用户名
        "password":#####,#密码
        "lt":ValueData[0],
        "execution":ValueData[1],
        "_eventId":ValueData[2],
        "rmShown":int(ValueData[3])
        }#构造发包数据
    Post_Headers = {"Host":"ids3.jsou.cn","cookie":"JSESSIONID="+Req_Cookie}#构造headers
    Post_Rep = requests.post(LoginUrl,data=Post_data,headers=Post_Headers,allow_redirects=False)#发包并且禁止重定向
    Redirect_Url = Post_Rep.headers["Location"]#获取重定向url
    Redirect_Req = requests.get(Redirect_Url,allow_redirects=False)#进行重定向url访问拿到登录成功的cookie
    Login_Cookie = Redirect_Req.headers["Set-Cookie"].split(';')[0]#分割取首
    return Login_Cookie

def Get_CourseId(CourseUrl,LoginHeaders):#获取课程总ID
    Raw_Json_Data = requests.post(CourseUrl,headers=LoginHeaders).json()
    Course_D = {}
    Course_IDL = []
    for Each_Course_Info in Raw_Json_Data['body']:
        Course_Id = Each_Course_Info["courseVersionId"]
        Course_Name = Each_Course_Info["courseName"]
        Course_D[Course_Id] = Course_Name
        Course_IDL.append(Course_Id)
    return Course_D,Course_IDL
    
def Get_Course_ContentUrl(): #获取各个课程API URL
    Course_ID,CourseID_NameD = Get_CourseId(CourseUrl,LoginHeaders)
    Content_Urls = []
    for ID in Course_ID:
        Course_ContentUrl = "http://xuexi.jsou.cn/jxpt-web/student/course/getAllActivity/"+ID
        Content_Urls.append(Course_ContentUrl)
    return Content_Urls

def M_Heart():#获取各个课程下属全部视频信息并且构造数据包写入txt
    Post_Data0 = {
        "playStatus":"true",
        "isResourcePage":"true",
        "courseVersionId":"0",
        "activityId":"0",
        "type":2,
        "isStuLearningRecord":2,
        "token":SetToken(),#生成token
        "timePoint":random.random()*100
    }
    Content_Urls = Get_Course_ContentUrl()
    for Url in Content_Urls:#进行第一层循环
        Course_DeatilContent = requests.get(Url,headers=LoginHeaders).json()['body']
        Course_Json_Len = len(Course_DeatilContent)
        for Index in range(0,Course_Json_Len):#进行第二层循环
            Avtive_List = Course_DeatilContent[Index]["activitys"]
            for Active_Info in Avtive_List:#进行第三层循环
                Type_Ac = Active_Info["type"]
                if(Type_Ac == "2"):#过滤非视频链接
                    ACtiveID_CourseID = {}
                    Deal_Url = Url.replace("http://xuexi.jsou.cn/jxpt-web/student/course/getAllActivity/","")#处理课程URL，提取CRL
                    Post_Data0["courseVersionId"] = Deal_Url
                    Post_Data0["activityId"] = Active_Info["activityId"]
                    with open("PostData.txt","a+") as f:
                        f.write(str(Post_Data0)+"\n")#写入数据包
    print("写入完成,请重新运行脚本")
def SetToken():#根据网站逆向得出Token算法
    len_ = 8.or(32)
    Salt = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
    MaxPos = len(Salt)
    Pwd = ""
    i = 0
    while(i<len_):
        i+=1
        Pwd+=Salt[math.floor(random.random()*MaxPos)]
    return Pwd
    
def Start_Run():
    print("等待刷课中....")
    Count = 0
    with open("PostData.txt","r+") as f:
        P_Data = f.readlines()
    for P_E in P_Data:
        Count+=1
        R_I = random.randint(2,5)
        print("本次随机间隔为{}秒...等待中...\n".format(R_I))
        time.sleep(R_I)
        Repo = requests.post(HeartBeatUrl,headers=LoginHeaders,data=eval(P_E)).json()
        if(Repo["code"]=="SUCCESS"):
            print("刷课运行正常，正在进行第{}个视频\n".format(Count))
        else:
            print("respone返回错误，刷课终止.")
            exit(0)
    Count=0
if __name__ == "__main__":

    Num = 0
    LoginUrl = "https://ids3.jsou.cn/login?service=http://xuexi.jsou.cn/jxpt-web/auth/idsLogin"
    CourseUrl = "http://xuexi.jsou.cn/jxpt-web/student/courseuser/getAllCurrentCourseByStudent"
    HeartBeatUrl = "http://xuexi.jsou.cn/jxpt-web/common/learningBehavior/heartbeat"
    LoginHeaders = {"Host":"xuexi.jsou.cn","Cookie":Start_Login(),"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    if(os.path.exists("PostData.txt")==False):
        M_Heart()
    else:
        while True:
            Start_Run()
            Num+=1
            print("\n第{}轮结束,第{}轮即将开始...\n".format(Num,Num+1))
    

