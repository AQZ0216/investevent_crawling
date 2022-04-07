#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import bs4.element
import time
import csv

## paremeter
cookies = {
    'juzi_user': '',
    'juzi_token': '',
}

headers = {
    'authority': 'www.itjuzi.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'accept': 'application/json, text/plain, */*',
    'authorization': '',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.itjuzi.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.itjuzi.com/investevent?time=2021,2022,2020&tag=%E6%96%B0%E6%9D%90%E6%96%99&type=1',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
}


# In[ ]:


## paremeter
num_pages = 22

cnt = 0 ## verbose
with open('新材料.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['时间', '公司名', '行业', '轮次', '金额', '投资方', '最新估值(估算)(万)', '标签', '基本信息', '团队信息'])
    
    for i in range(num_pages):  
        json_data = {
            'tag': '\u65B0\u6750\u6599',
            'time': [
                '2021',
                '2022',
                '2020',
            ],
            'type': 1,
            'page': i+1,
            'per_page': 20,
        }

        r1 = requests.post('https://www.itjuzi.com/api/v1/investevents', headers=headers, cookies=cookies, json=json_data)
        
        for j in r1.json()["data"]["data"]:            
            headers2 = {
                'authority': 'www.itjuzi.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
            }
            
            r2 = requests.get('https://www.itjuzi.com/company/'+str(j["com_id"]), headers=headers2, cookies=cookies)
            soup2 = BeautifulSoup(r2.text, 'html.parser')
            print(cnt, r2) ## verbose
            time.sleep(1)
            
            ## investor
            investor_text = ""
            for k in range(len(j["investor_info"])):
                if k != 0:
                    investor_text += ', '
                investor_text += j["investor_info"][k]["name"]
            
            ## tags
            a_tags = soup2.find(class_="company-tags").find_all("a")
            tags = ""
            for k in range(3):
                if k != 0:
                    tags += "、"
                tags += a_tags[k].string
            
            ## person
            soup2.find(id="person").h3.extract()
            person_text = ""
            for k in soup2.find(id="person").strings:
                if k != " ":
                    if k.endswith(' '):
                        person_text += k 
                    else:
                        person_text += k + ' '
            
            writer.writerow([j["agg_time"], j["name"], j["com_scope"], j["round"], j["money"], investor_text, j["valuation"], tags, soup2.find(id="desc").p.string, person_text])
            cnt += 1


# In[ ]:


## paremeter
num_pages = 20

cnt = 0 ## verbose
with open('新能源.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['时间', '公司名', '行业', '轮次', '金额', '投资方', '最新估值(估算)(万)', '标签', '基本信息', '团队信息'])
    
    for i in range(num_pages):  
        json_data = {
            'tag': '\u65B0\u80FD\u6E90',
            'time': [
                '2021',
                '2022',
                '2020',
            ],
            'type': 1,
            'page': i+1,
            'per_page': 20,
        }

        r1 = requests.post('https://www.itjuzi.com/api/v1/investevents', headers=headers, cookies=cookies, json=json_data)
        
        for j in r1.json()["data"]["data"]:            
            headers2 = {
                'authority': 'www.itjuzi.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
            }
            
            r2 = requests.get('https://www.itjuzi.com/company/'+str(j["com_id"]), headers=headers2, cookies=cookies)
            soup2 = BeautifulSoup(r2.text, 'html.parser')
            print(cnt, r2) ## verbose
            time.sleep(1)
            
            ## investor
            investor_text = ""
            for k in range(len(j["investor_info"])):
                if k != 0:
                    investor_text += ', '
                investor_text += j["investor_info"][k]["name"]
            
            ## tags
            a_tags = soup2.find(class_="company-tags").find_all("a")
            tags = ""
            for k in range(3):
                if k != 0:
                    tags += "、"
                tags += a_tags[k].string
            
            ## person
            soup2.find(id="person").h3.extract()
            person_text = ""
            for k in soup2.find(id="person").strings:
                if k != " ":
                    if k.endswith(' '):
                        person_text += k 
                    else:
                        person_text += k + ' '
            
            writer.writerow([j["agg_time"], j["name"], j["com_scope"], j["round"], j["money"], investor_text, j["valuation"], tags, soup2.find(id="desc").p.string, person_text])
            cnt += 1


# In[ ]:


## paremeter
num_pages = 28

cnt = 0 ## verbose
with open('机器人.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['时间', '公司名', '行业', '轮次', '金额', '投资方', '最新估值(估算)(万)', '标签', '基本信息', '团队信息'])
    
    for i in range(num_pages):  
        json_data = {
            'tag': '\u673A\u5668\u4EBA',
            'time': [
                '2021',
                '2022',
                '2020',
            ],
            'type': 1,
            'page': i+1,
            'per_page': 20,
        }

        r1 = requests.post('https://www.itjuzi.com/api/v1/investevents', headers=headers, cookies=cookies, json=json_data)
        
        for j in r1.json()["data"]["data"]:            
            headers2 = {
                'authority': 'www.itjuzi.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
            }
            
            r2 = requests.get('https://www.itjuzi.com/company/'+str(j["com_id"]), headers=headers2, cookies=cookies)
            soup2 = BeautifulSoup(r2.text, 'html.parser')
            print(cnt, r2) ## verbose
            time.sleep(1)
            
            ## investor
            investor_text = ""
            for k in range(len(j["investor_info"])):
                if k != 0:
                    investor_text += ', '
                investor_text += j["investor_info"][k]["name"]
            
            ## tags
            a_tags = soup2.find(class_="company-tags").find_all("a")
            tags = ""
            for k in range(3):
                if k != 0:
                    tags += "、"
                tags += a_tags[k].string
            
            ## person
            soup2.find(id="person").h3.extract()
            person_text = ""
            for k in soup2.find(id="person").strings:
                if k != " ":
                    if k.endswith(' '):
                        person_text += k 
                    else:
                        person_text += k + ' '
            
            writer.writerow([j["agg_time"], j["name"], j["com_scope"], j["round"], j["money"], investor_text, j["valuation"], tags, soup2.find(id="desc").p.string, person_text])
            cnt += 1


# In[ ]:




