import re

mail_pattern = re.compile(r"\b[a-z0-9._-]+@[a-z0-9]+\.[a-z0-9]{2,3}\b", re.I)

def isValidMail(email: str) -> bool:
    """
        Verifie le format d'une addresse e-mail
        :param email: l'addresse e-mail
        :return: True si l'addresse est valid sinon False
    """
    return bool(mail_pattern.match(email))
