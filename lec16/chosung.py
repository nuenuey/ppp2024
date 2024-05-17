def get_chosung(text):
    chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    chosung = []

    for gulja in text:  # 가에서 얼마나 떨어져있는지 (몇번째 줄 몇번째 칸)계산하는 , 유니코드 588개
        # print(gulja, ord(gulja) -ord('가'))//588, (ord(gulja)- ord('가'))%588))
        chosung.append(chosung_list[(ord(gulja) - ord('가')) // 588])
        return chosung


def main():
    hidden_answer = "프원실"

    problem = get_chosung(hidden_answer)  # ㅍㅇㅅ
    print(f"문제입니다.주어진 초성은 '{''.join(problem)}'입니다")

    answer= input("답은=>?")
    if answer == hidden_answer:
       print("정답입니다")
    else:
       print("틀렸습니다")


if __name__ == "__main__":
    main()