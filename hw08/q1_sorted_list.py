def text2list(input_text):
    tokens = input_text.split(" ") #리스트 자르는 함수 ['5', ' 10', ' 3', ' 4', ' 7’]

    text2list=[] #리스트만들기
        
    for token in tokens:
        text2list.append(int(token)) # 리스트에 숫자넣기

    return text2list

def median(nums):

    nums.sort()
    n=len(nums)
    if n%2 ==0: #짝수(나머지=0)
        mid_left = n // 2 #몫을 나누기2 ex) 4>>2
        mid_right = mid_left + 1
        median_value = (nums[mid_left] + nums[mid_right]) / 2
    else:
         median_value = nums[n // 2] #홀수 9>>4.5
    return median_value

def average(nums):

    n=len(nums)
    total= sum(nums)
    return total/ n

def main():
    
    input_text = "5 10 3 4 7"
    nums = text2list(input_text) #리스트
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print(f"최솟값은 {min(nums)}")
    print(f"최댓값은 {max(nums)}")

if __name__ == "__main__":
    main()

