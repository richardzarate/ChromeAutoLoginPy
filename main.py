from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
from time import sleep



#opens loginDetails.yml and saves it in the file variable
with open("loginDetails.yml", "r+") as file:
    conf = yaml.safe_load(file) #reads the contents of the file

#saves the username/email and password to their respected variables
myFbEmail = conf['fb_user']['email']
myFbPassword = conf["fb_user"]["password"]

#saves the driver for Chrome into the driver variable
driver = webdriver.Chrome()

#function for logging in to a website, allows the use of code on other websites as well
def login(url, usernameId, username, passwordId, password, submit_buttonName):
    driver.get(url) #opens a window to the specified url

    # finds the element on the page by its ID, then enters the given information
    driver.find_element(By.ID, usernameId).send_keys(username)
    driver.find_element(By.ID, passwordId).send_keys(password)

    #wait for everything to load in at least 1 sec
    sleep(1)

    #once the username and password are entered, click the login button
    driver.find_element(By.NAME, submit_buttonName).click()
    #keeps the window open
    input("Browser is open. Press Enter to exit...")

#currently working on facebook properly
login("https://www.facebook.com/", "email", myFbEmail, "pass", myFbPassword, "login")