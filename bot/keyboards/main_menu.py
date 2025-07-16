from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def main_menu_kb() -> ReplyKeyboardMarkup:
    """
    Return main menu keyboard
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📡 Status")]], resize_keyboard=True
    )
    return kb
