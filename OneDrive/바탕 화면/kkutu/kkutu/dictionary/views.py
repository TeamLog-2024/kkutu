from django.shortcuts import render, redirect
from dictionary.models import Dictionary
import requests
from bs4 import BeautifulSoup

# Create your views here.

def main(request):
    return render(request, "main.html")


def wordsheet(request):
    return redirect("backletter")


def backletter(request):
    if request.method == "POST":
        first = request.POST.get("first")
        mission = request.POST.get("mission")
        length = request.POST.get("length")
        print(len(length))
        candidate = []
        for i in Dictionary.objects.all():
            corre = 0
            for j,k in zip(i.word, first):
                if j == k:
                    corre += 1
            if len(length) == 0:
                if corre == len(first):
                    candidate.append(i)
            else:
                if corre == len(first) and len(i.word) == int(length):
                    candidate.append(i)
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    class Word:
                        word = j
                        misnum = dic[j]
                    words.append(Word)
            mis -= 1
        
        placeholders = [first, mission, length]

        return render(request, "backletter.html", {"words" : words, "placeholders" : placeholders})
    return render(request, "backletter.html", {"placeholders" : ["시작 글자", "미션 글자", "단어 길이"]})


def frontletter(request):
    if request.method == "POST":
        last = request.POST.get("last")
        mission = request.POST.get("mission")
        length = request.POST.get("length")
        candidate = []
        for i in Dictionary.objects.all():
            corre = 0
            rev = -1
            for j in last:
                if j == i.word[rev]:
                    rev -= 1
                    corre += 1
            if len(length) == 0:
                if corre == len(last):
                    candidate.append(i)
            else:
                if corre == len(last) and len(i.word) == int(length):
                    candidate.append(i)
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    class Word:
                        word = j
                        misnum = dic[j]
                    words.append(Word)
            mis -= 1

            
        placeholders = [last, mission, length]

        return render(request, "frontletter.html", {"words" : words, "placeholders" : placeholders})
    return render(request, "frontletter.html", {"placeholders" : ["마지막 글자", "미션 글자", "단어 길이"]})


def attack(request):
    # 방금 시작함
    if request.method == "POST":
        first = request.POST.get("first")
        mission = request.POST.get("mission")
        length = request.POST.get("length")
        print(len(length))
        candidate = []
        for i in Dictionary.objects.all():
            corre = 0
            for j,k in zip(i.word, first):
                if j == k:
                    corre += 1
            if len(length) == 0:
                if corre == len(first):
                    candidate.append(i)
            else:
                if corre == len(first) and len(i.word) == int(length):
                    candidate.append(i)
        dic = {}
        for i in candidate:
            misnum = 0
            for j in i.word:
                if j == mission:
                    misnum += 1
            dic[i.word] = misnum

        mis = 6
        words = []
        for i in range(7):
            for j in dic:
                if dic[j] == mis:
                    class Word:
                        word = j
                        misnum = dic[j]
                    words.append(Word)
            mis -= 1
        
        placeholders = [first, mission, length]

        return render(request, "backletter.html", {"words" : words, "placeholders" : placeholders})
    return render(request, "backletter.html", {"placeholders" : ["시작 글자", "미션 글자", "단어 길이"]})



def database(request):
    li = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

    if request.method == "POST":
        category = request.POST.get("category")

        if category == "1":
            # 긴 단어(한국어)
            # for i in li:
            #     res = requests.get(f"https://kkukowiki.kr/w/긴_단어/한국어/{i}")
            #     soup = BeautifulSoup(res.text, "html.parser")
            #     for j in soup.select(".sortable > tbody > tr > td > a"):
            #         word = j.text
            #         if not Dictionary.objects.filter(word=word).exists():
            #             Dictionary.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "2":
            # 방어 단어(한국어)
            # for i in li:
            #     res = requests.get(f"https://kkukowiki.kr/w/방어단어/한국어/{i}")
            #     soup = BeautifulSoup(res.text, "html.parser")
            #     for j in soup.select(".sortable > tbody > tr > td > a"):
            #         word = j.text
            #         if not Dictionary.objects.filter(word=word).exists():
            #             Dictionary.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "3":
            # 긴 단어(영어)
            # res = requests.get(f"https://kkukowiki.kr/w/긴_단어/영어")
            # soup = BeautifulSoup(res.text, "html.parser")
            # for j in soup.select(".sortable > tbody > tr > td > a"):
            #     word = j.text
            #     if not Dictionary.objects.filter(word=word).exists():
            #         Dictionary.objects.create(word=word).save()
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "4":
            # 일반 단어(한국어)
            # f = open("db.sql", "r", encoding="utf-8")

            # data = f.readlines()[147827:579225:]

            # for i in data:
            #     word = ""
            #     for j in i:
            #         if j == "\t":
            #             if not Dictionary.objects.filter(word=word).exists():
            #                 Dictionary.objects.create(word=word).save()
            #             break
            #         word += j
            # 막아놓음
            return render(request, "disabled.html")


        elif category == "5":
            # 일반 단어(영어)
            # f = open("db.sql", "r", encoding="utf-8")

            # data = f.readlines()[794:147811:]
            # # data = f.readlines()[116634:147811:] # 중간 점검

            # for i in data:
            #     word = ""
            #     for j in i:
            #         if j == "\t":
            #             if not Dictionary.objects.filter(word=word).exists():
            #                 Dictionary.objects.create(word=word).save()
            #             break
            #         word += j
            # 막아놓음
            return render(request, "disabled.html")

        # if category == "6":
        #     return render(request, "preparing.html")

        else:
            return render(request, "NotFound.html")


    return render(request, "database.html")
