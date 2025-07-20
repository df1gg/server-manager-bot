from db.models import Service
from db.database import async_session_maker


async def add_service(name: str, display_name: str = None):
    async with async_session_maker() as session:
        service = Service(name=name, display_name=display_name or name)
        session.add(service)
        await session.commit()


async def get_service(name: str):
    async with async_session_maker() as session:
        result = await session.execute(
            Service.__table__.select().where(Service.name == name)
        )
        return result.fetchone()


async def get_all_services():
    async with async_session_maker() as session:
        result = await session.execute(Service.__table__.select())
        return result.fetchall()


async def delete_service(name: str):
    async with async_session_maker() as session:
        await session.execute(Service.__table__.delete().where(Service.name == name))
        await session.commit()


async def update_service_status(name: str, is_running: bool):
    async with async_session_maker() as session:
        await session.execute(
            Service.__table__.update()
            .where(Service.name == name)
            .values(is_running=is_running)
        )
        await session.commit()
