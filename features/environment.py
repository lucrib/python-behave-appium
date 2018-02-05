# from selenium.webdriver import Chrome, ChromeOptions
from appium import webdriver


def before_all(ctx):
    # start appium server
    # setup the android device
    # start android device
    pass


def after_all(ctx):
    # shutdown android device
    # shutdown appium server
    pass


def before_scenario(ctx, scenario):
    # start browser
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        # "platformVersion": "8.0",
        "browserName": "Chrome",
        # "browserVersion": ""
    }
    ctx.browser = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
    # chrome_options = ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # ctx.browser = Chrome(chrome_options=chrome_options)
    ctx.browser.implicitly_wait(10)


def after_scenario(ctx, scenario):
    ctx.browser.quit()
