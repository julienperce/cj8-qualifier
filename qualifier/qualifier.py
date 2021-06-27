from typing import Any, List, Optional
import math

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    if not labels: # single column table / or no labels
        # test if no labels but still more than 1 column
        if len(rows[0]) > 1:
            numItems = len(rows[0])

            if centered:
                longestItems = [] # find longest items in each column, to line up spaces
                for i in range(0, numItems): 
                    longestItem = 0
                    for row in rows:
                        if len(str(row[i])) > longestItem:
                            longestItem = len(str(row[i]))
                    longestItems.append(longestItem)

                # top delimiter
                print("┌", end="") 
                for i in range(0, numItems):
                    for v in range(0, ((longestItems[i]) + 2)):
                        print("─", end="")
                    if i == (numItems - 1):
                        print("┐")
                    else:
                        print("┬", end="")

                # main info
                for row in rows:
                    print("│", end="")
                    for i in range(0, len(row)):
                        if len(str(row[i])) == longestItems[i]:
                            print(" ", end="")
                            print(row[i], end="")
                            print(" ", end="")
                            if i == (numItems - 1):
                                print("│")
                            else:
                                print("│", end="")
                        else:
                            neededSpaces = (longestItems[i] - len(str(row[i]))) / 2
                            
                            if neededSpaces % 2 == 0:
                                for v in range (-1, int(neededSpaces)):
                                    print(" ", end="")
                                print(row[i], end="")
                                for z in range (-1, int(neededSpaces)):
                                    print(" ", end="")
                                if i == (numItems - 1):
                                    print("│")
                                else:
                                    print("│", end="")
                            else:
                                neededSpacesLeft = math.floor(neededSpaces)
                                neededSpacesRight = math.ceil(neededSpaces)
                                for v in range(-1, neededSpacesLeft):
                                    print(" ", end="")
                                print(row[i], end="")
                                for z in range(-1, neededSpacesRight):
                                    print(" ", end="")
                                if i == (numItems - 1):
                                    print("│")
                                else:
                                    print("│", end="")  
                
                # end delimiter
                print("└", end="") 
                for i in range(0, numItems):
                    for v in range(0, ((longestItems[i]) + 2)):
                        print("─", end="")
                    if i == (numItems - 1):
                        print("┘")
                    else:
                        print("┴", end="")  

            else:
                longestItems = [] # find longest items in each column, to line up spaces
                for i in range(0, numItems): 
                    longestItem = 0
                    for row in rows:
                        if len(str(row[i])) > longestItem:
                            longestItem = len(str(row[i]))
                    longestItems.append(longestItem)

                # top delimiter
                print("┌", end="") 
                for i in range(0, numItems):
                    for v in range(0, ((longestItems[i]) + 2)):
                        print("─", end="")
                    if i == (numItems - 1):
                        print("┐")
                    else:
                        print("┬", end="")

                #main info
                for row in rows:
                    print("│", end="")
                    for i in range(0, len(row)):
                        if len(str(row[i])) == longestItems[i]:
                            print(" ", end="")
                            print(row[i], end="")
                            print(" ", end="")
                            if i == (numItems - 1):
                                print("│")
                            else:
                                print("│", end="")
                        else:
                            neededSpaces = longestItems[i] - len(str(row[i]))
                            print(" ", end="")
                            print(row[i], end="")
                            for v in range(-1, neededSpaces):
                                print(" ", end="")
                            if i == (numItems - 1):
                                print("│")
                            else:
                                print("│", end="")
                
                # end delimiter
                print("└", end="") 
                for i in range(0, numItems):
                    for v in range(0, ((longestItems[i]) + 2)):
                        print("─", end="")
                    if i == (numItems - 1):
                        print("┘")
                    else:
                        print("┴", end="")

                
        
        else:
            longest = 0
            for row in rows:
                if len(str(row[0])) > longest:
                    longest = len(str(row[0]))
            neededChars = longest + 2
            
            # start printing our table
            print("┌", end="") # start delimiter
            for i in range(0, neededChars):
                print("─", end="") # add end="" to not go to newline
            print("┐") # end delimiter, with line skip this time
            
            if centered:
                for row in rows: 
                    if len(str(row[0])) == longest:
                        print("│", row[0], "│")
                    else:
                        neededSpaces = longest - len(str(row[0]))
                        if neededSpaces % 2 == 0:
                            neededSpacesSides = int(neededSpaces / 2)
                            print("│", end="")
                            for i in range(0, neededSpacesSides + 1): # +1 because we have default 1space buffer for longest
                                print(" ", end="")
                            print(row[0], end="")
                            for i in range(0, neededSpacesSides + 1):
                                print(" ", end="")
                            print("│")
                        else:
                            startSpaces = math.floor(neededSpaces / 2)
                            endSpaces = math.ceil(neededSpaces / 2)
                            print("│", end="")
                            for i in range(0, (int(startSpaces) + 1)):
                                print(" ", end="")
                            print(row[0], end="")
                            for i in range(0, (int(endSpaces)+ 1)):
                                print(" ", end="")
                            print("│")
            else:
                for row in rows:
                    if len(str(row[0])) == longest:
                        print("│", row[0], "│")
                    else:
                        print("│", row[0], end="")
                        neededSpaces = longest - len(str(row[0]))
                        for i in range (-1, neededSpaces):
                            print(" ", end="")
                        print("│")        

            print("└", end="")  
            for i in range(0, neededChars):
                print("─", end="")
            print("┘")
    
    else: # multiple columns
        if centered: 
            labelQuan = len(labels)
            longestItems = [] # find longest items in each column, to line up spaces
            for i in range(0, labelQuan): 
                longestItem = len(str(labels[i]))
                for row in rows:
                    if len(str(row[i])) > longestItem:
                        longestItem = len(str(row[i]))
                longestItems.append(longestItem)

            # top delimiter
            print("┌", end="") 
            for i in range(0, labelQuan):
                for v in range(0, ((longestItems[i]) + 2)):
                    print("─", end="")
                if i == (labelQuan - 1):
                    print("┐")
                else:
                    print("┬", end="")

            # label headers
            print("│ ", end="")
            for i in range(0, labelQuan):
                if len(str(labels[i])) == longestItems[i]:
                    print(labels[i], end="") 
                    if i == (labelQuan - 1):
                        print(" │")
                    else:
                        print(" │ ", end="")
                
                else:
                    neededSpaces = longestItems[i] - len(str(labels[i]))
                    if neededSpaces % 2 == 0:
                        neededSpacesSides = int(neededSpaces / 2)
                        for v in range(0, neededSpacesSides): 
                            print(" ", end="")
                        print(labels[i], end="")
                        for z in range(-1, neededSpacesSides):
                            print(" ", end="")
                        if i == (labelQuan - 1):
                            print("│")
                        else:
                            print("│ ", end="")
                    else:
                        startSpaces = math.floor(neededSpaces / 2)
                        endSpaces = math.ceil(neededSpaces / 2)
                        for v in range(0, (int(startSpaces))):
                            print(" ", end="")
                        print(labels[i], end="")
                        for z in range(-1, (int(endSpaces))):
                            print(" ", end="")
                        if i == (labelQuan - 1):
                            print("│")
                        else:
                            print("│ ", end="")
            
            # label delimiter from main info
            print("├", end="") 
            for i in range(0, labelQuan):
                for v in range(0, ((longestItems[i]) + 2)):
                    print("─", end="")
                if i == (labelQuan - 1):
                    print("┤")
                else:
                    print("┼", end="")

            # main info
            for row in rows:
                print("│ ", end="")
                for i in range(0, labelQuan):
                    if len(str(row[i])) == longestItems[i]:
                        print(row[i], end="")
                        if i == (labelQuan - 1):
                            print(" │")
                        else:
                            print(" │ ", end="")
                    else:
                        neededSpaces = longestItems[i] - len(str(row[i]))
                        if neededSpaces % 2 == 0:
                            neededSpacesSides = int(neededSpaces / 2)
                            for v in range(0, neededSpacesSides): # +1 because we have default 1space buffer for longest
                                print(" ", end="")
                            print(row[i], end="")
                            for z in range(0, neededSpacesSides):
                                print(" ", end="")
                            if i == (labelQuan - 1):
                                print(" │")
                            else:
                                print(" │ ", end="")
                        else:
                            startSpaces = math.floor(neededSpaces / 2)
                            endSpaces = math.ceil(neededSpaces / 2)
                            for v in range(0, (int(startSpaces))):
                                print(" ", end="")
                            print(row[i], end="")
                            for z in range(0, (int(endSpaces))):
                                print(" ", end="")
                            if i == (labelQuan - 1):
                                print(" │")
                            else:
                                print(" │ ", end="")
            
            #bottom delimiter 
            print("└", end="") 
            for i in range(0, labelQuan):
                for v in range(0, ((longestItems[i]) + 2)):
                    print("─", end="")
                if i == (labelQuan - 1):
                    print("┘")
                else:
                    print("┴", end="") 

        else:
            labelQuan = len(labels)
            longestItems = [] # find longest items in each column, to line up spaces
            for i in range(0, labelQuan): 
                longestItem = len(str(labels[i]))
                for row in rows:
                    if len(str(row[i])) > longestItem:
                        longestItem = len(str(row[i]))
                longestItems.append(longestItem)

            # top delimiter
            print("┌", end="") 
            for i in range(0, labelQuan):
                for v in range(0, ((longestItems[i]) + 2)):
                    print("─", end="")
                if i == (labelQuan - 1):
                    print("┐")
                else:
                    print("┬", end="")
            
            # label headers
            print("│ ", end="") 
            for i in range(0, labelQuan):
                if len(str(labels[i])) == longestItems[i]:
                    print(labels[i], end="") 
                    if i == (labelQuan - 1):
                        print(" │")
                    else:
                        print(" │ ", end="")
                else:
                    neededSpaces = longestItems[i] - len(str(labels[i]))
                    print(labels[i], end="")
                    for v in range(-1, neededSpaces):
                        print(" ", end="")
                    if i == (labelQuan - 1):
                        print("│")
                    else:
                        print("│ ", end="")

            # label delimiter from main info
            print("├", end="") 
            for i in range(0, labelQuan):
                for v in range(0, ((longestItems[i]) + 2)):
                    print("─", end="")
                if i == (labelQuan - 1):
                    print("┤")
                else:
                    print("┼", end="")

            # main info
            for row in rows:
                print("│ ", end="")
                for i in range(0, labelQuan):
                    if len(str(row[i])) == longestItems[i]:
                        print(row[i], end="")
                        if i == (labelQuan - 1):
                            print(" │")
                        else:
                            print(" │ ", end="")
                    else:
                        neededSpaces = longestItems[i] - len(str(row[i]))
                        print(row[i], end="")
                        for v in range(-1, neededSpaces):
                            print(" ", end="")
                        if i == (labelQuan - 1):
                            print("│")
                        else:
                            print("│ ", end="")

            #bottom delimiter 
            print("└", end="") 
            for i in range(0, labelQuan):
                for v in range(0, ((longestItems[i]) + 2)):
                    print("─", end="")
                if i == (labelQuan - 1):
                    print("┘")
                else:
                    print("┴", end="")
