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

word = "Python 1"
list = []
for x in word:
	list.append(x)
list.sort()
print list

string = ""
for i in range(len(list)):
	string+= list[i]
print string

dict = {}
for i, y in enumerate(string):
	dict[i] = y
print dict

for key in dict:
	print key, '=', dict[key]

word = "Pithon. Rozmowki"
string = ""
for ch in word:
	if ch =='i':
		string += 'y'
		continue
	if ch == ' ':
		break
	string += ch
print string


def a(s):
	print s
def switach(ch):
	try:
		{'1': lambda: a("jeden"),
		 '2': lambda: a("dwa"),
		 '3': lambda: a("trzy"),
		 '1': lambda: a("litera a"),
		 }[ch]()
	except KeyError:
		a("Nie znaleziono klucza")
