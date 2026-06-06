Array = list(map(int,input("Enter the elements: ").split()))

key = int(input("Enter the key to search: "))

for i in range(len(Array)):
  if Array[i]==key:
    print("search successfull.")
    break
else:
  print("Search unsuccessfull.")