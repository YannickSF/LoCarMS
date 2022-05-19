
from app.endpoints import app


class _Setting:
    NAME = 'LoCarMS'
    HOST = '0.0.0.0'
    PORT = 5001


SETTINGS = _Setting()


if __name__ == '__main__':
    app.run(host=SETTINGS.HOST, port=SETTINGS.PORT)
