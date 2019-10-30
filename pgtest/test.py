import psycopg2
import sys
import getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
        print(opts)
        print(args)
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])

try:
    connection = psycopg2.connect(user='postgres',
                                  password='postgres',
                                  host='127.0.0.1',
                                  port='5432',
                                  database='learning')

    cursor = connection.cursor()
    print(connection.get_dsn_parameters(), '\n')

    cursor.execute('SELECT version();')
    record = cursor.fetchone()
    print("You are connected to : ", record, "\n")

    cursor.execute('SELECT * FROM customers;')
    rec_customers = cursor.fetchall()
    for row in rec_customers:
        # print("id : ", row[1])
        # print("first_name : ", row[0])
        # print("last_name : ", row[2], "\n")
        print(row[1], row[0], row[2])

except (Exception, psycopg2.Error) as error :
    print("Error while connecting to Postgres", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed!")
