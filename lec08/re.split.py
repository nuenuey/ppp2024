


def main():
    input_text = "5, 10, 3, 4, 7"
    tokens = input_text.split(",") #자르는 함수 ['5', ' 10', ' 3', ' 4', ' 7’]
    print(tokens)
#   print(sum(tokens)) 에러가 뜸
    results = []
    for token in tokens:
        results.append(int(token))
    print(results)
    print(sum(results))

    results2= [int(x) for x in input_text.split(",")]
if __name__ == "__main__":
    main()