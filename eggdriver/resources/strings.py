"""
FUNCTION normalize

Remove accents from words

Eg:
spanish_phrase = "El camión es mío"
normalize(spanish_phrase)
>>> El camion es mio
"""
def normalize(self): # Method retrieved from https://micro.recursospython.com/recursos/como-quitar-tildes-de-una-cadena.html
    """Remove accents from words"""
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = self.str.replace(a, b).replace(a.upper(), b.upper())
    return s