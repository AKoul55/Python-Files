# 1
f = open('poems.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not prsent")
    f.close()


# 2

def game():
    return 84784

score = game()
with open("highscore.txt") as f:
    highscorestr = f.read()
if highscorestr =='':
        with open("highscore.txt", "w") as f:
            f.write(str(score))
elif int(highscorestr)<score :
    with open("highscore.txt", "w") as f:
        f.write(str(score))    


 # 3
words =["mc","nonsense", "stokes"]

with open("sample.txt") as f:
     content = f.read()

for word in words:          
  content = content.replace(word, "$^&^*$#")
  with open("sample.txt", "w") as f:
          f.write(content)

# 4
with open ("log.txt") as f:
     content = f.read()
if "python" in content.lower():
   print("yes python is present")   
else:
     print("no python is not prsent")

# 5
content = True
i= 1
with open ("log.txt") as f:
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print(f"yes python is present in line {i}") 
        i+=1  


# 6
with open ("this.txt") as f:
    content = f.read()
    with open("copy.txt", 'w') as f:
        f.write(content) 

# 7
file1 = "log.txt"
file2 = "this.txt"

with open(file1) as f:
    f1 = f.read()

    with open (file2) as f:
        f2 = f.read()

        if f1 == f2:
            print("files are identical")
        else:
            print("files are not identical")

# 8
filename = "sample.txt"
with open(filename, "w") as f:
    f.write("")            

# 9
import os
oldname = "sample2.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()
  
with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)    