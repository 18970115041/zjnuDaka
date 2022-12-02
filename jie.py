from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://zyt.zjnu.edu.cn/H5/Login.aspx?OP=phone_html5')
browser.find_element(By.ID,'UserText').send_keys('202207001169') # 学号
browser.find_element(By.ID,'PasswordText').send_keys('287832') # 身份证后6位
browser.find_element(By.ID,'btn_Login').click()

browser.get('http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx?address=%E6%B5%99%E6%B1%9F%E7%9C%81%E2%9C%B0%E9%87%91%E5%8D%8E%E5%B8%82%E2%9C%B0%E5%A9%BA%E5%9F%8E%E5%8C%BA')
browser.find_element(By.ID,'DATA_5_1').click()
browser.find_element(By.ID,'DATA_13_1').click()
browser.find_element(By.ID,'DATA_15').click()
submit = browser.find_element(By.ID,'btn_save')
submit.click() # 上报