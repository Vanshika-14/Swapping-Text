def swapFileData():
   file1 = input("Enter name of original file: ")
   file2 = input("Enter name of file to be swapped: ")

   with open(file1, 'r') as a:
      dataA = a.read()
   with open(file2, 'r') as b:
      dataB = b.read()

   with open(file1, 'w') as a:
      a.write(dataB)
   with open(file2, 'w') as b:
      b.write(dataA)

swapFileData()