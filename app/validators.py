
from jsonschema import ValidationError, validate


car_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "id_owner": {"type": "string"},
        "date_creation": {"type": "string"},
        "model": {"type": "string"},
        "registration": {"type": "string"},
    }
}


def _car_validator(object_to_update):
    try:
        validate(instance=object_to_update.__json__(), schema=car_schema)
        return 200
    except ValidationError as ve:
        return ve.message


announce_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "id_car": {"type": "string"},
        "available_period": {"type": "string"},
        "price_h": {"type": "string"},
        "price_j": {"type": "string"},
        "status": {"type": "string"},
    }
}


def _announce_validator(object_to_update):
    try:
        validate(instance=object_to_update.__json__(), schema=announce_schema)
        return 200
    except ValidationError as ve:
        return ve.message


location_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "id_owner": {"type": "string"},
        "id_tenant": {"type": "string"},
        "start_date_time": {"type": "string"},
        "end_date_time": {"type": "string"},
        "total_price": {"type": "string"},
        "status": {"type": "string"},
    }
}


def _location_validator(object_to_update):
    try:
        validate(instance=object_to_update.__json__(), schema=location_schema)
        return 200
    except ValidationError as ve:
        return ve.message
