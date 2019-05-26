from random import shuffle


liste = "amazing gorgeous stunning bold tremendous greatest fantastic phenomenal \
         ambitious exciting outstanding \
         fantastic best massive incredible spectacular cool".upper().split()

shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM ",end ='')
        print()
    el1 = liste.pop()
    el2 = liste.pop()
    print("{} SPAM,{} SPAM".format(el1, el2))
    print()