from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from utils.logging_decorator import log_request


router = Router()


@router.callback_query(F.data == "cancel")
@log_request
async def cancel_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await state.clear()

    await callback.message.answer("🙆🏽 You cancelled the action!")
