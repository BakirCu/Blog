import mysql.connector


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(title, post, image_path):
    print("Inserting BLOB into python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='biblioteka1',
                                             user='root',
                                             password='password')

        cursor = connection.cursor()

        sql_insert_blob_query = """ INSERT INTO blog.posts(title, post, image)
                        VALUES (%s, %s, %s);"""

        empPicture = convertToBinaryData(image_path)

        # Convert data into tuple format
        insert_blob_tuple = (title, post, empPicture)

        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        connection.rollback()
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        # closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


insertBLOB('milica', 'jsjsjsjjs',
           "C:/Users/Bakir/Desktop/python/Flask blog/static/download.jpg")
