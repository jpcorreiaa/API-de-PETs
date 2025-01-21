from typing import List  # python 3.8
from src.models.sqlite.entities.pets import PetsTable
from sqlalchemy.orm.exc import NoResultFound


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self._db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self._db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self._db_connection as database:
            try:
                (
                    database.session.query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
