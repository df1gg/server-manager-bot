from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def service_control_kb(service_name: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="▶️ Start", callback_data=f"start_service:{service_name}"
                ),
                InlineKeyboardButton(
                    text="🔃 Restart", callback_data=f"restart_service:{service_name}"
                ),
                InlineKeyboardButton(
                    text="⏹  Stop", callback_data=f"stop_service:{service_name}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔄 Refresh", callback_data=f"refresh_service:{service_name}"
                ),
                InlineKeyboardButton(
                    text="🗑 Delete", callback_data=f"delete_service:{service_name}"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Back to menu", callback_data=f"back_to_service_list"
                ),
            ],
        ]
    )
