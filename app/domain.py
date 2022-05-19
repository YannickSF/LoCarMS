
import uuid
import datetime
from app.nosql import Table, Query
from app.objects import Car, Announce, Location
from app.validators import _car_validator, _announce_validator, _location_validator


class Domain:
    def __init__(self):
        # validate object
        self._cars_db = Table('cars')
        self._announce_db = Table('announces')
        self._location_db = Table('locations')

    # CAR
    def create_car(self, **obj_to_create):
        new_car = Car(**obj_to_create)
        new_car.id = uuid.uuid4().__str__()
        new_car.date_creation = datetime.datetime.now().strftime("%Y-%m-%d")

        self._cars_db.insert(new_car.__repr__())

    def read_car(self):
        return self._cars_db.all()

    def read_car_by_id(self, id):
        q = Query()
        return self._cars_db.search(q.id == id)

    def update_car(self, id,  **obj_to_update):
        q = Query()
        car_found = self._cars_db.search(q.id == id)
        if len(car_found) == 0:
            return 'No cars found.'

        upt_car = Car(**obj_to_update)
        can = _car_validator(upt_car)
        if can == 200:
            self._cars_db.update(upt_car.__repr__(), q.id == id)
        return can

    def delete_car(self, id):
        q = Query()
        self._cars_db.remove(q.id == id)

    # ANNOUNCE
    def create_announce(self, **obj_to_create):
        new_announce = Announce(**obj_to_create)
        new_announce.id = uuid.uuid4().__str__()
        new_announce.date_creation = datetime.datetime.now().strftime("%Y-%m-%d")

        self._announce_db.insert(new_announce.__repr__())

    def read_announce(self):
        return self._announce_db.all()

    def read_announce_by_id(self, id):
        q = Query()
        return self._announce_db.search(q.id == id)

    def update_announce(self, id,  **obj_to_update):
        q = Query()
        announce_found = self._announce_db.search(q.id == id)
        if len(announce_found) == 0:
            return 'No announces found.'

        upt_announce = Announce(**obj_to_update)
        can = _announce_validator(upt_announce)
        if can == 200:
            self._announce_db.update(upt_announce.__repr__(), q.id == id)
        return can

    def delete_announce(self, id):
        q = Query()
        self._announce_db.remove(q.id == id)

    # LOCATION
    def create_location(self, **obj_to_create):
        new_location = Location(**obj_to_create)
        new_location.id = uuid.uuid4().__str__()
        new_location.date_creation = datetime.datetime.now().strftime("%Y-%m-%d")

        self._location_db.insert(new_location.__repr__())

    def read_location(self):
        return self._location_db.all()

    def read_location_by_id(self, id):
        q = Query()
        return self._location_db.search(q.id == id)

    def update_location(self, id,  **obj_to_update):
        q = Query()
        location_found = self._location_db.search(q.id == id)
        if len(location_found) == 0:
            return 'No locations found.'

        upt_location = Location(**obj_to_update)
        can = _location_validator(upt_location)
        if can == 200:
            self._location_db.update(upt_location.__repr__(), q.id == id)
        return can

    def delete_location(self, id):
        q = Query()
        self._location_db.remove(q.id == id)
