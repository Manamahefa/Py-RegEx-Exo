import re

mail_pattern = re.compile("[a-z0-9._-]+@[a-z0-9]+\.[a-z0-9]{2,3}", re.I)

def isValidMail(email: str) -> bool:
    """
        Verifier si l'addresse e-mail a une format valid
        :param email: l'addresse e-mail
        :return: True si l'addresse est valid sinon False
    """
    return bool(mail_pattern.match(email))