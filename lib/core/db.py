from mysql import connector
from lib.utils.config import config



class dbEngine:

  table_create_stmt = "CREATE TABLE `cities`.`city_trend` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(120) NOT NULL , `lon` VARCHAR(14) NOT NULL , `lat` VARCHAR(14) NOT NULL , `point` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"
  mydb = None
  resu = None
  def __init__(self) -> None:
    self.mydb = connector.connect(
      host = config.MYSQL_HOST,
      user = config.MYSQL_USER,
      password = config.MYSQL_PASS,
      database = config.MYSQL_DB
    )


  def exeuteQuery(self, query:str , value):
      mycursor = self.mydb.cursor()
      mycursor.execute(query, value)
      self.resu = mycursor.fetchall()
      self.mydb.commit()

  def initiateTable(self):
      self.exeuteQuery(self.table_create_stmt,None)