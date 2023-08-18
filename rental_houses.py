import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
'''A.first webscrape the data from the site for:
1.Rent
2.Area
3.Link
B.Fill the form for each property
C.Generate google spreadsheet
'''
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.quikr.com/homes/property/residential-apartments-for-rent-in-vizag-cid_531001')
time.sleep(2)
prices = driver.find_elements(By.CLASS_NAME,'prsg')
location = driver.find_elements(By.CLASS_NAME,'listloc')
links = driver.find_elements(By.CLASS_NAME,'tophe')
for i in range(0,len(links)):
    links[i] = links[i].find_element(By.TAG_NAME,'a')
    links[i] = links[i].get_attribute('href')
data = []
for i in range(0,len(prices)):
    sub_data = []
    sub_data.append(location[i].text)
    sub_data.append(prices[i].text.replace(',',''))
    sub_data.append(links[i])
    data.append(sub_data)
driver.quit()
out = len(links)
out = 5
for i in range(0,out):
    form = webdriver.Chrome(options=options)
    form.get('https://forms.gle/p8HKU5aFFAX3ccwb7')
    time.sleep(1)
    text_boxes = form.find_elements(By.CSS_SELECTOR, "textarea")
    time.sleep(1)
    time.sleep(1)
    text_boxes[0].send_keys(data[i][0])
    time.sleep(1)
    text_boxes[1].send_keys(data[i][1])
    time.sleep(1)
    text_boxes[2].send_keys(data[i][2])
    time.sleep(1)
    submit = form.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(1)
    another_response = form.find_element(By.CSS_SELECTOR,"a").click()
    time.sleep(1)
    form.quit()
spreadsheet = webdriver.Chrome(options=options)

spreadsheet.get('https://docs.google.com/forms/d/1n7bxqKK8xVhRs96uXSAdhTJsWzcDaVaP3M52KSmN50Y/edit#responses')
# spreadsheet.find_element(By.XPATH,'//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]')
