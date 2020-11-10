text_file = input("enter file to be encrypted: ")
x = open(text_file,"r",)
text = x.readlines()

key = {"a":"h"}
for y in range(len(text)):
    s = ""
    for z in range(len(text[y])):
        if text[y][z] == "\n":
            break
        s += key[text[y][z]]
    text[y] = s
print (text)

x.close()
y = open(text_file,"w+")
for z in text:
    y.write(z)
    y.write("\n")
y.close()
