import time
import json
import stomp
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 待查询信息

AMQHOST = "mq.ossez.com"
AMQPORT = 61616
AMQUSER = "artemis"
AMQPASS = "artemis"
TOPICNAME = "policyQueue"

begin_year = input("请输入最早年份:")
current_timestamp = time.time()
time_tuple = time.localtime(current_timestamp)
end_year = time_tuple.tm_year

wait_time = 0.5  # 等待时间
action_pixel = 100  # 鼠标滚动像素

# get网站
chrome = Chrome(service=Service(r"C:\Users\yhu\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"))
chrome.get('https://www.isharkfly.com/')
wait = WebDriverWait(chrome, 10)
rowContent = chrome.find_elements(By.XPATH, '/html/body/div[3]/div/div/div/div[4]/div/table/tbody/tr')
main_window = chrome.current_window_handle


def send_mq(ctxInfo, ctx):
    for summary in ctxInfo.splitlines():
        if summary.startswith('索引号'):
            index_string = summary.split('：')[1]
        elif summary.startswith('发文日期'):
            policyDateTime = summary.split('：')[1]
        elif summary.startswith('名称'):
            policy_name = summary.split('：')[1]

    data = {}
    data['policy_index_number'] = index_string
    data['policy_title'] = policy_name
    data['policy_content'] = ctx

    hosts = [(AMQHOST, AMQPORT)]
    conn = stomp.Connection(host_and_ports=hosts, auto_content_length=False)
    conn.connect(username=AMQUSER, passcode=AMQPASS, wait=True)
    conn.send(body=json.dumps(data), destination=TOPICNAME)
    time.sleep(1)
    conn.disconnect()


for tr in rowContent:

    tdList = tr.find_elements("xpath", 'td')
    indexNumber = tdList[0].text
    docName = tdList[1].text
    tdList[1].find_element(By.TAG_NAME, 'a').click()
    docDate = tdList[2].text
    wait.until(EC.number_of_windows_to_be(2))
    # Loop through until we find a new window handle
    for window_handle in chrome.window_handles:
        if window_handle != main_window:
            chrome.switch_to.window(window_handle)
            break
    ctxInfo = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[1]/ul').text
    ctx = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[2]').text
    send_mq(ctxInfo, ctx)
    chrome.close()
    chrome.switch_to.window(main_window)
    print(docName)
    # break

chrome.quit()
