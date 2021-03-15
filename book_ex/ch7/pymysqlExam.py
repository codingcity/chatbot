import pymysql 

conn = pymysql.connect(host='localhost', user='root', password='cdct123!', charset='utf8')
cursor = conn.cursor() 

sql = "CREATE DATABASE developer" 

cursor.execute(sql) 

conn.commit() 
conn.close()
