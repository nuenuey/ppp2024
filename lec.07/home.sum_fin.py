#숫자 n이 주어짐, 1-n까지의 합

def sum_n(n):
    total=0
    for i in range(n):
        total=total+(i+1)
    return total
    
    

def main():
    n=5
    result=sum_n(n)
    print(f"1부터 {n}까지의 합은 {result}입니다")


if __name__ == "__main__":
    main()