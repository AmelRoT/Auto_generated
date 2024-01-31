from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()


Songs = [
    "Le Monde Chico (2015) - PNL",
    "Dans la légende (2016) - PNL",
    "Deux Frères (2019) - PNL",
    "Naha (2015) - PNL",
    "DA (2016) - PNL",
    "J'suis QLF (2016) - PNL",
    "Oh Lala (2016) - PNL",
    "Au DD (2019) - PNL",
    "91's (2015) - PNL",
    "Tchiki Tchiki (2015) - PNL",
    "La vie est belle (2015) - PNL",
    "Tempête (2016) - PNL",
    "A l'ammoniaque (2018) - PNL",
    "Blanka (2015) - PNL",
    "Sheita (2016) - PNL"
]




# You can access individual songs using indexing, for example:




Url = []; 

try:
    for song in Songs:
        # Open YouTube
        driver.get("https://www.youtube.com")
        driver.implicitly_wait(6)

        # Find the search input element by name attribute
        search_box = driver.find_element(By.NAME, "search_query")

        # Type the current song as the search query
        search_box.send_keys(song)

        # Press Enter to initiate the search
        search_box.send_keys(Keys.RETURN)

        # Wait for some time to let the search results load
        time.sleep(5)

        # Click on the first video thumbnail
        thumbnail_image = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img")
        thumbnail_image.click()

        # Wait for some time to let the video page load
        time.sleep(3)

        # Retrieve the current video URL
        video_url = driver.current_url
        Url.append(video_url)
        print(f"Video URL for {song}: {video_url}")
        time.sleep(2)


    for url in Url: 
        driver.get("https://ytmp3.nu/CNtD/")
        time.sleep(2)
        search_box1 = driver.find_element(By.XPATH, '//*[@id="url"]')
        search_box1.send_keys(url)
        search_box1.send_keys(Keys.RETURN)
        time.sleep(4)
        clicking_down = driver.find_element(By.XPATH, '/html/body/form/div[2]/a[1]')
        clicking_down.click() 
        time.sleep(6)
        print(f"Downloaded URL for {url}")


finally:
    
    print("Ende ")
    for i in range(0,len(Url)): 
        print(Url[i]) 
    # Close the browser window
    driver.quit()
