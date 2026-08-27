#File Handling in python :
#In order to achive file handling in python we need to use a FILE OBJECT.

def write_patterns(filename):

    with open(filename, 'w') as f:
        
        f.write('Right angle triangle\n----------------------\n')
        for i in range(1, 6):
            line = str(i)* i
            f.write(line + '\n')    
        f.write('\n') 
            
        f.write('Left angle triangle\n----------------------\n')
        for i in range(1, 6):
            line = (" " * (5 - i)) + (str(i) * i)
            f.write(line + '\n')
        f.write('\n')
            
        f.write('Pyramid\n----------------------\n')
        for i in range(1, 6):
            line = (" " * (5 - i)) + (str(i) * (2 * i - 1))
            f.write(line + '\n')

def read_patterns(filename):
    with open(filename, 'r') as f:
        for i in f.readlines():
            print(i)

if __name__ == "__main__":

    filename = 'patterns.txt'
    write_patterns(filename)
    print('Patterns saved to file\n')
    read_patterns(filename)


def chrctscollower():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle characterslowercase-columnwise\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(j+97))
        f.write('\n')
    f.close()
    
def namerow():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle characterslowercase-rownwise\n")
    for i in range(0,len(name)):
        for j in range(0,i+1):
            f.write(name[i])
        f.write('\n')
    f.close()


def iratrowlow():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angle Triangle lower-row\n")
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.close()
    
def iratnamecol():
    f=open('pattern.txt','a+')
    f.write("Inversed Right angle Triangle characters-columnwise\n")
    for i in range(len(name),0,-1):
        for j in range(0,i):
            f.write(name[j])
        f.write('\n')
    f.close()
