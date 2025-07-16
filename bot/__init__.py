from .handlers import start, status


def setup_routers(dp):
    dp.include_router(start.router)
    dp.include_router(status.router)
