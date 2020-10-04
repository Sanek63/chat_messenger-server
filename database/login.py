import psycopg2


class Login_Database():

    def __init__(self, name):
        self.dbname = name
        self.conn = psycopg2.connect(
            host="127.0.0.1",
            database=self.dbname,
            user="postgres",
            password="postgres"
        )
        self.cursor = self.conn.cursor()
        self.check_table('users')

    def check_table(self, name_table):
        if self.is_table(name_table):
            pass
        else:
            self.cursor.execute("CREATE TABLE users(username VARCHAR(30) NOT NULL, password VARCHAR(20))")
            self.cursor.execute("INSERT INTO users VALUES('username', 'password')", ('admin', 'admin'))
            self.conn.commit()
            self.cursor.close()

    # checking for table avail
    def is_table(self, table_name):
        query = "SELECT * from information_schema.tables WHERE table_name='{}';".format(table_name)
        cur = self.conn.cursor()
        cur.execute(query)
        result = bool(cur.rowcount)

        return result
