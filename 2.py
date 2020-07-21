

class FASTQ() :
    def __init__(self, filename) :
        self.filename = filename
        self.count = 0
        self.c = 0
    def read_read(self) :
        with open(self.filename, 'r') as f1 :
            for line in f1 :
                self.c += 1
            self.count = self.c / 4
            return self.count


t = FASTQ('061.fastq')
t.read_read()
print(t.c, t.count)
