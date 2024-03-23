#문자열, 글자수 계산
text = input("영어 단어를 입력하세요.")

print('입력한 문자는 "{}"입니다.'.format(text))
print(len(text))
print(text.upper())
#text뒤에 . 을 찍으면 관련 명령어가 나옴
# text.upper = 대문자 만들기

print(5*20) 
#계산
print("5"*20) 
#20번 출력하라

print("="*30)

print(text[:3])
print(text[-2:])

print(text[4])