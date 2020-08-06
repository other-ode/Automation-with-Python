f = open('inputFile.txt', 'r')
passFile = open('passFile.txt', 'w')
failFile = open('failFile.txt', 'w')
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        #print(str(count) + " - " + line)
        passFile.write(line)
    else:
        failFile.write(line)
    count += 1


f.close()
passFile.close()
failFile.close()