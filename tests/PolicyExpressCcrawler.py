import time
import requests
import stomp
import json
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


def send_mq(data):
    hosts = [(AMQHOST, AMQPORT)]
    conn = stomp.Connection(host_and_ports=hosts, auto_content_length=False)
    conn.connect(username=AMQUSER, passcode=AMQPASS, wait=True)
    conn.send(body=json.dumps(data), destination=TOPICNAME)

    conn.disconnect()


# https://policyapi.10nservice.com/api/v1/WebPolicy/GetSearchPageList?pageSize=50&pageIndex=1&postType=99&release=&years=&area=430100&platformId=3479085520414310401

def do_data_crawl(page_index):
    URL = "https://policyapi.10nservice.com/api/v1/WebPolicy/GetSearchPageList"
    PARAMS = {'pageSize': 5000, 'pageIndex': page_index, 'postType': 99, 'postType': '', 'years': '', 'area': 430100,
              'platformId': 3479085520414310401}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    responseData = r.json()

    # Loop List
    for policyList in json.loads(responseData['Data']):
        pid = policyList['PID']
        policyTitle = policyList['PolicyTitle']
        detail_url = "https://policyapi.10nservice.com/api/v1/WebPolicy/GetAdoptDetails?pid=" + pid + "&platformId=3479085520414310401"
        request_detail_data = requests.get(url=detail_url).json()
        province_id = json.loads(request_detail_data['Data'])['ProvinceID']

        data = {}
        data['policy_index_number'] = pid
        data['policy_title'] = policyTitle
        data['policy_content'] = json.loads(request_detail_data['Data'])['PolicyText']
        data['policy_tag'] = json.loads(request_detail_data['Data'])['PolicyKey']
        data['release_time'] = json.loads(request_detail_data['Data'])['ReleaseTime']
        data['start_time'] = json.loads(request_detail_data['Data'])['StarTime']
        data['end_time'] = json.loads(request_detail_data['Data'])['EndTime']
        data['source_name'] = json.loads(request_detail_data['Data'])['Source']
        data['source_url'] = json.loads(request_detail_data['Data'])['PageUrl']

        send_mq(data)

        print(policyTitle)
        # break


for i in range(3, 6):
    do_data_crawl(i)
    # break
