
def read_string(txt):
    pos = 0
    ret = ""
    while txt[pos] != "\"":
        ret += txt[pos]
        pos += 1
        if pos >= len(txt):
            raise SyntaxError("Expected closing quote, found EOF!")

    return ret, pos

class TExercise:
    def __init__(self, conlang, engl):
        self.conlang = conlang
        self.engl = engl

    def deserialise(txt):
        pos = 0
        if txt[pos] != "\"": raise SyntaxError("Expected quote at start of definition")
        pos += 1
        conlang, pos2 = read_string(txt[pos:])
        pos += pos2 + 1
        _, pos2 = read_string(txt[pos:])
        pos += pos2 + 1
        engl, pos2 = read_string(txt[pos:])
        return TExercise(conlang, engl)

    def __repr__(self):
        return f"TExercise(\"{self.conlang}\", \"{self.engl}\")"

def read_tef(filename):
    with open(filename, "r") as f:
        data = f.read()

    ret = []
    for line in data.split("\n"):
        if line == "": continue
        ret.append(TExercise.deserialise(line))
    return ret

if __name__ == "__main__":
    print(read_tef("tef.txt"))
