def dna_to_rna(dna):
    return dna.replace('/T/g', 'U')


print(dna_to_rna('GCAT'))