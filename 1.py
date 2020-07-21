
d = {}

with open('059.fasta', 'r') as f1 :
    for i in f1 :
        if i.startswith(">") :
            continue
        l = i.strip()
        for k in range(len(l)) :
            if l[k] in d :
                d[l[k]] += 1
            else :
                d[l[k]] = 1

print(d)
