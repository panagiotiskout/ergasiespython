import random

plat=input("Δώσε πλάτος ορθογωνίου για να ξεκινησούμε!-->")
platos=int(plat)
up=input("Δώσε και ύψος ορθογωνίου και είμαστε ετοιμοί!-->")
upsos=int(up)
x=platos*upsos
cnt=1
sos=0
while(cnt<=100):
        box=["S" for i in range(x)]
        for i in range(x//2):
            k=random.randint(0,x-1)
            box[k]="O"
        seira=0
        while(seira<upsos-1):
            #orizontios elegxos, den elegxw tin prwth kai teleutaia stili
            for i in range(1,platos-2):
                if box[seira*platos+i]=="O":
                    if box[seira*platos+i+1]=="S":
                        if box[seira*platos +i-1]=="S":
                            sos+=1
            seira+=1
        seira=1
        while(seira<upsos-2):
            #kathetos elegxos,den elegxw tin prwth k teleutaia grammi
            for i in range(0,platos-1):
                if box[seira*platos + i]=="O":
                    if box[seira*platos + i -platos]=="S":
                        if box[seira*platos+ 1 +platos]=="S":
                            sos+=1
            seira+=1
        seira=1
        while(seira<upsos-2):
            #diagwnios pros ta deksia elegxos,den elegxw 1h kai teleutaia stili kai grammi
            for i in range(1,platos-2):
                if box[seira*platos+i]=="O":
                    if box[seira*platos-platos+1]=="S":
                        if box[seira*platos+platos-1]=="S":
                            sos+=1
            seira+=1
        seira=1
        while(seira<upsos-2):
            #diagwnios pros ta aristera,den elegxw 1h kai teleutaia stili kai grammi
            for i in range(1,platos-2):
                if box[seira*platos+i]=="O":
                    if box[seira*platos+i+platos+1]=="S":
                        if box[seira*platos+i-platos-1]=="S":
                            sos+=1
            seira+=1
        cnt+=1
print("Ο μέσος όρος των SOS που δημιουργήθηκαν είναι-->",sos/100)