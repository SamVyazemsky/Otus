from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from robot.api.deco import keyword
from . import variables


@keyword('Open Google')
def open_google():
    driver = webdriver.Chrome()
    driver.get(variables.url)
    elem = driver.find_element_by_name("q")
    elem.send_keys("Robot Framework")
    elem.send_keys(Keys.RETURN)
