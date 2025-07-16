from .handlers import start, status
from .middlewares import access_control


def setup_middleware(dp):
    dp.message.middleware(access_control.AccessControlMiddleware())
    dp.callback_query.middleware(access_control.AccessControlMiddleware())


def setup_routers(dp):
    dp.include_router(start.router)
    dp.include_router(status.router)
