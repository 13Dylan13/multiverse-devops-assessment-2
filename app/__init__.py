def getfile(filename):
    data = []
    with open (filename) as f:
        for line in readlines():
            data.append(line)
        return data