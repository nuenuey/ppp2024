import random
def get_chosung(text):
    chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    chosung = []

    for gulja in text:  # 가에서 얼마나 떨어져있는지 (몇번째 줄 몇번째 칸)계산하는 , 유니코드 588개
        # print(gulja, ord(gulja) -ord('가'))//588, (ord(gulja)- ord('가'))%588))
        chosung.append(chosung_list[(ord(gulja) - ord('가')) // 588])
    return chosung


def main():
    hidden_answer_list = ["빅파이","초코파이","화이트하임","초코송이","새우깡","감자깡","먹태깡","꼬북칩","빈츠","고래밥"]
    choicelist =random.choice(hidden_answer_list)
    #print(choicelist)
    problem = get_chosung(choicelist)  # ㅍㅇㅅ
    print(f"과자 이름 맞추기 게임입니다!! 주어진 초성은 '{''.join(problem)}'입니다. 정답을 입력해주세요.")
    while True:
        answer= input("답은=>?")
        if answer == choicelist:
            print("정답입니다")
            break
        else:
            print("틀렸습니다. 다시시도하시오.")


if __name__ == "__main__":
    main()