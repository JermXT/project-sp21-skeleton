import random
def main(v):
    f = open('input'+str(v)+".in", 'w')
    f.write(str(v)+'\n')
    for i in range(v):
        for j in range(v):
            if(i != j and i < j):
                f.write(str(i) + " " + str(j) + " " + str(random.randint(1,99)) + "\n")
    
    
    f.close()



main(30)
main(50)
main(100)
