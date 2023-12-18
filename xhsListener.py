from FlowViewer import Listener

listener =Listener(9333)  # 创建监听器，监听9222端口的浏览器
listener.listen()  # 开始监听，不设置目标，无限制监听

for data in listener.steps():  # 遍历所有监听到的数据包
    if 'https://edith.xiaohongshu.com/api/sns/web/v1/you/mentions' in data.url:
        print(data.url,11111111111)  # 实时打印监听到的内容
        print(data.body)