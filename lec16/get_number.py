def get_numbers():
    results = []
    while True:
        try:
            x = input("자연수를 입력하시오=>?")
            num = int(x)
            if num == -1:
                break
            if num <= 0:
                print(f"입력한 값은 자연수가 아닙니다.")
            else:

                results.append(num)
        except ValueError:
            print(f"입력한 {x}는 저장되지 않습니다 ")
    return results


def avg(nums):
    if len(nums) != 0:
        return sum(nums) / len(nums)
    return 0



def main():
    num_list = get_numbers()

    print(f"입력된 값은 {num_list}입니다. 총 {len(num_list)}개의 자연수가 입력되었고, 평균은 {(sum(num_list)) / len(num_list)} 입니다.")


if __name__ == "__main__":
    main()