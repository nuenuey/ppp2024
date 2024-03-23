for i in range(10):
    print(i)
#출력 0,2,3,4,5,6,7,8,9 // 인덱스 i

#1부터 10까지 합    
n=10
total=0
for i in range(n):
    total= total + (i+1)
print(f"1부터 10까지의 합은 {total:,}입니다.")


n=250
total=0
for i in range(n):
    if (i+1)%2==0 :
        total= total + (i+1)
print(f"250까지의 짝수 합은 {total:,}입니다.")

