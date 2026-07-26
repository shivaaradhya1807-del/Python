#read(n)

file=open("student.txt","r")
print(file.read(20))
file.close()

#readline()
file=open("student.txt","r")
line=file.readline()
file.close()

print('total lines :-', len(line))

for i in range(len(line)):
    print(i + 1, '->', line[i].strip())

#loop

file=open("student.txt","r")
for line in file:
    print(line.strip())
file.close()