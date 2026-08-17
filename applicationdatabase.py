#function to store data in database
def storenewapprenticeship(score,company,title,level,salary,location,applicationstartdate,applicationenddate,startdate):

    import sqlite3

    #define a connection to connect to the calulations database and define a cursor so that tables within the database can be created and edited.

    connection = sqlite3.connect('apprenticeshiplog.db') #opens connection to database
    cursor = connection.cursor() #create cursor so SQL queries can be executed in database.

    #create a table to store previous values of calculations

    cursor.execute("""CREATE TABLE IF NOT EXISTS openapprenticeships (
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

    cursor.execute("INSERT INTO pastcalculations(score, company, title, level, salary, location, applicationstartdate, applicationenddate, startdate) VALUES (?,?,?,?,?,?,?,?,?)", #inserts data of last calculation into the table
                   (score,company,title,level,salary,location,applicationstartdate,applicationenddate,startdate)
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

    cursor.execute("INSERT INTO applicationtracker(company, applicationcompleted, onlineassessmentscompleted, onlineinterviewcompleted, (online/inperson)assessmentcentrecompleted, offerrecieved) VALUES (?,?,?,?,?,?)", #inserts data of last calculation into the table
                   (company,applicationcompleted,onlineassessmentscompleted,onlineinterviewcompleted,onlineinpersonassessmentcentrecompleted,offerrecieved)
                   )

    connection.commit() #commits changes to database.

    connection.close() #closes connection to database