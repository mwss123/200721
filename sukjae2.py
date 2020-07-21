
#4

import json

class Sukjae() :
    def __init__(self, filename) :
        self.filename = filename
        self.dic = {}
    def read_csv(self) :
        l = []
        with open(self.filename, 'r') as f1 :
            imsi = []
            for line in f1 :
                k = line.strip().split(',')
                imsi.append(k)
            d = dict(zip(imsi[0], imsi[1]))
        return d

    def to_json(self, l, new_filename : str) :
        print(l)
        with open(new_filename, "w") as f2 :
            json.dump(l, f2, indent=4)

    
t = Sukjae('2_4.csv')
ddic = t.read_csv()
print(t.read_csv())

t.to_json(ddic, '2_4.json')
