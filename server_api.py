import json
import bottle
import time
import calendar
import sys
from datetime import date
import MySQLdb
from bottle import route, run, request, response, abort, default_app, \
    get, post


#READ Credentials
args = open('creds.txt', 'r')
args = args.readline().split(',')
DB_SERVER = args[0]
USER = args[1]
PASSWORD = args[2]
DATABASE = args[3]

#Connect database
db = MySQLdb.connect(host=DB_SERVER, user=USER, passwd=PASSWORD, db=DATABASE)
cursor=db.cursor()


def main():
        print "Starting bottle server"
        run(host='localhost', port=8080)


@route('/getUser')
def getUser():
        rq_id = request.query.id
        query = "select * from users where id = %s" % (rq_id)
        cursor.execute(query)
        row = cursor.fetchone()
        data = {
        'id': row[0],
        'user': row[1],
        'cuisine': row[3],
        'date_time': str(row[4]),
        }
        
        json_data = json.dumps(data)
        return json_data

main()
