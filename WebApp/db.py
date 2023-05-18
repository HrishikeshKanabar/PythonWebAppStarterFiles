## STEP-1 : Importing My SQL Connector
import mysql.connector;

## STEP-2: Establishing connection by "connect" method
connection=mysql.connector.connect(
  user='root',
  password='',
  host='127.0.0.1',
  database='employees'

)

## STEP:3 Creating variable to excecute our query by "Cursor" method
sqlObj= connection.cursor()

## STEP:4 Write Query
query = 'SELECT * FROM EMPLOYEES LIMIT 1;'

## STEP:5 Excecute query by "Excecute" method
sqlObj.execute(query)

## STEP:6 Get and Store result by "Fetch ALL" method
result = sqlObj.fetchall()
###print(result)

for recs in result:
    print(recs[0])

