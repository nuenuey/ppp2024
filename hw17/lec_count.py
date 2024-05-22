import time

def main():
    count = int(input("카운트다운!! 몇 초를 셀까요? "))
    #count = 5

    while True:
        print(f"{count}")

        time.sleep(1)
        count -= 1
        if count <= 0:
            break
    print()
    print("bomb!!!")


if __name__ == "__main__":
    main()