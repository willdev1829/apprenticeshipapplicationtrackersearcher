#function to store data in database
def storevalidapprenticeship(number, score,company,title,level,salary,location,applicationstartdate,applicationenddate,startdate):

    import sqlite3

    #define a connection to connect to the calulations database and define a cursor so that tables within the database can be created and edited.

    connection = sqlite3.connect('apprenticeshiplog.db') #opens connection to database
    cursor = connection.cursor() #create cursor so SQL queries can be executed in database.

    #create a table to store previous values of calculations

    cursor.execute("""CREATE TABLE IF NOT EXISTS validapprenticeships (
            number real
            score real
            company text,
            title real,
            level real,
            salary real,
            location text,
            applicationstartdate text,
            applicationenddate text,
            startdate text
            )""")

    cursor.execute("INSERT INTO validapprenticeships(number, score, company, title, level, salary, location, applicationstartdate, applicationenddate, startdate) VALUES (?,?,?,?,?,?,?,?,?,?)", #inserts data of last calculation into the table
                   (number,score,company,title,level,salary,location,applicationstartdate,applicationenddate,startdate)
                   )

    connection.commit() #commits changes to database.

    connection.close() #closes connection to database



def updateapplicationtracker(company,applicationcompleted,onlineassessmentscompleted,onlineinterviewcompleted,onlineinpersonassessmentcentrecompleted,offerrecieved):

    import sqlite3

    #define a connection to connect to the calulations database and define a cursor so that tables within the database can be created and edited.

    connection = sqlite3.connect('apprenticeshiplog.db') #opens connection to database
    cursor = connection.cursor() #create cursor so SQL queries can be executed in database.

    #create a table to store previous values of calculations

    cursor.execute("""CREATE TABLE IF NOT EXISTS applicationtracker (
            company text,
            applicationcompleted text,
            onlineassessmentscompleted text,
            onlineinterviewcompleted text,
            (online/inperson)assessmentcentrecompleted text,
            offerrecieved text
            )""")

    cursor.execute("INSERT INTO applicationtracker(company, applicationcompleted, onlineassessmentscompleted, onlineinterviewcompleted, (online/inperson)assessmentcentrecompleted, offerrecieved) VALUES (?,?,?,?,?,?)", #inserts data into table
                   (company,applicationcompleted,onlineassessmentscompleted,onlineinterviewcompleted,onlineinpersonassessmentcentrecompleted,offerrecieved)
                   )

    connection.commit() #commits changes to database.

    connection.close() #closes connection to database

def fetchmostrecentapprenticeship():
    import sqlite3
        
    #define a connection to connect to the apprenticeshiplog database and define a cursor so that SQL queries can be committed within tables
    connection = sqlite3.connect('apprenticeshiplog.db') #opens connection to database
    cursor = connection.cursor() #create cursor so SQL queries can be executed in database.
    
    #Query to select most recent apprenticeship row. Does this by ordering rows in terms of lowest number first. Then has a limit of 1, so only the newest row is selected.
    
    cursor.execute("""SELECT * 
                FROM allapprenticeships 
                ORDER BY number ASC
                LIMIT 1 """)
    mostrecentapprenticeship = cursor.fetchone() #fetches the result of the query and stores it in variable 'mostrecentapprenticeship'
        
    connection.close() #closes connection to database

    return mostrecentapprenticeship

#function to store all apprenticeships, before sifting for only valid ones.

def storeallapprenticeship(score, number,company,title,level,salary,location,applicationstartdate,applicationenddate,startdate):

    import sqlite3

    #define a connection to connect to the calulations database and define a cursor so that tables within the database can be created and edited.

    connection = sqlite3.connect('apprenticeshiplog.db') #opens connection to database
    cursor = connection.cursor() #create cursor so SQL queries can be executed in database.

    #create a table to store previous values of calculations

    cursor.execute("""CREATE TABLE IF NOT EXISTS allapprenticeships (
            score real,
            number real,
            company text,
            title text,
            level real,
            salary real,
            location text,
            applicationstartdate text,
            applicationenddate text,
            startdate text
            )""")

    cursor.execute("INSERT INTO allapprenticeships(score, number, company, title, level, salary, location, applicationstartdate, applicationenddate, startdate) VALUES (?, ?,?,?,?,?,?,?,?,?)", #inserts data of last calculation into the table
                   (score, number,company,title,level,salary,location,applicationstartdate,applicationenddate,startdate)
                   )

    connection.commit() #commits changes to database.

    connection.close() #closes connection to database