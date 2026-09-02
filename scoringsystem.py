#code for scoring new applications
#The basis for these scoring are as follows:
#Company size/Reputation, Level of apprenticeship, Salary, Location
def scorevacancy(vacancy):
    #scoring system for apprenticeship level
    def scoreapprenticeshiplevel(apprenticeshiplevel):
        if apprenticeshiplevel == "Degree":
            levelscore = 20
        elif apprenticeshiplevel == "Higher":
            levelscore = 5
        else:
            levelscore = 0
        return levelscore

    #scoring system for location
    def getlocationscore(mypostcode, companypostcode):
        import math
        if not companypostcode:
            return 0
        import pgeocode
        area = pgeocode.GeoDistance("GB")
        distancekm = area.query_postal_code(mypostcode,companypostcode)
        if distancekm is None or math.isnan(float(distancekm)):
            return 3
        distancemiles = distancekm * 0.621371192
        return distancemiles

    def scorelocation(mypostcode, companypostcode):
        distancemiles = getlocationscore(mypostcode,companypostcode)
        if distancemiles <= 25:
            locationscore = 5
        elif distancemiles <= 50:
            locationscore = 4
        elif distancemiles <= 100:
            locationscore = 3
        elif distancemiles <= 150:
            locationscore = 2
        else:
            locationscore = 1
        return locationscore

    #scoring system for salary

    def getsalaryscore(salaryvalue):
        if salaryvalue is None:
            return 3
        salaryscore=0
        if salaryvalue <= 20000.0:
            salaryscore = 1
        elif salaryvalue <= 22000.0:
            salaryscore = 2
        elif salaryvalue <= 24000.0:
            salaryscore  = 3
        elif salaryvalue <= 26000.0:
            salaryscore = 5
        else:
            salaryscore = 10
        return salaryscore

    def scoresalary(salaryvalue):
        salaryscore = getsalaryscore(salaryvalue)
        return salaryscore

    #scoring system for company

    companydict = {
                    "Accenture": 5, 
                    "Google" : 5,
                    "Amazon": 5,
                    "Microsoft": 5,
                    "JPMorgan" : 5,
                    "BAE" : 5,
                    "JLR" : 5,
                    "Bloomberg" : 4,
                    "Rolls-Royce": 5,
                }

    def getcompanyscore(companyname):
        hascompany = 0
        hascompany = companydict.get(companyname)

        if hascompany != None:
            companyscore  = companydict.get(companyname)
        else:
            companyscore = 3

        return companyscore

    def scorecompany(companyname):
        companyscore = getcompanyscore(companyname)
        return companyscore

    #overall scoring system for single vacancy

    def producescore(vacancy):
        locationscore = scorelocation("WV3", vacancy[5])
        levelscore = scoreapprenticeshiplevel(vacancy[3])
        salaryscore = scoresalary(vacancy[4])
        companyscore = scorecompany(vacancy[1])
        if locationscore is None:
            locationscore = 0
        elif levelscore is None:
            levelscore = 0
        elif salaryscore == None:
            salaryscore = 0
        elif companyscore is None:
            companyscore = 0
        totalscore = locationscore + levelscore + salaryscore + companyscore
        totalscore = totalscore * 2.5 #ensures scores are scaled up so that the scoring system is out of 100
        return totalscore

    score = producescore(vacancy)
    return score