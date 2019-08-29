import pymysql


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB():
    print("Reading BLOB data from python_employee table")

    try:
        connection = pymysql.connect(host='localhost',
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
            if not row[4]:
                continue
            image = row[4]

            print("Storing employee image and bio-data on disk \n")
            write_file(image, "C:/Users/Bakir/Desktop/python/timur.jpg")

    except pymysql.Error as error:
        connection.rollback()
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


readBLOB()
