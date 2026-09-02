#function to format notification message
def formatnotificationmessage(topapprenticeships):
    if not topapprenticeships:
        return "No scored apprenticeships available"
    lines = []
    for score, number, company, title, level, salary, location, applicationenddate in topapprenticeships:
        if salary:
            salary = f"£{salary:,.0f}"
        else:
            salary = "Not found"
        lines.append(f"{score:.0f} out of 100 pts | {title}")
        lines.append(f"   {company} | {level} | {salary} | {location}")
        lines.append(f"   closes {applicationenddate} | reference {number:.0f}")
        lines.append("")
    return "\n".join(lines)

def sendapprenticeships():
    import os, requests
    from applicationdatabase import gettopapprenticeships

    ntfytopic = os.environ.get("NTFY_TOPIC")
    if not ntfytopic:
        raise SystemExit("NTFY_TOPIC is not set.")
    topapprenticeships = gettopapprenticeships()
    apprenticeshipsmessage = formatnotificationmessage(topapprenticeships)

    response = requests.post(
    f"https://ntfy.sh/{ntfytopic}",
    data = apprenticeshipsmessage.encode("utf-8"),
    headers = {
        "Title": f"Top 5 current apprenticeships",
        "Priority": "default",
        "Tags": "briefcase",
    },
    timeout = 30,
    )