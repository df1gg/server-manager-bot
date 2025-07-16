from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def server_status_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔄 Refresh", callback_data="refresh_server_status"
                )
            ]
        ]
    )
    return kb
