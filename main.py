
def counting():
    numberOfWords=0

    f=open("test.txt", "r")
    for lines in f:
        words = lines.split()
        numberOfWords= numberOfWords + len(words)
    print(numberOfWords)

counting()




