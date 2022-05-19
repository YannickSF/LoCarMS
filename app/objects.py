

class Car:

    def __init__(self, **kwargs):
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.id_owner = kwargs['id_owner'] if 'id_owner' in kwargs else None
        self.date_creation = kwargs['date_creation'] if 'date_creation' in kwargs else None
        self.model = kwargs['model'] if 'model' in kwargs else None
        self.registration = kwargs['registration'] if 'registration' in kwargs else None

    def __repr__(self):
        return {
            'id': self.id,
            'id_owner': self.id_owner,
            'date_creation': self.date_creation,
            'model': self.model,
            'registration': self.registration,
        }

    def __str__(self):
        return self.__repr__().__str__()


class Announce:

    def __init__(self, **kwargs):
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.id_car = kwargs['id_car'] if 'id_car' in kwargs else None
        self.available_period = kwargs['available_period'] if 'available_period' in kwargs else None
        self.price_h = kwargs['price_h'] if 'price_h' in kwargs else None
        self.price_j = kwargs['price_j'] if 'price_j' in kwargs else None
        self.status = kwargs['status'] if 'status' in kwargs else None

    def __repr__(self):
        return {
            'id': self.id,
            'id_car': self.id_car,
            'available_period': self.available_period,
            'price_h': self.price_h,
            'price_j': self.price_j,
            'status': self.status,
        }

    def __str__(self):
        return self.__repr__().__str__()


class Location:

    def __init__(self, **kwargs):
        self.id = kwargs['id'] if 'id' in kwargs else None
        self.id_owner = kwargs['id_owner'] if 'id_owner' in kwargs else None
        self.id_tenant = kwargs['id_tenant'] if 'id_tenant' in kwargs else None
        self.start_date_time = kwargs['start_date_time'] if 'start_date_time' in kwargs else None
        self.end_date_time = kwargs['end_date_time'] if 'end_date_time' in kwargs else None
        self.total_price = kwargs['total_price'] if 'total_price' in kwargs else None
        self.status = kwargs['status'] if 'status' in kwargs else None

    def __repr__(self):
        return {
            'id': self.id,
            'id_owner': self.id_owner,
            'id_tenant': self.id_tenant,
            'start_date_time': self.start_date_time,
            'end_date_time': self.end_date_time,
            'total_price': self.total_price,
            'status': self.status,
        }

    def __str__(self):
        return self.__repr__().__str__()
