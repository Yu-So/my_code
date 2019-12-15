with open('../untitled/example.txt', 'w') as txt_File:
    i=1
    while i<=100:
        txt_File.write(str(i))
        txt_File.write('\n')
        i=i+1

with open('../untitled/example.txt', 'r') as txt_File:
    for line in txt_File:
        print (line)




list = [1,2,3,45,45,7,8,5]
print (list)
list.reverse()
print (list)
list.append(789)
print (list)
list.extend([2345,4567,4578])
print (list)

print(list.count(45))

print (sum(list))
print (len(list))

a = {0, 1, 4, 81, 64, 64, 16, 64, 25, 36}
b = {0, 1, 4, 81, 64, 64, 16, 64, 25, 36}

def func1 ():
  print ("Hi JQ")

func1()