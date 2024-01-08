import re

def isStrongPasswd(passwd = str) -> bool:
    """
        Verifie si un mot de passe est fort
    """
    is_strong_passwd = len(passwd)>=8
    patterns = ["[a-z]", "[A-Z]", "[0-9]","[è_çà=$ù!:;,#{}\[\]| +*-/&é\"'(-)^@<>]"]
    for pattern in patterns:
        is_strong_passwd &= bool(re.search(pattern, passwd))
    return is_strong_passwd
