#!/usr/local/bin/python3

import re 

accessions = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

for acc in accessions:
#	if re.search(r"5", acc):
#		print(f"{acc} has a 5 in it.")
#	if re.search(r"[de]", acc):
#		print(f"{acc} has a 'd' or 'e' in it.")
#	if re.search(r"de", acc):
#               print(f"{acc} has a 'de' in it.")
#	if re.search(r"d[^1,2,3,4,5,6,7,8,9,0]e", acc):
#		print(f"{acc} has a d and e in that order with a single letter between them")
#	if re.search(r"(de|ed)", acc):
#		print(f"{acc} has a 'de' or 'ed' in it.")
#	if re.search(r"^[xy]", acc):
#		print(f"{acc} starts with 'x' or 'y'.")
#	if re.search(r"^[xy].*e$", acc):
#		print(f"{acc} starts with 'x' or 'y' and ends with 'e'.")
#	if re.search(r"[1,2,3,4,5,6,7,8,9,0]{3,}", acc):
#		print(f"{acc} contains three or more numbers in a row.")
#	if re.search(r"", acc):
#		print(f"{acc} contains three numbers in any order.")

	if re.search(r"d[arp]$", acc):
		print(f"{acc} ends with d followed by either a, r or p.")
