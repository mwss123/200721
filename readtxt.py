import sys
import json



def read_txt(file_name : str) -> str :
    ret = ""
    with open(file_name, 'r') as f1 :
        for line in f1 :
            if line.startswith(">") :
                continue
            ret += line.strip()
        return ret


def read_csv(file_name : str) -> list :
    ret = []
    with open(file_name, 'r') as f1 :
        for line in f1 :
            if line.startswith("#") :
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)

        return ret


def read_tsv(file_name : str) -> list :
    ret = []
    with open(file_name, 'r') as f1 :
        for line in f1 :
            if line.startswith("#") :
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
        return ret

def to_json(l: list, new_filename : str) -> None :
    with open(new_filename, "w") as f1 :
        json.dump(l, f1, indent = 4)


def read_json(file_name: str) -> list :
    with open(file_name, 'r') as f1 :
        l = json.load(f1)                  # file open hae seo juck-jal han type eu ro save.
    return l


if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print('#usage python {sys.argv[0]} [txt]')
        sys.exit()

    file_name = sys.argv[1]
#txt = read_txt(file_name)
    print(txt)
#ret = read_csv(file_name)
    ret = read_tsv(file_name)
    to_json(ret)
    print(ret)
