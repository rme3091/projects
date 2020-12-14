# Instagram selenium script to go to specifc pages and like/heart all photos
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# make sure pip is configured properly by entering 'pip' in cmd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import os
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Go to instagram
driver.get("https://www.instagram.com/"); 
driver.implicitly_wait(5)

# Login to instagram
login = open("userInfo.txt", "r").read().split("\n")
username = login[0]
password = login[1]
numPhotos = int((login[2])[25:])

# Function to remove all spaces from a given string 
def removeSpaces(string): 
    list = ""
  
    # Traverse the given string. If current character 
    # is not space, then place it at index 'count++' 
    for i in range(len(string)): 
        if string[i] != ' ': 
            list += (f"{ string[i] }") 
  
    return list

print(numPhotos)
useThisUsername = removeSpaces(username[9:])
useThisPassword = removeSpaces(password[9:])

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys(useThisUsername)		
password.send_keys(useThisPassword)				
password.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

# Prompt to save password info comes up, click not now button
button = driver.find_element_by_class_name("cmbtv")
button.click()
driver.implicitly_wait(5)
# Prompt to get notifications comes up, click not now button
notificationsButton = driver.find_element_by_class_name("mt3GC")
notificationsButton.click()

# Pages of instagram photos to like/heart
pageList = open("pages.txt", "r")
pagesToLike = pageList.read().split("\n")
print(len(pagesToLike))

time.sleep(1)
# Cycle through list of pages from pages.txt
for i in range(len(pagesToLike)):
	driver.get(pagesToLike[i])
	driver.implicitly_wait(5)
	time.sleep(2)
	firstPhoto = driver.find_element_by_class_name("eLAPa")
	firstPhoto.click()
	
	# View each photo on page
	j = 0
	while j < numPhotos:
		# Check to see if the photo already has a heart/like or not
		try:
			driver.find_element_by_css_selector("[aria-label='Unlike']")
			print("This photo was already liked")
		except NoSuchElementException:
			heart = driver.find_element_by_class_name("fr66n")
			time.sleep(1)
			heart.click()
			time.sleep(2)
		nextPhoto = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
		nextPhoto.send_keys(Keys.RIGHT)
		driver.implicitly_wait(5)
		time.sleep(2)
		j += 1

print("Done")
driver.quit()