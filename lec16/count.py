import time



def main():
    # count = int(input())
    count = 5

    while True:
        print(f"카운트 다운 ...{count}", end="\r")

        time.sleep(1)
        count -= 1
        if count <= 0:
            break
    print()
    print("bomb!")


if __name__ == "__main__":
    main()