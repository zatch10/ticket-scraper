from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


browser = webdriver.Firefox(executable_path='/home/~')
browser.get("https://www.redbus.in/bus-tickets/")
to = input("Enter your destination: ")
browser.find_element_by_link_text('To').click()

<input type="text" id="txtSource" autocomplete="off" class="search-input" placeholder="FROM">