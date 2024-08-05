from typing import Optional

from flask import current_app

from app.database import database as db, Pallet


class PalletRepository:
    last_error: Optional[Exception] = None

    @staticmethod
    def read_by_table_id(table_id: int) -> Optional[list[Pallet]]:
        try:
            database = db.get_database()
            pallet = database.execute('SELECT * FROM pallet WHERE tables_id = ?', (table_id,)).fetchall()
            print(pallet)
            pallet = list(map(lambda plt: Pallet(*plt), pallet))

            return pallet
        except Exception as e:
            PalletRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_table_id_and_surface(table_id: int, surface: int) -> Optional[list[Pallet]]:
        try:
            database = db.get_database()
            pallet = database.execute('SELECT * FROM pallet WHERE tables_id = ? AND surface_type = ? ',
                                      (table_id, surface, )).fetchall()
            print(pallet)
            pallet = list(map(lambda plt: Pallet(*plt), pallet))

            return pallet
        except Exception as e:
            PalletRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_by_id(pallet_id: int) -> Optional[Pallet]:
        try:
            database = db.get_database()
            pallet_row = database.execute('SELECT * FROM pallet WHERE id = ?', (pallet_id,)).fetchone()
            if pallet_row:
                pallet = Pallet(*pallet_row)
                return pallet
            return None
        except Exception as e:
            PalletRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def read_all() -> Optional[list[Pallet]]:
        try:
            database = db.get_database()
            pallet = database.execute('SELECT * FROM pallet').fetchall()
            print(pallet)
            pallet = list(map(lambda plt: Pallet(*plt), pallet))

            return pallet
        except Exception as e:
            PalletRepository.last_error = e
            current_app.logger.error(e)
            return None

    @staticmethod
    def insert(hex_color: str, table_id: int, surface: int) -> bool:
        try:
            database = db.get_database()
            database.execute('INSERT INTO pallet (tables_id, surface_type, hex_color) VALUES (?, ?)',
                             (table_id, surface, hex_color,))
            database.commit()
            return True
        except Exception as e:
            PalletRepository.last_error = e
            current_app.logger.error(e)
            return False
