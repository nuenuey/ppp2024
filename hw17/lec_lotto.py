import random
def get_lotto():
    results = []

    while len(results) < 6:  # 결과가 6개가 될 때까지 반복
        num = random.randint(1, 45)
        if num not in results:
            results.append(num)

    return sorted(results)
    # return [3,5,8,10, 12, 15]


def main():
    count = int(input("로또!!!! 몇 번을 추출할까요?"))

    for i in range(count):
        lotto_nums = get_lotto()
        print(f"{i + 1} : {lotto_nums}")


if __name__ == "__main__":
    main()