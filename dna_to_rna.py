from re import sub
def dna_to_rna(dna):
    return sub('T', 'U', dna)


print(dna_to_rna('GCAT'))
print(dna_to_rna('TTTT'))
print(dna_to_rna("GACCGCCGCC"))