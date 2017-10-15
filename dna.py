dna = "AATTCGAACCGTGCTAGATCGGATTACGATACGATCGATCAGGGTACTCATCATCATACTGGGTGTGTCAG"

counter = range(0,len(dna))

for x in counter:
    counter[x] = len(dna)-(x+1)

rev_dna = []
for x in counter:
    rev_dna.append(dna[x])

reverse_dna = "".join(rev_dna)

print 'REVERSE:'
print(reverse_dna)
print 'REVERSE CHECK:'
print (dna[::-1])


comp_dna = dna.replace('A','1').replace('C','2').replace('G','3').replace('T','4').replace('4','A').replace('1','T').replace('2','G').replace('3','C')

print 'COMPLEMENT:'
print (comp_dna)

counter2 = range(0,len(comp_dna))

for x in counter2:
    counter2[x] = len(comp_dna)-(x+1)

rev_comp_dna = []
for x in counter2:
    rev_comp_dna.append(comp_dna[x])

reverse_comp_dna = "".join(rev_comp_dna)

print 'REVERSE COMPLEMENT:'
print (reverse_comp_dna)