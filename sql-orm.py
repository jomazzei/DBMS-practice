from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()


class Artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key = True)
    name = Column(String)

class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key = True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.artist_id"))

class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    media_type = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)
    

Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

artists = session.query(Artist)
for artist in artists:
    print(artist.artist_id, artist.name, sep=" | ")