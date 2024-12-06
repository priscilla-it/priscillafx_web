"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from sqlmodel import Field, SQLModel


class Artists(SQLModel, table=True):
    __tablename__ = 'Artist'

    id: int | None = Field(default=None, primary_key=True)
    image_url: str
    full_name: str
    band: str
    link: str | None = None
