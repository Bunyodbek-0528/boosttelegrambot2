from aiogram.types import  ReplyKeyboardMarkup#Reply
from  aiogram.utils.keyboard import ReplyKeyboardBuilder #Reply
from aiogram.types import  InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
def get_inline()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="uz O'zbekiston",callback_data="uz")
    inline.button(text="kz Qozog'iston", callback_data="kz")
    inline.button(text="kg Qirg'iz", callback_data="kg")
    inline.button(text="tm Turmaniston", callback_data="tm")
    inline.button(text="ru Rossiya", callback_data="ru")
    inline.button(text="tjk Tojikiston", callback_data="tjk")
    inline.adjust(3)
    return  inline.as_markup()
def get_ha_yoq() -> ReplyKeyboardMarkup:
    kb=ReplyKeyboardBuilder()
    kb.button(text="Ha")
    kb.button(text="Yo'q")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
def tozalash()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Ha", callback_data="ha")
    inline.button(text="Yo'q",callback_data="yoq")
    return inline.as_markup()