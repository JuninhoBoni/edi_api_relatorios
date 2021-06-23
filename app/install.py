import os
from db_sqlite.conn_sqlite import ConnSqlite
from sqlite3 import Error
from passlib.context import CryptContext
from pydantic import BaseSettings

class Settings(BaseSettings):
    secret: str  # autmatically taken from environement variable

def create_table_users():
    try:
        cursor.execute(f"""
        CREATE TABLE {table} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username        VARCHAR(10) NOT NULL UNIQUE,
                full_name       VARCHAR(100) NOT NULL,
                email           TEXT NOT NULL,
                access_level    INTEGER NOT NULL,
                hashed_password TEXT NOT NULL,
                disabled        BOOLEAN  NOT NULL,
                create_date     DATE NOT NULL
        );
        """)

        print(f"TABLE {table} CREATE".upper())
    except Error as e:
        print(str(e).upper())


def insert_table_users():

    admin = {
        "username": "admin",
        "full_name": "admin",
        "email": "admim@admin.com",
        "access_level": 0,
        "hashed_password": pwd_context,
        "disabled": False
    }

    try:
        cursor.execute(f"""
        INSERT INTO {table} (username, full_name, email, access_level, hashed_password, disabled, create_date)
        VALUES (
            '{admin["username"]}',
            '{admin["full_name"]}',
            '{admin["email"]}',
            {admin["access_level"]},
            '{admin["hashed_password"]}',
            {admin["disabled"]},
            date()
        )
        """)

        conn.commit()

        print(f"RECORD INSERTED SUCCESSFULLY IN {table}".upper())

    except Error as e:
        print(str(e).upper())


if __name__ == "__main__":
    if os.path.exists(".env"):
        print(".env file already exists. Exiting...")
    else:
        with open(".env", "w") as f:
            f.write(f"SECRET={os.urandom(24).hex()}")
    DEFAULT_SETTINGS = Settings(_env_file=".env")
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto").hash('asd')
    conn_sqlite = ConnSqlite()
    conn, cursor = conn_sqlite.conn()
    table = "users"
    create_table_users()
    insert_table_users()
    conn.close()
