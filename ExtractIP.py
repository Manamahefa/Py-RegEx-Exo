import re

ip_pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b|\b[\da-f]{2}\.[\da-f]{2}\.[\da-f]{2}\.[\da-f]{2}\.[\da-f]{2}\.[\da-f]{2}\b")

def extractIP(text: str) -> list:
    """
        Extraire toutes les addresses IP d'un texte
    """
    return ip_pattern.findall(text)
