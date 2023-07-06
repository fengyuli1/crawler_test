import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建一个参数对象，用来控制chrome以无界面模式打开（可以视为固定写法）
opt = Options()  # 新建参数对象
opt.add_argument("--headless")  # 无头
opt.add_argument("--disbale-gpu")  # 无gpu图形化界面

dirver = webdriver.Chrome(options=opt)  # 把参数配置设置到浏览器中
dirver.get("https://kyfw.12306.cn/otn/resources/login.html")
time.sleep(1)
dirver.find_element(
    by="xpath", value='//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a'
).click()
time.sleep(1)
dirver.find_element(by="id", value="J-userName").send_keys("11111111111111111")
dirver.find_element(by="id", value="J-password").send_keys("111111111111111111")
time.sleep(1)
dirver.find_element(by="id", value="J-login").click()
time.sleep(1)
# 这里比较重要了，这里就是利用这个代码，来更改selenium中的滑动功能，让网站不报错
script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
dirver.execute_script(script)

while True:
    try:
        btn = dirver.find_element(
            by="xpath", value='//*[@class="nc_iconfont btn_slide"]'
        )
        action = webdriver.ActionChains(dirver)
        action.click_and_hold(btn)
        action.drag_and_drop_by_offset(btn, 400, 0).perform()
        info = dirver.find_element(
            by="xpath", value='//*[@class="errloading"]/span'
        ).text
        action.release()
        if info == "哎呀，出错了，点击刷新再来一次":
            dirver.find_element(
                by="xpath", value='//*[@class="errloading"]/span/a'
            ).click()
            time.sleep(0.2)
    except Exception:
        print(11111111111111)
        break
time.sleep(3)
dirver.quit()
