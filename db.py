import mysql.connector
from trip import Trip
from configurations_service import ConfigurationsService

class TripisDb:

    cursor = None
    tripis_db = None
    configs = None


    def __init__(self, configs: ConfigurationsService):
        self.configs = configs
        try:
            self.tripis_db = mysql.connector.connect(
              host="localhost",
              user=self.configs.db_user(),
              password=self.configs.db_pass(),
              database=self.configs.db_name())
        except mysql.connector.errors.DatabaseError:
            print("Failed to connect to DB. User=%s Pass=%s, Db=%s" % (self.configs.db_user(), self.configs.db_pass(), self.configs.db_name()))
            exit(1)

        self.cursor = self.tripis_db.cursor()
        self.create_tables()
        self.tripis_db.commit()
        self.cursor.close()
        self.tripis_db.close()
        self.db_name = self.configs.db_name()

    def get_connection(self):
        """
        Makes a connection to database and returns is
        After use, close the connection
        """
        return mysql.connector.connect(
          host="localhost",
          user=self.configs.db_user(),
          password=self.configs.db_pass(),
          database=self.configs.db_name())
        
    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS trips (id INT AUTO_INCREMENT PRIMARY KEY, \
                city TEXT, \
                country TEXT, \
                userId TEXT, \
                participants TEXT)")


    def run_sql_command(self, command):
        cnx = self.get_connection()
        cursor = cnx.cursor()
        cursor.execute( command )
        records = cursor.fetchall()
        cursor.close()
        cnx.close()
        return records


    def get_trips(self):
        sql = "select id, city, country, userId, participants from trips;"
        records = self.run_sql_command( sql )
        return records


    def get_trip(self, trip_id: str):
        sql = "select id, city, country, userId, participants from trips where id=" + trip_id
        records = self.run_sql_command( sql )
        return records


