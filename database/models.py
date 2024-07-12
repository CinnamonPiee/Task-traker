from datetime import datetime
from database.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, text, String, DateTime, Integer, Boolean


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, nullable=False,
                                                    server_default=text("TIMEZONE('utc', now())"))
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False,
                                                 server_default=text("TIMEZONE('utc', now())"))

    user: Mapped["User"] = relationship("User", cascade="all, delete", back_populates="Task")
