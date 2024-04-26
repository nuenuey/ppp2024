import os
import requests
url="http://api.taegon.kr/stations/146/?sy=2022&format=csv" #링크창 다운로드 받을 수 있다
#과제13번 메인함수써보기/ 과제 10번하기

filename="lec13/weather_146_2022.csv"

if not os.path.exists(filename):
    with open (filename, "w") as f:
        res=requests.get(url)
        f.write(res.text)