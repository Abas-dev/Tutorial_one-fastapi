from pydantic import BaseModel,validator
from datetime import date
from enum import Enum 
from sqlmodel import SQLModel, Field, Relationship

class GenreURLChoices(Enum): 
    ROCK = 'rock'
    METAL = 'metal'
    REGGAE = 'reggae'
    ELECTRONIC = 'electronic'

class GenreChoices(Enum): 
    ROCK = 'Rock'
    METAL = 'Metal'
    REGGAE = 'Reggae'
    ELECTRONIC = 'Electronic'

class AlbumsBase(SQLModel): 
    title: str 
    release_date: date
    band_id: int | None = Field(foreign_key="band.id")

class Album(AlbumsBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band: "Band" = Relationship(back_populates="albums")

class BandBase(SQLModel):
    name: str 
    genre: GenreChoices

class BandCreate(BandBase):
    albums: list[AlbumsBase] | None = None 

    @validator('genre',pre=True)
    def title_case_genre(cls, value):
        return value.title()

class Band(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    albums: list[Album] = Relationship(back_populates="band")
    date_formed: date | None