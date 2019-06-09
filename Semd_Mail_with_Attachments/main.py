# coding: utf-8
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import mydata
import time

class Sender(object):
    # 初始化： 服务器，用户名， 密码， 目标列表， 标题
    def __init__(self, 
                 server=mydata.server, 
                 user=mydata.user, 
                 passwd=mydata.passwd, 
                 targets="losacii@163.com, losacii@126.com",
                 title="Default Title!"):
        self.server = server    # smtp server
        self.user = user        # name@xxx.com
        self.passwd = passwd    # passwd
        self.targets = targets  # sendto
        self.title = title      # title

        self.msg = MIMEMultipart()

        self.msg['From'] = self.user
        self.msg['To'] = self.targets
        self.msg['Subject'] = title

    # 添加文本
    def addText(self, str="UNSPECIFIED - defalt", type='plain', encoding='utf-8'):
        mimeText = MIMEText(str, type, encoding)
        self.msg.attach(mimeText)

    # 添加文件附件
    def addFile(self, filePath):
        attachment = open(filePath, "rb")
        filename = os.path.basename(filePath)

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        self.msg.attach(part)

    # ---> 添加文件夹内的所有文件
    def addDir(self, DIR):
        os.chdir(DIR)
        files = os.listdir(".")

        for file in files:
            self.addFile(file)

    # ---> 登录，发送
    def loginSend(self, PORT=25):
        smtp = smtplib.SMTP(self.server, port=PORT) 
        smtp.starttls()
        smtp.login(self.user, self.passwd)
        smtp.sendmail(self.user, self.targets, self.msg.as_string())
        smtp.quit()

def main():
    sender = Sender()
    sender.addText("Sender have added some text here!")
    sender.addFile(r"C:\Program Files (x86)\Windows Sidebar\Gadgets\SlideShow.Gadget\images\Tulip.jpg")
    sender.addDir(r"D:\doc\SCAN\testDir")
    sender.loginSend()

def sendWork():
    ''' 根据文件目录，把目录中所有文件-作为附件发送给 sptqzwzx 
    '''

    # 定义发送对象， 文本内容， 附件所在目录 
    sendTo  = "losacii@163.com"
    txt     = r"testmail" 
    DIR = input("Please Enter files' Dir:\n==> ")

    # 以 目录名称 为标题
    print("Start!\n")
    mailTitle = os.path.basename(DIR); 

    # 只为获取目录中的文件列表，以输出附件列表信息
    os.chdir(DIR)
    files = os.listdir(".");  

    # 创建 Sender 对象， 添加文本、目录附件， 发送
    sender = Sender(targets=sendTo, title=mailTitle)
    sender.addText(txt)
    sender.addDir(DIR)
    sender.loginSend()

    # 输出任务完成信息
    print("FROM:{}, TO:{}\n".format(sender.user, sendTo))
    print("Mail Title:", mailTitle)
    print("file attachments:", files)

if __name__ == "__main__":
    sendWork()
    time.sleep(5.5)
