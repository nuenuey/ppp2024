
def average(nums):

    n=len(nums)
    total= sum(nums)
    return total/ n


def read_list_from_file(filename) :
    data=[]
    with open (filename) as f:
        lines= f.readlines() #파일내의 모든 텍스트를 읽는다
        for line in lines: #ex)8 3 5 --> ['8, 3, 5'] 읽은 모든 텍스트를 변수에 넣고  반복문 실행
                text = line.strip()  #['8', '3', '5']/ strip()양쪽 공백제거함수
                #split()은 특정 패턴에 따라 문자열을 분리하는 함수
                numbers= text.split() #분리를 다시 리스트로

            #반복문으로  꺼내서 정수형으로 바꿔주기

                int_data=[] #리스트 초기화, 정수로 바꾸기
                for num_str in numbers:
                     num_int = int(num_str)
                     int_data.append(num_int)

                
                data.extend(int_data) #기존의 리스트의 끝부분에 추가하겠다....['8', '3', '5'] 리스트가 있고, 다음 줄인 ['2', '4']가 있다고 가정하면,
                                   #append를 하게되면 ['8', '3', '5', ['2', '4']]가 되어 이중 리스트가 될 거에요. 이럴 경우에는 리스트1 + 리스트2와 같이 리스트끼리를 서로 더해주면 되겠죠?

    return data  

def median(nums):
    nums.sort()
    
    n=len(nums)
    if n%2 ==0: #짝수(나머지=0)
        mid_left = n // 2 -1 
        mid_right = n // 2
        median_value = (nums[mid_left] + nums[mid_right]) / 2
    else:
         median_value = nums[n // 2]
    return median_value

def main():
    
    nums = read_list_from_file("hw09/numbers2.txt")
    
    print("주어진 리스트는", nums)
    print(f"총 숫자의 개수는{len(nums)}")
    print(f"주어진 숫자의 평균값은 {average(nums):.1f}")
    print(f"주어진 숫자의 최댓값은 {max(nums)}")
    print(f"주어진 숫자의 최솟값은 {min(nums)}")
    print(f"중앙값은 {median(nums)}")
    
    
if __name__ == "__main__":
    main()

    