from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
from word.models import Word
import time
from selenium.webdriver.common.by import By
from django.http import HttpResponse
from random import randint as ri
    

# Create your views here.
def main(request):
    return render(request, "main.html")

def crawling(request):
    if request.method == "POST":
        session = requests.Session()
        header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
                    AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                    "Accept":"text/html,application/xhtml+xml,application/xml;\
                    q=0.9,imgwebp,*/*;q=0.8"}
        
        word = {}

        for k in range(2,60):
            url = request.POST.get("url") + f"&&page={k}"
            res = requests.get(url, headers=header)
            soup = BeautifulSoup(res.text, "html.parser")

            for i in soup.select(".wrap_word"):
                word[i.select_one(".txt_word > div > .link_wordbook").text] = i.select_one(".mean_info > p > .link_mean").text

        for i in word:
            if not Word.objects.filter(word=i).exists():
                Word.objects.create(word=i, mean=word[i]).save()

        return render(request, "main.html")
    return render(request, "crawling.html")

def word(request):
    words = Word.objects.all()
    return render(request, "word.html", {"words" : words})

def test(request):
    word = []
    mean = []
    words = {}
    means = {}
    candidate = Word.objects.all()
    for i in range(10):
        word.append(ri(0, len(candidate) - 1))
        mean.append(ri(0, len(candidate) - 1))
    for i, j in enumerate(word, 0):
        words[candidate[j]] = i
    for i, j in enumerate(mean, 0):
        means[candidate[j]] = i
    
    return render(request, "test.html", {"words" : words, "means" : means})