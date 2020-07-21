


class FASTQ() :
    def __init__(self, filename) :
        self.filename = filename
        self.count = 0
    
    def read_read(self) :
        with open(self.filename, 'r') as f1 :
            for line in f1 :
                line = line.strip()
                if line.startswith("@") :
                    self.count += 1


"""
    def __name__ == "__main__" :
        if len(sys.argv) != 2 :
            print("#usage : python {sys.argv[0]} [fastq]")
""" 

t = FASTQ('061.fastq')
t.read_read()
print(t.count)
