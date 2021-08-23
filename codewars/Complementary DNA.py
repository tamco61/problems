dct = {
	'A': 'T',
	'T': 'A',
	'C': 'G',
	'G': 'C'
	}

def DNA_strand(dna):
	return ''.join([dct[i] for i in dna])