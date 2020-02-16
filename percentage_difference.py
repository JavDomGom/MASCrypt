def percentage_difference(header, a, b):
    print(header)
    print(f'SAMCrypt = {a}s')
    print(f'MASCrypt = {b}s')
    print(f'Time reduced by {((a - b) / a) * 100}%\n')


# =============================================================================

# 5 records in Primitive root from SAMCrypt.
a_0 = 3.854
b_0 = 3.851
c_0 = 3.851
d_0 = 3.851
e_0 = 3.853

# 5 records in Primitive root from MASCrypt.
a_1 = 0.020031452178955078
b_1 = 0.018837928771972656
c_1 = 0.015370607376098633
d_1 = 0.016665220260620117
e_1 = 0.01695561408996582

# Average.
SAMCrypt = (a_0+b_0+c_0+d_0+e_0)/5
MASCrypt = (a_1+b_1+c_1+d_1+e_1)/5

percentage_difference(f'Primitive root\n{"="*35}', SAMCrypt, MASCrypt)

# =============================================================================

# 5 records in Factorization from SAMCrypt.
a_0 = 0.019
b_0 = 0.015
c_0 = 0.010
d_0 = 0.026
e_0 = 0.007

# 5 records in Factorization from MASCrypt.
a_1 = 0.006754875183105469
b_1 = 0.006248950958251953
c_1 = 0.0056874752044677734
d_1 = 0.00951242446899414
e_1 = 0.006460666656494141

# Average.
SAMCrypt = (a_0+b_0+c_0+d_0+e_0)/5
MASCrypt = (a_1+b_1+c_1+d_1+e_1)/5

percentage_difference(f'Factorization\n{"="*35}', SAMCrypt, MASCrypt)

# =============================================================================

# 5 records in Discrete Logarithm from SAMCrypt.
a_0 = 24.530
b_0 = 24.722
c_0 = 22.368
d_0 = 23.619
e_0 = 23.429

# 5 records in Discrete Logarithm from MASCrypt.
a_1 = 14.824936151504517
b_1 = 14.629260540008545
c_1 = 14.565803766250610
d_1 = 14.673845529556274
e_1 = 14.543920516967773

# Average.
SAMCrypt = (a_0+b_0+c_0+d_0+e_0)/5
MASCrypt = (a_1+b_1+c_1+d_1+e_1)/5

percentage_difference(f'Discrete Logarithm\n{"="*35}', SAMCrypt, MASCrypt)
