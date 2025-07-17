from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def service_control_kb(service_name: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="▶️ Start", callback_data=f"start:{service_name}"
                ),
                InlineKeyboardButton(
                    text="🔃 Restart", callback_data=f"restart:{service_name}"
                ),
                InlineKeyboardButton(
                    text="⏹  Stop", callback_data=f"stop:{service_name}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔄 Refresh", callback_data=f"refresh_service:{service_name}"
                ),
                InlineKeyboardButton(
                    text="🗑 Delete", callback_data=f"delete:{service_name}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Back to menu", callback_data=f"back_to_service_list"
                ),
            ],
        ]
    )
