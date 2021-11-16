#!/usr/local/bin/python3

import re

with open("long_dna.txt", "r") as infile:
	sequence_newlines = infile.read()
	sequence = sequence_newlines.replace("\n","")

bpsm1_match_obj = re.search(r"A[AGCT]TAAT", sequence)
bpsm1_recognition_pos = bpsm1_match_obj.start()
bpsm1_cut_pos = bpsm1_recognition_pos + 3

bpsm2_match_obj = re.search(r"GC[AG][AT]TG", sequence)
bpsm2_recognition_pos = bpsm2_match_obj.start()
bpsm2_cut_pos = bpsm2_recognition_pos + 4


if bpsm2_cut_pos > bpsm1_cut_pos:
	first_frag = sequence[:bpsm1_cut_pos]
	second_frag = sequence[bpsm1_cut_pos:bpsm2_cut_pos]
	third_frag = sequence[bpsm2_cut_pos:]

else:
	first_frag = sequence[:bpsm2_cut_pos]
	second_frag = sequence[bpsm2_cut_pos:bpsm1_cut_pos]
	third_frag = sequence[bpsm1_cut_pos:]

print(f"First fragment is {first_frag} with length {len(first_frag)}")
print(f"Second fragment is {second_frag} with length {len(second_frag)}")
print(f"Third fragment is {third_frag} with length {len(third_frag)}")
print(len(sequence))

