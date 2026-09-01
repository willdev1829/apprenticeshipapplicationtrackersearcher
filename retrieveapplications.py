
def fetchvacancies():

    import os, time, requests

    BASE = "https://api.apprenticeships.education.gov.uk/vacancies"
    headersdict ={"Ocp-Apim-Subscription-Key": os.environ["APPRENTICESHIP_API_KEY"], "X-Version": "2","User-Agent": "applicationtrackersearcher/0.1 (personal apprenticeship search)" }

    page = 1
    vacancies = []
      
    while True:
        parameters = {
                    "Routes": "Digital",
                    "PageSize": 100,
                    "PageNumber": page,
                    "IncludeDetails": "true",
                    "Sort": "AgeDesc",
                    "ExcludeRecruitingNationally": "false",
                    }
        r = requests.get(f"{BASE}/vacancy", headers = headersdict, params = parameters , timeout = 30)
        r.raise_for_status()
        vacancydata = r.json()
        vacancies += vacancydata["vacancies"]
        if page >= vacancydata["totalPages"]:
            return vacancies
        page += 1
        time.sleep(2)

