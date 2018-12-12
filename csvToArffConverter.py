
import sys

if len(sys.argv) < 4:
    print "Usage: python " + sys.argv[0] + " <classIndex> <csvFile> <arffFile> [-opts]"
    print "\nOptions:\n\t-n <name>: set a name to dataset relation\n\t-r: use for regression dataset"
    exit(0)

classIndex = int(sys.argv[1])

###################
## Opening files ##

try: csvFile = open(sys.argv[2])
except:
    print "Error: can\'t open csv file"
    exit(0)

try: arffFile = open(sys.argv[3], "w")
except:
    print "Error: can\'t open destination (.arff) file"
    exit(0)

######################
## Handling options ##

regression = ('-r' in sys.argv)

relationName = (sys.argv[2][:sys.argv[2].index('.')] if '.' in sys.argv[2]\
                else sys.argv[2])

if '-n' in sys.argv:
    if len(sys.argv) <= sys.argv.index('-n') + 1:
        print "Error: define name for the dataset relation"
        exit(0)
        
    relationName = sys.argv[sys.argv.index('-n') + 1]

############################
## Converting CSV to ARFF ##

attributes = csvFile.readline().replace('\n','').replace('\r','').split(',')
data = ""
classValues = dict()

for line in csvFile:    
    data += line
    classValues[line.replace('\n','').replace('\r','').split(',')[classIndex]] = True

arffFile.write("@relation " + relationName + "\n\n")
for i in range(len(attributes)):
    if i != classIndex or regression:
        arffFile.write("@attribute " + attributes[i] + " numeric\n")
    else:
        arffFile.write("@attribute " + attributes[i] + " " + \
                       str(classValues.keys()).replace('[','{').replace(']','}').replace(' ','')\
                       + "\n")

arffFile.write("\n@data\n" + data)

arffFile.close()
