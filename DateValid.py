import re

date_pattern = re.compile(r"\b((0[1-9])|([1-2][0-9])|(3[0-1]))/((0[1-9])|(1[0-2]))/\d{4}\b")

def validDate(date: str) -> bool:
    print(date)
    return date_pattern.match(date)

