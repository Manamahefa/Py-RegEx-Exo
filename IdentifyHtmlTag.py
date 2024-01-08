import re

html_tag_pattern = re.compile(r"<[a-z0-9]+[\s\w='\"-:;(){}]*>|</[a-z0-9]+>|<[a-z0-9]+[\s\w='\"-:;(){}]*/>")

def identifyHtmlTag(text: str) -> list:
    """
        Identifier toutes les balises HTML dans un text
    """
    return html_tag_pattern.findall(text)
