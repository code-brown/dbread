from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver_path = r'F:\ST\python\msedgedriver.exe'

driver = webdriver.Edge()

target_file = input("输入目标文件") + ".txt"
chapter_number = input("输入章节号（如 '一'、'二' 等）: ")
chapter = "第"+chapter_number+"章"

with open(target_file, "w", encoding="utf-8") as f:
    driver.get('https://read.douban.com/column/64721393/chapters?dcs=column&dcm=chapter-list')
    title = driver.find_element(By.XPATH, f"//div[@class='title-text' and contains(text(), \"{chapter}\")]")
    print(title.text)
    f.write(title.text + "\n\n")
    time.sleep(5)

    title.click()
    time.sleep(5)
    words = driver.find_elements(By.TAG_NAME, "p")
    for word in words:
        text = word.text.strip()
        if text:
            f.write(word.text + "\n")
