from typing import List
from src.models.sqlite.entities.people import PeopleTable
from sqlalchemy.orm.exc import NoResultFound


class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self._db_connection = db_connection

    def list_people(self) -> List[PeopleTable]:
        with self._db_connection as database:
            try:
                people = database.session.query(PeopleTable).all()
                return people
            except NoResultFound:
                return []
