import os
import requests

API_URL = "https://api.apprenticeships.education.gov.uk/vacancies/vacancy"

headers = {
    "Ocp-Apim-Subscription-Key": os.environ["APPRENTICESHIP_API_KEY"],
    "X-Version": "2",
}

params = {"PageSize": 10, "PageNumber": 1}

response = requests.get(API_URL, headers=headers, params=params, timeout = 45)
print(response.status_code)

if response.status_code != 200:
    print(response.text)

response.raise_for_status()

apprenticeshipdata = response.json()

print(f"total: {apprenticeshipdata['total']}, pages: {apprenticeshipdata['totalPages']}")

for vacancy in apprenticeshipdata["vacancies"]:
    print(vacancy["vacancyReference"], "|", vacancy["employerName"], "|", vacancy["title"])