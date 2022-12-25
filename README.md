### Project description
- A data modeling was built with Postgres with an ETL pipeline using Python by creating star schema which was about of fact and dimensions tables and wrote an ETL pipline to transfer data from files to tables using Python and SQL.

### Database design
- Fact table: songplays table with attributes(songplay_id, ts, userId, level, song_id, artist_id, sessionId, location, userAgent)

- Dimension Tables :
    1. users table with attributes (userId, firstName, lastName, gender, level)
    2. songs table with attributes (song_id, title, artist_id, year, duration)
    3. artists table with attributes (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    4. time table - timestamps with extracted attributes(ts, hour, day, week, month, year, weekday)

### Project Repository files

1. Create_tables.py creates and drops the database using queries from sql_queries.py file
2. etl.ipynb processes, reads and loads a single file from log_data and song_data into our tables.
3. etl.py processes, reads and loads files from log_data and song_data into our tables.
4. sql_queries.py contains the SQL queries that are used by the files above
5. test.ipynb displays the first few rows of each table to verify the creation of the database


### Project Steps:

1. Inisialize the database by running create_tables.py

2.  Run etl.ipynb file to:
    - perform ETL on the first dataset, song_data, to create the songs and artists dimensional tables
        1. Extract Data for Songs Table
        2. Insert Record into Song Table by Implementing the song_table_insert query in sql_queries.py
        3. Extract Data for Artists Table
        4. Insert Record into Artists Table by Implementing the artist_table_insert query in sql_queries.py
        5. Run test.ipynb to see if you've successfully added a record to this table
            
    - perform ETL on the second dataset, log_data, to create the time and users dimensional tables, as well as the songplays fact
       table.
         1. Extract Data for Time Table
         2. Insert Records into Time Table by Implementing the time_table_insert query in sql_queries.py
         3. Extract Data for Users Table
         4. Insert Records into Users Table by Implementing the user_table_insert query in sql_queries.py
         5. Extract Data and Songplays Table
         6. Implement the song_select query in sql_queries.py
         7. Insert Records into Songplays Table by Implementing the songplay_table_insert query
         8. Run test.ipynb to see if you've successfully added records to this table
             
3. Close Connection to Sparkify Database and Restart test notebook to close connection to sparkifydb

4. Reinitialize the database by running create_tables.py

5. Start the ETL data pipeline by Implementing and running etl.py

