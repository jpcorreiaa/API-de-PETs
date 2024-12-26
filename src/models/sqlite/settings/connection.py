from sqlalchemy import create_engine


class DBCConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storege.db"
        self.__engine = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine


db_connection_handler = DBCConnectionHandler()
