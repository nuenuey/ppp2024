def minmax(nums):
    max_num= max(nums)
    min_num=min(nums)
    return min_num, max_num
    

def main():
    x = [3, 7, 25, 10, 2, 13]
    mn = minmax(x)[0]
    mx = minmax(x)[1]
   
    print(f"가장 작은 수는 {mn}이고, 가장 큰 수는 {mx}입니다.")

if __name__ == "__main__":
    main()