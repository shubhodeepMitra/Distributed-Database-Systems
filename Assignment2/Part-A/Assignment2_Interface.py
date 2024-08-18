#
# Assignment2 Interface
# Author: Shubhodeep Mitra
# email:  smitra27@asu.edu
#

import threading
import psycopg2
import os
import sys

# Do not close the connection inside this file i.e. do not perform openConnection.close()

def parallelJoin (pointsTable, rectsTable, outputTable, outputPath, openConnection):
    #Implement ParallelJoin Here.
    #pass # Remove this once you are done with implementation

    cur = openConnection.cursor()

    # Dropping existing tables with the same name
    tableNames = ["rectangle1", "rectangle2", "rectangle3", "rectangle4", "point1", "point2", "point3", "point4", outputTable]
    for tableName in tableNames:
        query = "DROP TABLE IF EXISTS " + tableName
        cur.execute(query)
    
    # Fragmenting Point Table and Rectangle Table based on Longitude Value 1 (longVal1), and Longitude Value 2 (longVal2)
    def createRectanagleAndPointsFragTables(reactangleName, pointName, longVal1, longVal2):
        query = "SELECT * INTO " + reactangleName + " FROM " + rectsTable + " WHERE ((longitude1>=" + longVal1 +" and longitude1<" + longVal2 +") or (longitude2>=" + longVal1 + " and longitude2<" + longVal2 + ") or (" + longVal2 + ">=longitude1 and " + longVal2 + "<longitude2))"
        cur.execute(query)
        query = "SELECT * INTO " + pointName + " FROM " + pointsTable + " WHERE (longitude>=" + longVal1 + " AND longitude<" + longVal2 + ")"
        cur.execute(query)

    #Fragementing by sorting the longitude of points in ascending order, followed by choosing interval as 2500th, 5000th, 7500th point for horizontal fragementaion
    createRectanagleAndPointsFragTables("rectangle1", "point1", "-75.000000", "-73.991447")
    createRectanagleAndPointsFragTables("rectangle2", "point2", "-73.991447", "-73.981682")
    createRectanagleAndPointsFragTables("rectangle3", "point3", "-73.981682", "-73.967983")
    createRectanagleAndPointsFragTables("rectangle4", "point4", "-73.967983", "-71.000000")

    # Target function for the threads to perform spatial joins based on the points which are inside a rectangle
    def fragmentation(fragTableName, pointName, rectangleName):
        cur = openConnection.cursor()

        query = "DROP TABLE IF EXISTS " + fragTableName
        cur.execute(query)

        query = "SELECT longitude1, latitude1, longitude2, latitude2, COUNT(*) AS POINTS_COUNT INTO " + fragTableName + " FROM " + rectangleName + " JOIN " + pointName + " ON ST_Contains( " + rectangleName + ".geom, " + pointName + ".geom) GROUP BY longitude1, latitude1, longitude2, latitude2 ORDER BY COUNT(*)"
        cur.execute(query)

    thread1 = threading.Thread(target=fragmentation, args=('fragmentation1', 'point1', 'rectangle1'))
    thread1.start()

    thread2 = threading.Thread(target=fragmentation, args=('fragmentation2', 'point2', 'rectangle2'))
    thread2.start()

    thread3 = threading.Thread(target=fragmentation, args=('fragmentation3', 'point3', 'rectangle3'))
    thread3.start()

    thread4 = threading.Thread(target=fragmentation, args=('fragmentation4', 'point4', 'rectangle4'))
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    query = "SELECT SUM(POINTS_COUNT) AS POINTS_COUNT INTO " + outputTable + " FROM (SELECT * FROM fragmentation1 UNION ALL SELECT * FROM fragmentation2 UNION ALL SELECT * FROM fragmentation3 UNION ALL SELECT * FROM fragmentation4) AS FRAG_UNION GROUP BY longitude1, latitude1, longitude2, latitude2 ORDER BY POINTS_COUNT"
    cur.execute(query)
    
    query = "SELECT * FROM " + outputTable + ""
    cur.execute(query)
    
    query = "SELECT SUM(POINTS_COUNT) FROM "+ outputTable + ""
    cur.execute(query)
    
    print('Writing to output file')
    fileout = open(outputPath, 'w+')
    
    query = "SELECT points_count FROM " + outputTable
    cur.execute(query)
    openConnection.commit()
    for each in cur.fetchall():
        fileout.write(str(each[0]) + '\n')
    fileout.close()


################### DO NOT CHANGE ANYTHING BELOW THIS #############################


# Donot change this function
def getOpenConnection(user='postgres', password='12345', dbname='dds_assignment2'):
#def getOpenConnection(user='postgres', password='cse512', dbname='dds_assignment2'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

# Donot change this function
def createDB(dbname='dds_assignment2'):
    """
    We create a DB by connecting to the default user and database of Postgres
    The function first checks if an existing database exists for a given name, else creates it.
    :return:None
    """
    # Connect to the default database
    con = getOpenConnection(dbname='postgres')
    con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    # Check if an existing database with the same name exists
    cur.execute('SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname=\'%s\'' % (dbname,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute('CREATE DATABASE %s' % (dbname,))  # Create the database
    else:
        print('A database named {0} already exists'.format(dbname))

    # Clean up
    cur.close()
    con.commit()
    con.close()

# Donot change this function
def deleteTables(tablename, openconnection):
    try:
        cursor = openconnection.cursor()
        if tablename.upper() == 'ALL':
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = cursor.fetchall()
            for table_name in tables:
                cursor.execute('DROP TABLE %s CASCADE' % (table_name[0]))
        else:
            cursor.execute('DROP TABLE %s CASCADE' % (tablename))
        openconnection.commit()
    except psycopg2.DatabaseError as e:
        if openconnection:
            openconnection.rollback()
        print('Error %s' % e)
        sys.exit(1)
    except IOError as e:
        if openconnection:
            openconnection.rollback()
        print('Error %s' % e)
        sys.exit(1)
    finally:
        if cursor:
            cursor.close()


