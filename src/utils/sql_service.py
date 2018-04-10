import sqlite3 as sql
import sys

from src.config.config_service import configuration

database_path = configuration['configuration']['sqlite3']['database-path']


def run_query(query):
  try:
    con = sql.connect(database_path + configuration['configuration']['sqlite3']['string-translator'])
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute(query)

    data = cur.fetchall()
    con.commit()

    return data

  except sql.Error as e:
    print("Error %s:" % e.args[0])

  finally:
    if con:
      con.close()


def getVersion():
  return run_query('SELECT SQLITE_VERSION();')
