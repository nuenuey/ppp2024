#숫자 n이 주어짐, 1-n까지의 합, 함수명은 sum_n(n)

def sum_n(n):
    total=0
    for i in range(n):
        total=total+(i+1)
    return total
n= 5
result=sum_n(n)
print(f"1부터 {n}까지의 합은 {result}입니다")
