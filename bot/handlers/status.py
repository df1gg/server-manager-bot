from aiogram import F, Router, types

from bot import text


router = Router()


@router.message(F.text == "📡 Status")
async def get_server_status_handler(message: types.Message):
    await message.answer(text.SERVER_STATUS)
