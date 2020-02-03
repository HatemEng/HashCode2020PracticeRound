aFileName = 'a_example.in'
bFileName = 'b_small.in'
cFileName = 'c_medium.in'
dFileName = 'd_quite_big.in'
eFileName = 'e_also_big.in'
# read file
inFile = open(bFileName, 'r')
line1 = inFile.readline().strip()  # maximum and different types of  pizza
maxAllowSlices = int(line1.split(' ')[0])
types = int(line1.split(' ')[1])

line2 = inFile.readline().strip()  # slices number in each type each type
slicesTypes = line2.split(' ')

# find result
chosenTypesIndexes = []
chosenTypes = []

sum = 0
index = types
print(types)
while index >= 0:
    index = index - 1
    print("sum:",sum)
    if int(slicesTypes[index]) != 0 and sum + int(slicesTypes[index]) <= maxAllowSlices:
        print("added:",slicesTypes[index])
        sum = sum + int(slicesTypes[index])
        chosenTypesIndexes.append(index)
        chosenTypes.append(slicesTypes[index])
    if index <= 0 and sum != maxAllowSlices:
        print("remove this solution")
        if len(chosenTypesIndexes) > 0:
            slicesTypes[chosenTypesIndexes[len(chosenTypesIndexes) -1]] = 0
        sum = 0
        chosenTypesIndexes = []
        chosenTypes = []
        index = types

# output
print("Write result to output.out-------------")
print('Finally:', sum)
print('indexes', chosenTypesIndexes)
print('values', chosenTypes)
fileName = 'output.out'
outFile = open('' + fileName, 'w+')
outFile.write(str(len(chosenTypesIndexes)) + '\n')
chosenTypes.reverse()
finalSum = 0
for i in chosenTypesIndexes:
    outFile.write(str(i))
    outFile.write(' ')
