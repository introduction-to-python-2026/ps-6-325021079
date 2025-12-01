def create_codon_dict(file_path):
    my_dic = {}
    with open(file_path) as codons_file:
        my_dic = {row.strip().split('\t')[0]: row.strip().split('\t')[2] for row in codons_file.readlines()}
    return my_dic
