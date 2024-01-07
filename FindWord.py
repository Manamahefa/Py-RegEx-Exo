import re

def findWord(word: str, text: str) -> tuple:
    """
        Trouver un mot dans une chaîne de caractères
        :param word: Le mot chercher
        :param text: La chaine de caractères
        :return: Tuple contenant la position de début et de fin du mot trouvé
    """
    # r"\b.......\b pour limiter le mot, cad sans sufix ou prefix
    pattern = r'\b'+word+r'\b'
    return re.search(pattern, text, re.IGNORECASE).span()
