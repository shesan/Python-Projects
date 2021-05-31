from time import sleep
from random import randint
from secrets import User, Pass, url, MATH2030, MATH1090
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


value = 0
start = time.time()


def increment():
    global value
    value = value + 1
    print("Loop Number: ", value)


def timelapse():
    global start
    end = time.time()
    print("Time Lapsed (SECONDS) = ", int(end - start))


class AutoBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.login()

    def login(self):
        self.driver.get(url)

        sleep(2)

        # Finds the REM weblink
        REM = self.driver.find_element_by_xpath('//*[@id="content"]/div/article/div/div[2]/div/ol/li[1]/a')
        REM.click()

        # User input
        userIn = self.driver.find_element_by_xpath('//*[@id="mli"]')
        userIn.send_keys(User)

        # Pass input
        passIn = self.driver.find_element_by_xpath('//*[@id="password"]')
        passIn.send_keys(Pass)

        # Enter
        enter = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input')
        enter.click()

        sleep(5)

        # Summer Select
        summer = Select(self.driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/select'))
        summer.select_by_value('1')

        # Enter
        enter2 = self.driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input')
        enter2.click()

        #
        #inside web
        #
        # addCourse = self.driver.find_element_by_xpath(
        #     '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[4]/tbody/tr[1]/td[1]/div/input')
        # addCourse.click()

        # sleep(randint(1, 2))
        # inpCourse = self.driver.find_element_by_xpath(
        #     '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[1]')
        # inpCourse.send_keys(MATH1090)

        # sleep(randint(1, 2))
        # self.driver.find_element_by_xpath(
        #     '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[2]').click()

        # sleep(randint(1, 2))
        # self.driver.find_element_by_xpath(
        #     '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[6]/td[2]/input[1]').click()

        # sleep(randint(1, 2))
        # self.driver.find_element_by_xpath(
        #     '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[7]/td[2]/span/input').click()

        # sleep(randint(2, 3))

        # Next Course input
        addCourse2 = self.driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[4]/tbody/tr[1]/td[1]/div/input')
        addCourse2.click()

        sleep(randint(1, 2))
        inpCourse2 = self.driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[1]')
        inpCourse2.send_keys(MATH2030)

        sleep(randint(1, 2))
        self.driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/span[2]/input[2]').click()

        sleep(randint(1, 2))
        self.driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[7]/td[2]/input[1]').click()

        sleep(randint(1, 2))
        self.driver.find_element_by_xpath(
            '/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[7]/td[2]/span/input').click()

        increment()
        timelapse()

        self.driver.quit()

AutoBot()
