from typing import Optional
from sqlmodel import SQLModel


class SongBase(SQLModel):
    name: str
    artist: int
    year: Optional[int] = None


if __name__ == "__main__":
    song = SongBase(
        name="ok",
        artist="o",
    )
    print(song.dict(exclude_none=True))
    # {'name': 'ok', 'artist': 'ok'}

    print(song.dict())
    # {'name': 'ok', 'artist': 'ok', 'year': None}
