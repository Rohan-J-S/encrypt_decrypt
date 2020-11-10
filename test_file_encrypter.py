text_file = input("enter file to be encrypted: ")
x = open(text_file,"r",)
text = x.readlines()

key = {'a':'h','b':'d','c':'s','d':'n','e':'a','f':'i','g':'q','h':'k','i':'e','j':'y','k':'u','l':'j','m':'o','n':'t','o':'c','p':'w','q':'w','r':'b','s':'r','t':'f','u':'l','v':'x','w':'p','x':'g','y':'z','z':'v',' ':' '}
for y in range(len(text)):
    s = ""
    for z in range(len(text[y])):
        if text[y][z] == "\n":
            break
        s += key[text[y][z]]
    text[y] = s


x.close()
y = open(text_file,"w+")
for z in text:
    y.write(z)
    y.write("\n")
y.close()
