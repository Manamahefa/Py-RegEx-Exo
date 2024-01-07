import re

def isValidPostalCode(postal_code: str) -> bool:
    """
        Validation de code postal dans un format spécifique. ex: 12345 ou 12345-6789
    """
    return re.match(r"\b\d{3,5}[-\d]*\b", postal_code)
