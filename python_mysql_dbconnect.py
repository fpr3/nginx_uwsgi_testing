import MySQLdb

def connect():
    """ Connect to MySQL database """

    db_config = "../private/config.ini"
    conn = None

    try:
        print('Connecting to MySQL database...')
        conn = MySQLdb.Connect(read_default_file=db_config)

        print('connection established.')

    except MySQLdb.Error as error:
        print("Connection FAILED:\n  "+ str(error))

    finally:
        if conn != None:
          conn.close()
        print('Connection closed.')


if __name__ == '__main__':
    connect()
