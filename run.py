def rundailycheck():
    from retrieveapplications import fetchvacancies
    from standardiseapplications import standardiseapplication
    from applicationdatabase import storeallapprenticeship, storevalidapprenticeship, gettopapprenticeships
    from scoringsystem import scorevacancy
    from sendnotification import sendapprenticeships
    vacancies = fetchvacancies()
    for vacancy in vacancies:
        standardisedvacancy = standardiseapplication(vacancy)
        score = scorevacancy(standardisedvacancy)
        number = standardisedvacancy[0]
        company = standardisedvacancy[1]
        title = standardisedvacancy[2]
        level = standardisedvacancy[3]
        salary = standardisedvacancy[4]
        location = standardisedvacancy[5]
        applicationstartdate = standardisedvacancy[6]
        applicationenddate = standardisedvacancy[7]
        startdate = standardisedvacancy[8]
        storeallapprenticeship(score, number, company, title, level, salary, location, applicationstartdate, applicationenddate, startdate)
    storevalidapprenticeship()
    topapprenticeships = gettopapprenticeships()
    sendapprenticeships()
rundailycheck()