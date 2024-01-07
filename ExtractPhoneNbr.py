import re

# phone_nbr_pattern = re.compile(r'(?:\+\d{1,3})?[()\s0-9-]{13,16}') # format conventionnel
# phone_nbr_pattern = re.compile(r'\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}') # format conventionnel
phone_nbr_pattern = re.compile(r"\+2613\d{8}|03\d{8}|03\d\s\d{2}\s\d{3}\s\d{2}|\+261\s3\d\s\d{2}\s\d{3}\s\d{2}") # num GASY

def extractPhoneNbr(text: str) -> list:
    """
        EXTRACTION DES NUMEROS DE TELEPHONE D'UN TEXT
        :return: List des numéros de Téléphone trouvés
    """
    result = phone_nbr_pattern.findall(text)
    return result