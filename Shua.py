from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json, time

def Start(driver, video_time, windows, year):
    try:
        while True:
            driver.find_element(By.LINK_TEXT, "开始学习").click()
            driver.implicitly_wait(1)
            driver.minimize_window()
            for window in driver.window_handles:
                if window not in windows:
                    driver.switch_to.window(window)
                    driver.minimize_window()
                    time.sleep(video_time)
                    driver.close()
            # 回到课程页面
            driver.switch_to.window(windows[1])
            driver.find_element(By.LINK_TEXT, "开始学习").send_keys(Keys.ENTER)
            driver.refresh()
            driver.implicitly_wait(1)
    except:
        try:
            while True:
                driver.find_element(By.LINK_TEXT, "继续学习").click()
                driver.implicitly_wait(1)
                driver.minimize_window()
                for window in driver.window_handles:
                    if window not in windows:
                        driver.switch_to.window(window)
                        driver.minimize_window()
                        time.sleep(video_time)
                        driver.close()
                # 回到课程页面
                driver.switch_to.window(windows[1])
                driver.find_element(By.LINK_TEXT, "继续学习").send_keys(Keys.ENTER)
                driver.refresh()
                driver.implicitly_wait(1)
        except:
            print("{}本年度已完成，或程序出错。".format(year))

if __name__ == "__main__":
    # read config file
    f = open("config.json", encoding="utf8")
    settings = json.load(f)
    f.close()

    browser = settings["Browser"]
    if browser == "Chrome":
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("start-maximized")
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=chrome_options, service=service)
    elif browser == "Edge":
        # 下载安装 msedgedriver from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        from selenium.webdriver.edge.options import Options

        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        edge_options.add_argument("start-maximized")
        driver = webdriver.Edge(options=edge_options)
    else:
        print("请使用Chrome、Firefox或者Edge浏览器。")

    # 登录系统
    url = "http://ptce.gx12333.net/"
    driver.get(url)

    ACCOUNT = settings["Username"]
    PASSWORD = settings["Password"]

    driver.find_element(By.ID, "username").send_keys(Keys.ESCAPE)
    driver.find_element(By.ID, "username").send_keys(ACCOUNT)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    print("在浏览器中输入验证码, 不要点击浏览器中的登录，回到此对话框，按回车进行下一步：")
    code = input()
    # driver.find_element(By.ID, "code").send_keys(code)
    try:
        driver.find_element(By.XPATH, "//input[@type='button' and @value='登录' and @onclick='lg();']").click()
    except:
        print("已经登录")

    # 获取窗口
    # Wait for the new window or tab
    while True:
        if "infocenter" in driver.current_url:
            break
        else:
            driver.implicitly_wait(0.5)

    # 进入学习页面
    driver.find_element(By.LINK_TEXT, "前往学习").click()
    windows = []
    windows.append(driver.current_window_handle)
    driver.implicitly_wait(1)
    for window in driver.window_handles:
        if window != windows[0]:
            driver.switch_to.window(window)
            windows.append(window)

    # 进入课程页面
    video_time = int(settings["video_time"]*60)

    years = settings["Years"]

    # 默认2022年
    if "2022" in years:
        Start(driver, video_time, windows, 2022)

    # 选择2021年
    if "2021" in years:
        driver.find_element(By.LINK_TEXT, "历年培训").click()
        driver.implicitly_wait(1)
        for window in driver.window_handles:
            if window not in windows:
                driver.switch_to.window(window)
                windows.append(window)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/table/tbody/tr[3]/td[4]/a").click()
        driver.implicitly_wait(1)
        Start(driver, video_time, windows, 2021)
    
    # 选择2020年
    if "2020" in years:
        driver.find_element(By.LINK_TEXT, "历年培训").click()
        driver.implicitly_wait(1)
        for window in driver.window_handles:
            if window not in windows:
                driver.switch_to.window(window)
                windows.append(window)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/table/tbody/tr[4]/td[4]/a").click()
        driver.implicitly_wait(1)
        Start(driver, video_time, windows, 2020)

    # 选择2019年
    if "2019" in years:
        driver.find_element(By.LINK_TEXT, "历年培训").click()
        driver.implicitly_wait(1)
        for window in driver.window_handles:
            if window not in windows:
                driver.switch_to.window(window)
                windows.append(window)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/form/table/tbody/tr[5]/td[4]/a").click()
        driver.implicitly_wait(1)
        Start(driver, video_time, windows, 2019)
