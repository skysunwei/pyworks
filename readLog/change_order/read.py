for line in open('old'):
    alls = line.split("()")
    print alls[2].count("http")

