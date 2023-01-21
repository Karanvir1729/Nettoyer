search = "Chess"
search.replace(" ", "+")
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)
driver.get('https://accounts.google.com/')

wait = WebDriverWait(driver, 120)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located


while True:
    url = driver.current_url
    if url == "https://myaccount.google.com/?pli=1":
        break

def likeWatchVideo(videoId: str, watch_time: int):
    driver.get(f"https://www.youtube.com/watch?v={videoId}")
    Xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape"
    wait.until(visible((By.XPATH, Xpath)))
    driver.find_element(By.XPATH, Xpath).click()

    time.sleep(watch_time)





driver.get(f'https://www.youtube.com/results?search_query={search}')
wait.until(visible((By.ID, "video-title")))

driver.execute_script("window.scrollTo(0, 100000)")

source = driver.page_source
print(source)
ids = source.split('"videoId":"')[1:]
for i, videoId in enumerate(ids):
    ids[i] = videoId.split('"')[0]
ids = set(ids)
print(len(ids))
#print(driver.find_element("video-title")[0])
print(ids)

for videoId in ids:
    likeWatchVideo(videoId, 1200)

