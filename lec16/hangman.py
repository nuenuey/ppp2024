def update_shown_answer_str(shown_answer, hidden_answer, x):
    return "".join(results)

def update_shown_answer(shown_answer, hidden_answer, x):
   for i in range(len(shown_answer)):
        if shown_answer[i] == "_" and hidden_answer[i]== x:
            shown_answer[i] = x
   return shown_answer


    # for shown_text, hidden_text in zip(shown_answer, hidden_answer):
    #         if shown_text == "_":
    #             if x == hidden_text:
    #                 results.append(x)
    #             else:
    #                 results.append("_")
    #         else:
    #              results.append(shown_text)
    #
    # return "".join(results)


def main():
    hidden_answer = "apple"
    # shown_answer="_" * len(hidden_answer) #"_ _ _ _ _"
    shown_answer = ["_" for x in range(len(hidden_answer))]
    trial = 3
    while True:
        x = input(f"({''.join(shown_answer)},목숨={trial})글자를 입력하시오 =>?")
        # x = "a"
        if x in hidden_answer:
            shown_answer = update_shown_answer(shown_answer, hidden_answer, x)
        else:
            trial -= 1
        if "_" not in shown_answer:
            print("축하합니다. 정답입니다.")
            break

        if trial <= 0:
            print("정답을 맟추지 못했습니다.")
            print(f"정답은 {hidden_answer}입니다")


if __name__ == "__main__":
    main()