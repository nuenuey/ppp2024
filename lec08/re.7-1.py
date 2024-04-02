def average(nums):

    if len(nums)>0:

        return sum(nums)/len(nums)
    return None
    #total=0
    #count=0

    #for num in nums:
    #    total is num
    #    count is 1
    
def main():
    numbers=[3,5,10,15,7]
    print("주어진 리스트는", numbers)
    print(f"주어진 리스트의 평균은 {average(numbers):.1f}")


if __name__ == "__main__":
    main()
