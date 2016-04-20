mport sys
import sqlite3
import os


directory = sys.argv[1]
db = sys.argv[2]


print directory
print db


conn = sqlite3.connect(db)
print 'opened database successfully'


curs = conn.cursor()


curs.execute('''CREATE TABLE files(ext TEXT, path TEXT, fname TEXT)''')


curs.execute("INSERT INTO files VALUES ('.cpp', '~/downloads', 'python.thong')")


conn.commit()




#for ext, path, fname in os.walk(directory):
#    print ext
#    print path
#    print fname





