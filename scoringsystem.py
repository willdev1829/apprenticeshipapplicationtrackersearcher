#code for scoring new applications
#The basis for these scoring are as follows:#
#Company size/Reputation, Level of apprenticeship, Salary, Location

from applicationdatabase import fetchmostrecentapprenticeship #so function can be called to retrieve information



def createscore():
    mostrecentapprenticeship = fetchmostrecentapprenticeship()
    company = mostrecentapprenticeship[1]
    level = mostrecentapprenticeship[3]
    salary = mostrecentapprenticeship[4]
    location = mostrecentapprenticeship[5]

    companyscore = scorebasedoncompany(company)



def scorebasedoncompany(company):
    #code to see which tier the company is within in comparison to my database.
    import