from aiogram.fsm.state import State, StatesGroup


class AddService(StatesGroup):
    waiting_for_service_name = State()
    waiting_for_display_name = State()


class DeleteService(StatesGroup):
    confirm = State()
