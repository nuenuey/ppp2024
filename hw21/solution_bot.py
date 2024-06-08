import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


##
#
token = "7379559766:AAEamF_pPuuxxXDXA4uFk-QPkvV5fny3-3c"
chat_id = "7281181367"
# bot = telegram.Bot(token=token)
# updates = bot.getUpdates()
# for u in updates:
#     print(u.message)

bot = telegram.Bot(token)
bot.sendMessage(chat_id=chat_id, text="테스트 중입니다.")

# updater
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

pepero_calories = {
    "오리지널 빼빼로": 270,
    "아몬드 빼빼로": 205,
    "누드 빼빼로": 255,
    "초코 쿠키 빼빼로": 190,
    "크런키 빼빼로": 205
}

# bongji_snacks_calories = {
#     "빈츠": 45,
#     "오레오": 240,  # 1봉지 기준
#     "칙촉": 76,
#
#     "초코파이": 160,
#     "몽쉘": 176
# }
# 사용자가 보낸 메세지를 읽어들이고, 답장을 보내줍니다.
# 아래 함수만 입맛에 맞게 수정해주면 됩니다. 다른 것은 건들 필요없어요.
def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "빼빼로":  # 갈까라는 문자가 있을떄
        bot.send_message(chat_id=chat_id, text="빼빼로 종류를 작성해주세요. ex) 오리지널 빼빼로, 누드 빼빼로")  # 답장 보내기
    elif user_text in pepero_calories:
        bot.send_message(chat_id=chat_id, text=f"{user_text}: {pepero_calories[user_text]}칼로리(Kcal)")
    elif user_text == "가장 낮은 칼로리의 빼빼로가 뭐야?":
        lowest_calorie_pepero = min(pepero_calories, key=pepero_calories.get)
        lowest_calorie_value = pepero_calories[lowest_calorie_pepero]
        bot.send_message(chat_id=chat_id,
                                 text=f"가장 낮은 칼로리의 빼빼로는 {lowest_calorie_pepero}로, {lowest_calorie_value}칼로리(Kcal) 입니다.")

    elif user_text == "포카칩":
        bot.send_message(chat_id=chat_id, text="포카칩 : 120칼로리(Kcal) (100g)")
    elif user_text == "빈츠":  # 살까라는 문자가 있을떄
        bot.send_message(chat_id=chat_id, text="빈츠 : 45칼로리(Kcal) (1 봉지)")  # 답장 보내기.

    elif user_text == "오레오":
        bot.send_message(chat_id=chat_id, text="오레오 : 240칼로리(Kcal) (1봉지 = 5개)")
    elif user_text == "칙촉":
        bot.send_message(chat_id=chat_id, text="칙촉 : 76칼로리(Kcal) (1 봉지)")

    elif user_text == "초코파이":
        bot.send_message(chat_id=chat_id, text="초코파이 : 160칼로리(Kcal) (1 봉지)")
    elif user_text == "몽쉘":
        bot.send_message(chat_id=chat_id, text="몽쉘 : 176칼로리(Kcal) (1 봉지)")
    # elif user_text in "빈츠":
    #     bot.send_message(chat_id=chat_id, text="몇 봉지를 드실 건가요?")
    #     #bot.send_message(chat_id=chat_id, text=f"{user_text} : {bongji_snacks_calories[user_text]}칼로리(Kcal)")
    # elif user_text in "칙촉":
    #     bot.send_message(chat_id=chat_id, text="몇 봉지를 드실 건가요?")
    # elif user_text in "초코파이":
    #     bot.send_message(chat_id=chat_id, text="몇 봉지를 드실 건가요?")
    # elif user_text in "몽쉘":
    #     bot.send_message(chat_id=chat_id, text="몇 봉지를 드실 건가요?")
    # elif user_text in bongji_snacks_calories:
    #     bot.send_message(chat_id=chat_id, text=f"{user_text}*{bongji_snacks_calories} 칼로리 입니다")


    else:
        bot.send_message(chat_id=chat_id, text="죄송합니다, 해당 과자의 칼로리 정보를 찾을 수 없습니다.")


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)


