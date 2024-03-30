def largest(a,b,c):

    if a>b and a>c:
      return a #largest_num= a와 같은 코드
    elif b>a and b>c:
      return b
    elif c>a and c>b:
      return c
#if a>b:
#    if a>c:  
#       return a
#    else:
#       return c
#    else: # a<= b
#        if b>c:
#            return b
#        else: 
#            return c  
    

def main():

    x1=5
    x2=7
    x3=3

    largest_num =largest(x1, x2, x3)

    print(f"가장 큰 수는 {largest_num}입니다.")


if __name__ == "__main__":
    main()