
p = ''

with open ('read_sample.txt', 'r') as f1 :
    for line in f1 :        
        if line.startswith(">") :
            continue
         p += line


print(k) 
