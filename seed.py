import model
import csv


def load_points(session):
    ''' Opens csv file and reads it into database '''

    poi_file = open('seed_data_simple.csv')

    for line in poi_file:
        data = line.split(',')

        # establishes connection between item and it's place in the db
        location = model.POI(title=data[0], lng=data[1], lat=data[2], info=data[3])
        session.add(location)
    session.commit()



def main(session):
    load_points(session)

if __name__ == "__main__":

    main(model.session)
