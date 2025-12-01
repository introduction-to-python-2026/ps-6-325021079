path = "/content/data/codons.txt" 
file = open(path)
rows = file.readlines()
file.close()

def create_codon_dict(file_path):
    my_dic = {} 
    for row in rows:
        row = row.strip().split('\t')
        codon = row[0]
        amino_acid = row[2]
        my_dic[codon] = amino_acid
    return my_dic
