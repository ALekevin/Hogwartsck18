from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_action():
    driver = webdriver.Chrome()
    driver.get('http://sahitest.com/demo/clicks.htm')
    dbl_element=driver.find_element(By.XPATH,'/html/body/form/input[2]')
    click_element=driver.find_element(By.XPATH,'/html/body/form/input[3]')
    rightclick_element=driver.find_element(By.XPATH,'/html/body/form/input[4]')
    clear_element=driver.find_element(By.XPATH,'/html/body/form/input[1]')
    action=ActionChains(driver)
    action.double_click(dbl_element).click(click_element).context_click(rightclick_element).move_to_element(clear_element).click().perform()
    sleep(3)
    driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
    drag_element=driver.find_element(By.ID,'dragger')
    drop_element=driver.find_element(By.XPATH,'/html/body/div[2]')
    action=ActionChains(driver)
    action.drag_and_drop(drag_element,drop_element).perform()
    sleep(3)
