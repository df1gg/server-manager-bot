from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def cancel_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel")]
        ]
    )
    return kb
