from sqlalchemy import Boolean, Column, Integer, String
from db.base import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    display_name = Column(String, nullable=True)
    is_running = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Service(name='{self.name}', display_name='{self.display_name}')>"
