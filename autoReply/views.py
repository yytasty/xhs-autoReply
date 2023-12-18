from django.shortcuts import render, HttpResponse
from DrissionPage import ChromiumPage
from DrissionPage.common import ActionChains
from FlowViewer import listener
import time
import base64

# Create your views here.
def index(request):
    
    # 指定不同人，不同端口
    page = ChromiumPage(addr_driver_opts='127.0.0.1:9333')

    ## 跳转首页
    page.get('https://www.xiaohongshu.com/')

    ## 登录（保存图片，到时候回显给前端）
    loginImgEle = page.ele('.qrcode-img')
    src = loginImgEle.get_src()
    file_path = './test.png'
    with open(file_path, 'wb') as file:
        # 将二进制数据写入文件
        file.write(src)

    return HttpResponse('欢迎来到自动回复中心')
    

# Create your views here.
def listener(request):
    listener = Listener(9333)  # 创建监听器，监听9222端口的浏览器
    listener.listen()  # 开始监听，不设置目标，无限制监听

    for data in listener.steps():  # 遍历所有监听到的数据包
        if 'https://edith.xiaohongshu.com/api/sns/web/v1/you/mentions' in data.url:
            print(data.url,11111111111)  # 实时打印监听到的内容
            print(data.body)
    return HttpResponse('监听了')
    


