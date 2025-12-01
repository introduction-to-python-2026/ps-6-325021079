
def create_codon_dict(file_path):
    my_dic = {}
    with open(file_path) as file:
        rows_from_file = file.readlines()
    for row in rows_from_file:
        parts = row.strip().split('\t')
        codon = parts[0]
        amino_acid = parts[2]
        my_dic[codon] = amino_acid
    return my_dic
