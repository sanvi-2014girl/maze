def findpath(rows,cols,path):
    if rows == 1 and cols ==1:
        print(path)
        return
    if cols>1:
        findpath(rows,cols-1,path+'r')
    if rows>1:
        findpath(rows-1,cols,path+'d')
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))
print("Here are all the ways you can move")
findpath(rows,cols,"")