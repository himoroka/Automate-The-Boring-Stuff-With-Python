tableData = [['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable():
    global colWith 
    colWith = [0] * len(tableData)
    for i in range(0,len(tableData)):
        rowWith = [0] * len(tableData[i])
        for j in range(len(tableData[i])):
            rowWith[j] = len(tableData[i][j])
            colWith[i]=max(rowWith)
    print(colWith)


printTable()
for k in range(len(tableData[0])):
    for v in range(len(tableData)):
        print(tableData[v][k].rjust(colWith[v]+1),end='')
    print('')
