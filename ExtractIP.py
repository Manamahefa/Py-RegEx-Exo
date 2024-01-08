import re

ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[0-9a-z]{1,4}:){7}[0-9a-z]{1,4}\b", re.I)

def extractIP(text: str) -> list:
    """
        Extraire toutes les addresses IP d'un texte
    """
    return ip_pattern.findall(text)
