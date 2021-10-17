from selenium import webdriver
import time
import random

user_agents=[
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
    "Mozilla/5.0 (Windows NT 10.0; rv:87.0) Gecko/20100101 Firefox/87.0"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:87.0) Gecko/20100101 Firefox/87.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
    "Mozilla/5.0 (Windows NT 6.1; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 6.3; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 10.0; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
    "Mozilla/5.0 (Windows NT 6.1; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 6.3; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 10.0; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    "Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0"
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:84.0) Gecko/20100101 Firefox/84.0"
    
]

#Proxy="93.171.224.43:4153"


options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agents)}")
#options.add_argument('--proxy-server=%s' % Proxy)
driver = webdriver.Chrome(executable_path="D:/Projects/chromedriver.exe",options=options)
try:
    driver.get("https://vk.com/")
    

    email_input=driver.find_element_by_id("index_email")
    pass_input=driver.find_element_by_id("index_pass")
    email_input.clear()
    pass_input.clear()
    email_input.send_keys("89882001775")
    pass_input.send_keys("babahanula2007")

    enter_button=driver.find_element_by_id("index_login_button").click()

    time.sleep(3600)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()