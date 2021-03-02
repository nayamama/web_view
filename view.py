from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
import time
import random

#t = time.localtime()
#current_time = time.strftime("%m/%d/%Y, %H:%M:%S")
#print(current_time)
#print("=======================================")

# The urls for all possible videos
media = ["https://v.qq.com/x/cover/mzc00200js3mdvw/q00354i139r.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/j00357b0cuz.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/p003524sofe.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/a00353f725d.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/s003537tpor.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/n003541yb8q.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/r0035tg5brg.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/l0035pno4wy.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/h00350k7goi.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/q0035cv7esm.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/u0035nkcd9y.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/l00357clii4.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/h0035ixn0dz.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/e0035a9lm9l.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/w00353nzvuh.html",
         "https://v.qq.com/x/cover/mzc00200js3mdvw/t0035iwvazc.html"]

# Start headless Google driver

options = Options()
options.headless = True
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

"""
# Start regular Google driver
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
                          #service_args=["--verbose", "--log-path=/home/qi/PycharmProjects/web_view/chrome.log"])
"""


i = 0

# for i in range(10):
while True:
    try: 
        i += 1
        current_time = time.strftime("%m/%d/%Y, %H:%M:%S")
        print(current_time)
        print("Running the video for {} time".format(i))
        print("=======================================")
        #driver.get("https://v.qq.com/x/page/w3228bfxa8z.html")
        video_id = random.randint(0, len(media) - 1)
        driver.get(media[video_id])
        sleep_time = random.randint(180, 280)
        time.sleep(sleep_time)
    except TimeoutException:
        print("Oops! There is a timeout error.")
        driver.close()
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)
    finally:
        print("Oops! There is a web-driver error.")
        driver.close()
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)
