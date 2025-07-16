from aiogram.exceptions import TelegramBadRequest


async def safe_edit(message, text, markup=None):
    current_text = message.text or message.caption or ""
    current_murkup = message.reply_markup

    same_text = current_text == text

    def kb_equal(kb1, kb2):
        if not kb1 and not kb2:
            return True
        if not kb1 or not kb2:
            return False
        return kb1.inline_keyboard == kb2.inline_keyboard

    same_markup = kb_equal(current_murkup, markup)

    if same_text and same_markup:
        return

    try:
        await message.edit_text(text, reply_markup=markup)
    except TelegramBadRequest as e:
        if "message is not modified" in str(e):
            return
        raise
