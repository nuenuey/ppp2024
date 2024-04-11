# 2. 몇 c층의 삼각형을 만들까요?

n=int(input("몇 층의 삼각형을 만들까요?"))
if n==1:
    print("1개의 *로는 삼각형을 만들 수 없습니다.")
else:
    total=0
    for i in range(n):
        total= total+ (i+1)
        print("*"*total)
