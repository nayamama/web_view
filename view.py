from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

t = time.localtime()
current_time = time.strftime("%m/%d/%Y, %H:%M:%S")
print(current_time)
print("=======================================")

media = ["https://v.qq.com/x/cover/mzc00200js3mdvw/j00357b0cuz.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/j00357b0cuz.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/p003524sofe.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/a00353f725d.html"]

# Start headless Google driver
options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",
                          service_args=["--verbose", "--log-path=/home/qi/PycharmProjects/web_view/chrome.log"],
                          chrome_options=options)

"""
# Start regular Google driver
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",
                          service_args=["--verbose", "--log-path=/home/qi/PycharmProjects/web_view/chrome.log"])

"""

for i in range(10):
    print("Running the video for {} time".format(i))
    driver.get("https://v.qq.com/x/page/w3228bfxa8z.html")
    sleep_time = random.randint(10, 25)
    time.sleep(sleep_time)

driver.close()