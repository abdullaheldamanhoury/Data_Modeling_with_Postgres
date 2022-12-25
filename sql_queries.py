# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
        songplay_id SERIAL PRIMARY KEY,
        ts bigint NOT NULL ,
         userId int NOT NULL,
         level varchar,
         song_id varchar,
         artist_id varchar,
         sessionId int,
         location varchar,
         userAgent varchar
                         );
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
        userId int PRIMARY KEY,
        firstName varchar,
        lastName varchar,
        gender varchar,
        level varchar
        );
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
        song_id varchar PRIMARY KEY,
        title varchar,
        artist_id varchar NOT NULL,
        year int,
        duration numeric
        );
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
         artist_id varchar PRIMARY KEY,
         artist_name varchar,
         artist_location varchar,
         artist_latitude numeric,
         artist_longitude numeric
        );
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
        ts timestamp PRIMARY KEY,
         hour int,
         day int,
         week int,
         month int,
         year int,
         weekday int
        
        );
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(
        ts ,
         userId ,
         level ,
         song_id ,
         artist_id ,
         sessionId ,
         location ,
         userAgent 
        )VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""INSERT INTO users(
        userId ,
        firstName ,
        lastName ,
        gender ,
        level 
        )VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT (userId) 
        DO UPDATE 
        SET level = EXCLUDED.level;
""")

song_table_insert = ("""INSERT INTO songs(
        song_id,
        title ,
        artist_id ,
        year ,
        duration
        )VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT (song_id)
        DO NOTHING;
""")

artist_table_insert = ("""INSERT INTO artists(
         artist_id,
         artist_name ,
         artist_location ,
         artist_latitude,
         artist_longitude
        )VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT (artist_id)
        DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time(
        ts,
         hour ,
         day ,
         week ,
         month ,
         year ,
         weekday   
        )VALUES (%s,%s,%s,%s,%s,%s,%s) 
        ON CONFLICT (ts) DO NOTHING;
""")

# FIND SONGS

song_select = ("""SELECT song_id, songs.artist_id 
               FROM songs JOIN artists ON 
               songs.artist_id = artists.artist_id 
               WHERE title = %s AND artist_name = %s AND duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]