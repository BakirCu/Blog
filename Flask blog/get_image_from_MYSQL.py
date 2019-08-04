import mysql.connector


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB():
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='biblioteka1',
                                             user='root',
                                             password='password')

        cursor = connection.cursor()

        sql_fetch_blob_query = '''SELECT * FROM blog.posts
                                ORDER by time_post DESC
                                LIMIT %s,%s;'''

        cursor.execute(sql_fetch_blob_query, (0, 4))
        record = cursor.fetchall()
        print(record)
        for row in record:
            print("tilte = ", row[0], )
            print("post = ", row[2])
            image = row[4]

            print("Storing employee image and bio-data on disk \n")
            write_file(image, "C:/Users/Bakir/Desktop/python")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        # closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


readBLOB()
