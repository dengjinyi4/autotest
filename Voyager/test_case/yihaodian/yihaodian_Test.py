#!/usr/bin/env python
# encoding: utf-8
import os,time,datetime
from selenium import webdriver
# from selenium import By
from selenium.webdriver.support.ui import WebDriverWait
# import selenium
def yihaodian():
    chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # chromedriver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    driver.set_page_load_timeout(30)
    # driver.maximize_window()
    driver.get("http://open.yhd.com/apitools/apiTools.do?pageMethod=yhd.union.clickUrl.get&pageCateId=15")
    # driver.refresh()
    time.sleep(3)
    driver.find_element_by_id('tmpAppkey').send_keys('10220017031500004360')
    driver.find_element_by_id('appSecret').send_keys('841e2c938d581b1a66ac8de3c2f94e1d')
    WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath(r'//*[@id="appParams"]/tbody/tr[1]/td[2]/input').is_displayed())
    driver.find_element_by_xpath('//*[@id="appParams"]/tbody/tr[1]/td[2]/input').send_keys('6258')
    driver.find_element_by_xpath('//*[@id="appParams"]/tbody/tr[2]/td[2]/input').send_keys('https://www.yhd.com')
    driver.find_element_by_xpath('//*[@id="appParams"]/tbody/tr[3]/td[2]/input').send_keys('871361')
    driver.find_element_by_xpath('//*[@id="appParams"]/tbody/tr[4]/td[2]/input').send_keys('123456')
    for i in range(1,5):
        # driver.switch_to.frame('toSubmitRequest')
        driver.switch_to_default_content()
        WebDriverWait(driver,20).until(lambda the_driver: the_driver.find_element_by_xpath(r'//*[@id="btnToSubmit"]/span/span').is_displayed())
        driver.find_element_by_xpath('//*[@id="btnToSubmit"]/span/span').click()
        # WebDriverWait(driver,50).until(lambda the_driver: the_driver.find_element_by_xpath(r'//*[@id="appResult"]/text()').is_displayed())
        driver.switch_to.frame('formSumit')
        r=driver.find_element_by_id('appResult').text
        # req = wd.findElement(By.id("req")).getAttribute("value");
        print i
        print r
    # driver.quit()
    driver.close()
    return

if __name__ == '__main__':
    yihaodian()

    # 判断是否隔天，如果隔天只取字符串后五位
