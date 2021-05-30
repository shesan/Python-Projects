from selenium import webdriver

url = "https://aislesofglory.nofrills.ca/"

chromedriver = "C:/Users/Shesan/Desktop/a/Chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get(url)

Actions act = new Actions(driver)
act.moveByOffset(913, 477).contextClick().build().perform()