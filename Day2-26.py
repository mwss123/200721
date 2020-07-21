
seq1 = "ATGTTATAG"

"""
for i in range(len(seq1)) :
    if i % 3 == 0 :
        print(seq1[i:i+3])
"""

for i in range(0, len(seq1), 3) :
    print(seq1[i:i+3])
