import json, os, aiohttp
from config import *

import numpy as np
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

async def get_data():
    if os.path.exists(json_data_path):
        os.remove(json_data_path)

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://dhlottery.co.kr/gameResult.do?method=byWin")

    final_num = driver.find_element(By.XPATH, "//*[@id='article']/div[2]/div/div[2]/h4/strong").text

    driver.quit()

    final_num = int(final_num.split("회")[0])

    json_data = {}

    for i in range(1, final_num+1):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={i}") as resp:
                data = await resp.text()
                json_data[i] = json.loads(data)
    
    with open(json_data_path, "w") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

def get_all_numbers(data):
    with open(data, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for key, value in data.items():
        draw = value
        rows.append([
            draw['drwNo'], 
            draw['drwtNo1'], 
            draw['drwtNo2'], 
            draw['drwtNo3'], 
            draw['drwtNo4'], 
            draw['drwtNo5'], 
            draw['drwtNo6']
        ])
    
    return pd.DataFrame(rows, columns=['draw_no', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6'])


def preprocess_data(data):
    # 각 번호의 출현 여부를 이진 인코딩
    X = []
    y = []
    
    for index, row in data.iterrows():
        # 이전 5회의 번호를 입력으로 사용
        if index >= 5:
            previous_numbers = row[['num1', 'num2', 'num3', 'num4', 'num5', 'num6']].values
            X.append(previous_numbers)
            # 현재 회차의 번호를 출력으로 사용
            y.append(row[['num1', 'num2', 'num3', 'num4', 'num5', 'num6']].values)
    
    return np.array(X), np.array(y)