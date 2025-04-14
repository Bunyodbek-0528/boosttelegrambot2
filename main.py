from aiogram import Bot,Dispatcher
from asyncio import run
from aiogram.filters import CommandStart #Command
from aiogram.types import Message

t="7402256865:AAFuKtaCSVgy28M7l4vslfEN66o9-I5uWGs"
dp=Dispatcher()

#dekorat bilan Dispetcherga vazifalar yaratish
#@dp.message(CommandStart)   #(Command("start"))     #xabar ko'rinishida
# javob beradigan dekoratr Command("start") start buyrugi
async def start_bosilganda(x:Message,bot:Bot):
    await x.answer(f"Xush kelibsiz")
    await bot.send_message("5727903783","xush kelmabsiz😆😁")


async def main():
    bot=Bot(token=t)
    dp.message.register(start_bosilganda,CommandStart)
    await dp.start_polling(bot)
run(main())


