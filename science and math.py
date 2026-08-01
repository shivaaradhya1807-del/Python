import os
with open("science.txt","r") as f:
    for line in f:
        print(line.strip())

print()

with open("math.txt","r") as f:
    for line in f:
        words=line.split()
        print(len(words),"words ->",line.strip())

print()

if os.path.exists("all notes writing.txt"):
    print("file exists")

else :
    print("file does not exist")

content=""

with open("science.txt","r") as f:
    content+="-----science notes ------"
    content+=f.read()+"/n"

with open("math.txt","r") as f:
    content+="-----math notes ------"
    content+=f.read()+"/n"

with open("all notes writing.txt","w") as f:
    f.write(content)
print(" saved to all notes writing. txt")