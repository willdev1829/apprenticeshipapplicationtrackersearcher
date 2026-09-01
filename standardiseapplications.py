def standardiseapplication(vacancy):
    def normalise(vacancy):
        return (
            storetext(checkalllevels(vacancy, "vacancyReference")),
            storetext(checkalllevels(vacancy, "employerName")),
            storetext(checkalllevels(vacancy, "title")),
            storetext(checkalllevels(vacancy, "apprenticeshipLevel")),
            storenumber(checkalllevels(vacancy, "wage", "wageAmount")),
            storetext(checkalllevels(vacancy, "addresses", "postcode")),
            storedate(checkalllevels(vacancy, "postedDate")),
            storedate(checkalllevels(vacancy, "closingDate")),
            storedate(checkalllevels(vacancy, "startDate")),
              )

    def checkalllevels(vacancy, *keys):
        for k in keys:
            if isinstance(k, int):
                if not isinstance(vacancy, list) or len(vacancy) <= k: 
                    return None
                vacancy = vacancy(k)
            else:
                if not isinstance(vacancy, dict): 
                    return None
                vacancy = vacancy.get(k)
        return vacancy

    def storetext(value):
        if value is None:
            return None
        return str(value).strip() or None

    def storenumber(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    def storedate(value):
        date = storetext(value)
        return date[:10] if date else None
    standardisedvacancy = normalise(vacancy)
    return standardisedvacancy
