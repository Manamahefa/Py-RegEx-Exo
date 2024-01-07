import re

def isValidPostalCode(postal_code: str) -> bool:
    """
        Validation de code postal dans un format spécifique. ex: 12345 ou 12345-6789
    """
    # print(postal_code, re.match(r"\b[0-9]{3,5}\b", postal_code))
    return re.match(r"\b\d{3,5}[-\d]*\b", postal_code)

print(isValidPostalCode("123-44568"))