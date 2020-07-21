
seq = "ATGTTATAG"

d = {"A" : "t", "T" : "a", "G" : "c", "C" : "g"}

comple = "" 

for i in seq :
    comple += (d[i]) 

print(comple.upper())



# Teacher

import sys

def comp1(seq: str) -> str :
    comp = ""
    for s in seq :
        if s == "A" :
            comp += "T"
        if s == "T" :
            comp += "A"
        if s == "G" :
            comp += "C"
        if s == "C" :
            comp += "G"
    return comp


def comp2(seq : str) -> str :
    d_comp = {"A":"T","T":"A","G":"C","C":"G"}
    comp ""

    for s in seq :
        comp += d_comp[s]
    return comp

if __name__ == "__main__" :
    if len(sys.argv) !=2 :
        print(f"#usage : python {sys.argv[1]} [string]")
        sys.exit()

    seq = sys.argv[1]
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)


