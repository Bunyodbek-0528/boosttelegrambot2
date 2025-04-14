import aiogram.types
from aiogram import Bot,Dispatcher,Router,F
from asyncio import run
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.types import CallbackQuery
import sys
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from os import getenv
load_dotenv()
tokenim=getenv("BOT_TOKEN")

def get_inline()-> InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="O'zbekiston",callback_data="uz")
    inline.button(text="Qozog'iston",callback_data="kz")
    inline.button(text="Qizg'iz", callback_data="kg")
    inline.button(text="Turkmaniston", callback_data="tm")
    inline.button(text="Rossiya", callback_data="ru")
    inline.adjust(1)
    return inline.as_markup()


def tozalash()-> InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="ha", callback_data="ha")
    inline.button(text="yoq", callback_data="yoq")
    return inline.as_markup()


dd=Dispatcher()
#tokenim="7402256865:AAG3_EALH171FrsfYQjNdlqUngxMa7yoBfQ"
global tanlov

my_router=Router()
dd.include_router(my_router)


@my_router.message(Command('start'))
#router yordamida xabar berish
async def start_bosilganda(m:Message):
    await m.answer("Xush kelibsiz👋🏻")
    await m.answer("Quyidagi davlatlardan birini tanlang? ",reply_markup=get_inline())


@my_router.callback_query(F.data=="uz")
async def uz_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan O'zbekistonni tanlaysizmi ?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("Siz O'zbekistonni tanladingiz")
    global tanlov
    tanlov="O'zbekiston"


@my_router.callback_query(F.data == "kz")
async def kz_tanlanganda(call: CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Qozog'istonni tanlaysizmi ?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("Siz Qozog'istonni tanladingiz")
    global tanlov
    tanlov="Qozog'iston"


@my_router.callback_query(F.data == "kg")
async def kg_tanlanganda(call: CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Qirg'izni tanlaysizmi ?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("Siz Qirg'izni tanladingiz")
    global tanlov
    tanlov="Qirg'iz"


@my_router.callback_query(F.data == "tm")
async def tm_tanlanganda(call: CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Turkmanistonni tanlaysizmi ?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("Siz Turkmanistonni tanladingiz")
    global tanlov
    tanlov="Turkmaniston"


@my_router.callback_query(F.data == "ru")
async def ru_tanlanganda(call: CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Rossiyani tanlaysizmi ?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("Siz Rossiyani tanladingiz")
    global tanlov
    tanlov="Rossiya"


@my_router.callback_query(F.data=="ha")
async def ha_tanlanganda(call:CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.delete()
    global tanlov
    matn=str(tanlov)
    await call.message.answer(f"{matn} ni tanladingiz")
    r=getenv("ADMINS")
    for i in r:
        await call.bot.send_message(chat_id=i,text=f"{call.from_user.full_name}  {matn} ni tanladi")
    #await call.bot.send_message(chat_id=getenv("MY_ID"),text="tanlov qilindi")

@my_router.callback_query(F.data=="yoq")
async def yoq_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Quyidagi davlatlardan birini tanlang")
    await call.message.edit_reply_markup(reply_markup=get_inline())

@my_router.message()
async def xabar_kelganda(m:Message,bot):
    await m.copy_to(chat_id=m.from_user.id) #kim xabar yozsa shunga yozadi
    await m.copy_to(chat_id="5727903783")      #shu id ga xabar qaytaradi
    await m.edit_text(m.text.upper())
    await bot.send_message(chat_id=getenv("MY_ID"),text=f"{m.from_user.full_name} sizning botingizga  '{m.text}' deb yozdi")

async def bot_ishlaganda(bot:Bot):
    await bot.send_message(chat_id=getenv("MY_ID"),text="Bot ishladi✅")


async def bot_toxtaganda(bot:Bot):
    await bot.send_message(chat_id=getenv("MY_ID"),text="Bot to'xtadi ❌")


async def main():
    botim=Bot(token=tokenim,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    #dd.startup.register(bot_ishlaganda)
    dd.startup.register(bot_toxtaganda)
    await dd.start_polling(botim)
if __name__=="__main__":
 logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s ",handlers=[logging.FileHandler("bot.log"),logging.StreamHandler(sys.stdout)])#,stream=sys.stdout)
 run(main())



