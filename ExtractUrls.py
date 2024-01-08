import re

url_pattern = re.compile(r'(?:http[s]?://)?(?:www.)?[a-z0-9-]*[.]\w{1,}[a-z0-9-#?+=/]*', re.I)

def extractUrls(text: str) -> list:
    """
        Extraire toutes les URLs d'un text
        :return: list d'urls
    """
    return url_pattern.findall(text)
