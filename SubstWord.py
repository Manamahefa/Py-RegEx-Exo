import re

def subWord(old: str, new: str, text: str) -> str:
    """
        Remplacer tous les occurence d'un mot par un autre mot dans un text
        :param old: le mot à remplacer
        :param new: le nouveau mot
        :text: le text contenant le mot à remplacer
        :return: un text modifié
    """
    pattern = r'\b'+old+r'\b'
    return re.sub(pattern, new, text)