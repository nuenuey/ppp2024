import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


## 내가 저장한 명언 보여주기
#고민을 입력하면 00을 하세요
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


# 사용자가 보낸 메세지를 읽어들이고, 답장을 보내줍니다.
# 아래 함수만 입맛에 맞게 수정해주면 됩니다. 다른 것은 건들 필요없어요.
def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "갈까":  # 사용자가 보낸 메세지가 "안녕"이면?
        bot.send_message(chat_id=chat_id, text="어 그래 안녕")  # 답장 보내기
    elif user_text == "뭐해":  # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=chat_id, text="그냥 있어")  # 답장 보내기


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
