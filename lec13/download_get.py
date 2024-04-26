import requests #뒤의 모듈을해

URL = "https://coopjbnu.kr/function/ajax.get.rest.data.php"



with open("./cafeteria_menu.html", "w", encoding="UTF-8") as f: #파일이름, .은 현재폴더/..은 상위폴더
    res = requests.post(URL) #포스트에 url있고 자료널기
    res.encoding = "UTF-8"
    f.write(res.text)