import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r'C:\Users\colin\Desktop\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_css_selector('#cookie')
cookies_per_second = driver.find_element_by_css_selector('#cps')


def click_cookie():
    global cookie
    cookie.click()

def purchase():
    cursor_cost = int(driver.find_element_by_css_selector('#buyCursor b').text.split(' - ')[1].replace(',', ""))
    grandma_cost = int(driver.find_element_by_css_selector('#buyGrandma b').text.split(' - ')[1].replace(',', ""))
    factory_cost = int(driver.find_element_by_css_selector('#buyFactory b').text.split(' - ')[1].replace(',', ""))
    mine_cost = int(driver.find_element_by_css_selector('#buyMine b').text.split(' - ')[1].replace(',', ""))
    shipment_cost = int(driver.find_element_by_css_selector('#buyShipment b').text.split(' - ')[1].replace(',', ""))
    alchemy_lab_cost = int(driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b').text.split(' - ')[1].replace(',', ""))
    portal_cost = int(driver.find_element_by_css_selector('#buyPortal b').text.split(' - ')[1].replace(',', ""))
    time_machine_cost = int(driver.find_element_by_xpath('//*[@id="buyTime machine"]/b').text.split(' - ')[1].replace(',', ""))

    global timer_toggle
    money = driver.find_element_by_css_selector('#money')
    money = int(money.text)
    if money >= 15:
        if money >= time_machine_cost:
            time_machine = driver.find_element_by_xpath('//*[@id="buyTime machine"]')
            time_machine.click()
        elif money >= portal_cost:
            portal = driver.find_element_by_css_selector('#buyPortal')
            portal.click()
        elif money >= alchemy_lab_cost:
            alchemy_lab = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]')
            alchemy_lab.click()
        elif money >= shipment_cost:
            shipment = driver.find_element_by_css_selector('#buyShipment')
            shipment.click()
        elif money >= mine_cost:
            mine = driver.find_element_by_css_selector('#buyMine')
            mine.click()
        elif money >= factory_cost:
            factory = driver.find_element_by_css_selector('#buyFactory')
            factory.click()
        elif money >= grandma_cost:
            grandma = driver.find_element_by_css_selector('#buyGrandma')
            grandma.click()
        elif money >= cursor_cost:
            cursor = driver.find_element_by_css_selector('#buyCursor')
            cursor.click()


    timer_toggle = True

def end_game():
    global toggle, cookies_per_second
    print(cookies_per_second.text)
    driver.quit()
    toggle = False


toggle = True
timer_toggle = True
clicker_timer = threading.Timer(300, end_game)
clicker_timer.start()

while toggle:
    click_cookie()
    if timer_toggle:
        timer = threading.Timer(2.5, purchase)
        timer.start()
        timer_toggle = False
