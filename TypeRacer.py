from selenium import webdriver
import time 
import pyautogui

pyautogui.PAUSE = 0.001
# download latest chromedriver, then proceed

# Method - 1:
# driver = webdriver.Chrome("C:/Users/abhin/Desktop/chromedriver.exe") # was giving a warning about a)usb node not working and b)devtools listening

#Method - 2: [ No error ]
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='C:/Users/abhin/Desktop/chromedriver.exe', options=options)

driver.get("https://play.typeracer.com/") 

time.sleep(7)  # time to open chrome and load page

#Method - 1: [Using "link_text"]

join_game = driver.find_element_by_link_text("Enter a Typing Race")
#print(type(join_game))
join_game.click()

'''
#Method - 2: [won't work as beautiful doesn't let you click on a link (it parses html.xml etc not a link clicker)]
from bs4 import BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
join_game=soup.find('a',href=True, attrs={'class':'gwt-Anchor prompt-button bkgnd-green'})
print(type(join_game))
join_game.click()
'''

time.sleep(3) # give time to load next page

# retrieve text
game_text = driver.find_element_by_class_name("gameView").text # get all the text in the game area  
game_text = game_text.split("\n") # split the text into a list 

#print(game_text) #print the list

required_text = game_text[-3] #get only the nexessary text
print(required_text)

time.sleep(14)

pyautogui.typewrite(required_text,interval = 0.01)

time.sleep(20)

driver.quit()