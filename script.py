import seq_utils

f = "ecoli-data/Escherichia_coli_o5_k4_l_h4_str_atcc_23502.GCA_000333195.1.26.pep.all.fa"

print(seq_utils.only_contains_valid_protein_seq(f))
