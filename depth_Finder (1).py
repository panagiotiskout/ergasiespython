def split(word):
    return [char for char in word]

counter = 0
max = 0
try:
 file = input("give the name of file")
 with open(file) as f:
     flat_list = [word for line in f for word in line.split()]
 for i in flat_list:
     list_of_chars = split(i)

     for i in list_of_chars:
         if i == "{" or i == "[":
             counter += 1
         elif i == "}" or i == "]":
             counter -= 1
         if(counter > max):
             max = counter
 if len(list_of_chars) == 2:
     print("Max depth is: 0")
 else:
     print("Max depth is: "+str(max))
except:
    print("Wrong File path!")
