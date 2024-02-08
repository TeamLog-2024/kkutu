import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

session = requests.Session()
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
			AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
			"Accept":"text/html,application/xhtml+xml,application/xml;\
			q=0.9,imgwebp,*/*;q=0.8"}

for k in range(2,60):
    url = f"https://wordbook.daum.net/open/wordbook.do?id=2869816&&page={k}"
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, "html.parser")

    word = {}
    for i in soup.select(".wrap_word"):
        word[i.select_one(".txt_word > div > .link_wordbook").text] = i.select_one(".mean_info > p > .link_mean").text


    for i in word:
        print(i, word[i])