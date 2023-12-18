from DrissionPage import ChromiumPage
from DrissionPage.common import ActionChains
import time
import base64

# 指定不同人，不同端口
page = ChromiumPage(addr_driver_opts='127.0.0.1:9333')

# 跳转指定笔记页面
# page.get('https://www.xiaohongshu.com/explore/654ae03c0000000025009ac4')

## 跳转首页
page.get('https://www.xiaohongshu.com/')

# 获取页面控制器（暂时没有用）
ac = ActionChains(page)
# 点击对应的需要回复的
# ele1 = page.ele('#comment-65734419000000002200fa4b')
# ele2 = ele1.ele('.reply icon-container')
# ele2.click(by_js=True)

# page.ele('#content-textarea').input('你好吗，我是小红')

# subEle = page.ele('.btn submit')
# subEle.click(by_js=True)


# ## 滚动信息
# scrollEle = page.ele('#noteContainer')
# print(page.get_cookies(as_dict=False))
# for i in range(10):
#     time.sleep(2)
#     scrollEle.scroll.down(6000)

## 登录（保存图片，到时候回显给前端）
loginImgEle = page.ele('.qrcode-img')
src = loginImgEle.get_src()
file_path = './test.png'
with open(file_path, 'wb') as file:
    # 将二进制数据写入文件
    file.write(src)

# page.quit()


####   通知接口   https://edith.xiaohongshu.com/api/sns/web/unread_count