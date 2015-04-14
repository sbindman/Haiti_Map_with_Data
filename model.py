from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, Unicode
from geojson import Feature, Point, FeatureCollection
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref
import os


# Creates engine,session, echo prints sqla calls, commits are not auto
engine = create_engine("sqlite:///poi.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

# Base is a class in sqla that my tables are instantiated from
Base = declarative_base()
Base.query = session.query_property()


# Class declarations

# The POI class includes all of the locations that will be added to the map

class POI(Base):
    __tablename__ = "points_of_interest"

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    lat = Column(Float(50))
    lng = Column(Float(50))
    info = Column(String(500), nullable=True)

    def __repr__(self):
        return "<title = %s>" % (self.title)


def getPOIs():
    """ Queries all points of interest in db and creates GeoJson """

    points_of_interest = session.query(POI).all()

    coordinates = []

    for poi in points_of_interest:

        title = poi.title
        lng = poi.lng
        lat = poi.lat
        info = poi.info

        # Functions from the geojson library create geoson objects with the
        # details specified
        my_point = Feature(geometry=Point((lng, lat)), properties={
                             "title": title, "longitude": lng, "lat": lat, "info": info, "marker-color": "#D95929"})
        coordinates.append(my_point)

    # We return all this geojson as a feature collection
    new_coords = FeatureCollection(coordinates)
    return new_coords


def main():
    pass


if __name__ == "__main__":
    main()
