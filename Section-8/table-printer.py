tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice','Bob', 'Carol','David'],
             ['dogs','cats','moose','goose']]

def printTable(lists):
    colWidths = [0] * len(tableData)
    
    # all list lengths will always be the same, and first index will always exist. grab that length
    listLength = len(lists[0])
    
    # loop through each word of each list to find the longest string, save that to the colWidth for each list
    for list in range(len(lists)):
        for word in range(len(lists[list])):
            if len(lists[list][word]) > colWidths[list]:
                   colWidths[list] = len(lists[list][word])
  
    # print em out, right justified
    for word in range(len(lists[0])):
	    for list in range(len(lists)):
		    print(lists[list][word].rjust(colWidths[list]), end = ' ')
	    print('')

printTable(tableData)
