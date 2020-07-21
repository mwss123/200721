
l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

mx = l[0]
mn = l[0]
for i in l :
    if i > mx :
         mx = i
    if i < mn :
        mn = i
        
print(mx, mn)



# Teacher

max_val = l[0]
min_val = l[0]

for elem in l :
    if elem > max_val :
        max_val = elem
    if elem < min_val :
        min_val = elem

print(f"max : {max_val}")
print(f"min : {min_val}")
