list= ['imie','nazwisko','tytul',2007]
letter="""
Szanowny Panie %s,\n
Dziekujemy za przeslanie ksiazki, %s.
Skontaktujemy sie z panem w %d roku."""
display = """
Tytul: %s
Autor: %s, %s
Data: %d
"""
record = "%s|%s|%s|%08d"

print letter % (list[1], list[2], list[3])

print display % (list[2], list[1], list[0], list[3])

print record % (list[0], list[1], list[2], list[3])