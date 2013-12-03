def printerC(dic, coding, off):
    if isinstance(dic, dict):
        print
        print off, "{"
        for x in dic:
            print off, x.encode(coding,'ignore'), ":\t",
            printerC(dic[x], coding, off + " |\t")
        print off, "}"
    elif isinstance(dic, list):
        print
        print off, "["
        for x in dic:
            printerC(x, coding, off + " |\t")
        print off, "]"
    else:
        print dic.encode(coding, "ignore")


def printer(dic, coding='utf-8'):
    printerC(dic, coding, "")


if __name__ == '__main__':
    printer({'a': {'c': {'b': 2, 'ca': 's'}, 'd': {'b': 'ca', 'ca': 's'}}, 'c': 'd'})

