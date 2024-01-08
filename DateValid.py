import re

#date au format "dd/mm/yyyy"
date_pattern = re.compile(r"\b((0[1-9])|([12][0-9])|(3[01]))/((0[1-9])|(1[0-2]))/\d{4}\b")

def isValidDate(date: str, date_pattern = date_pattern) -> bool:
    """
        Verifie une date au format date_pattern
    """
    return bool(date_pattern.match(date))
