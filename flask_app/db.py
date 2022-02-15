import csv
import psycopg2

# psycopg2로 postgreSQL 과 연동

try:
    conn = psycopg2.connect(host='localhost', dbname='past_weather',user='postgres',
                        password='', port='5433')
except:
    print("NOT CONNECTED!")
    
cur = conn.cursor()

# past weather table 생성

cur.execute("DROP TABLE IF EXISTS past_weather;")
cur.execute(
        """CREATE TABLE past_weather (
            id INTEGER PRIMARY KEY NOT NULL,
            id_num INTEGER,
            avg_temp FLOAT,
            avg_rain FLOAT,
            avg_wind FLOAT,
            season INTEGER,
            outfit INTEGER);
            """)

conn.commit()

# past_weather data 넣기

with open('weather.csv','r', encoding='UTF8') as file:
    rows = csv.reader(file)
    next(rows)
    for i in rows:
        cur.execute(f"""INSERT INTO past_weather (id, id_num, avg_temp,avg_rain, avg_wind, season, outfit)
                        VALUES ({i[0]}, {i[1]}, {i[2]}, {i[3]},{i[4]}, {i[5]}, {i[6]});""")


conn.commit()
cur.close()
conn.close()

