import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located


class FeedChanger:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        ROOT_DIR = os.path.abspath(os.curdir)

        chromedriver_autoinstaller.install()

        self.driver = webdriver.Chrome(options=opt)
        self.wait = WebDriverWait(self.driver, 120)



        """self.driver.get('https://accounts.google.com/')



        while True:
            url = self.driver.current_url
            if url == "https://myaccount.google.com/?pli=1":
                break"""

    def likeWatchVideo(self, videoId: str, watch_time: int):
        self.driver.get(f"https://www.youtube.com/watch?v={videoId}")
        Xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape"
        self.wait.until(visible((By.XPATH, Xpath)))
        self.driver.find_element(By.XPATH, Xpath).click()
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='skip-button:6']/span/button")))
        element.click()


        time.sleep(watch_time)


    def changeFeed(self, prompt, watchTime):
        search = prompt
        search = search.replace(" ", "+")







        self.driver.get(f'https://www.youtube.com/results?search_query={search}')
        self.wait.until(visible((By.ID, "video-title")))

        self.driver.execute_script("window.scrollTo(0, 100000)")

        source = self.driver.page_source
        print(source)
        ids = source.split('"videoId":"')[1:]
        for i, videoId in enumerate(ids):
            ids[i] = videoId.split('"')[0]
        ids = set(ids)
        print(len(ids))
        #print(driver.find_element("video-title")[0])
        print(ids)

        for videoId in ids:
            self.likeWatchVideo(videoId, watchTime)

feedChanger = FeedChanger()
feedChanger.likeWatchVideo("8tnf_LQTySM", 10)
#feedChanger.changeFeed("Chess", 30)
