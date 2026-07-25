file=open("bucketlist.txt","w")
file.write("1. visit Eiffel tower \n")
file.write("2.learn to play guitar \n")
file.write("3.code my own game\n")
file.close()
print("bucket list saved to bucketlist.txt")

file=open("bucketlist.txt","r")
content=file.read()
print("===== BUCKET LIST =====")
print(content)
file.close()

file= open("bucketlist.txt","r")
lines=file.readlines()
print(f"you have {len(lines)} items in your bucket list.")
file.close()

file=open("bucketlist.txt","a")
file.write("4. go to japan \n")
file.write("5. goto USA \n")
file.close()

file= open("bucketlist.txt","r")
print("====new bucket list ===")
print(file.read())
file.close




