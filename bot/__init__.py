from .handlers import start


def setup_routers(dp):
    dp.include_router(start.router)
