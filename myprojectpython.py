#veuillez utiliser le compilateur  https://codeboot.org/py/ puisque des  images et quelques éléments  sont pré-enregistrer la bas merci beaucoup :D
def init():
    nom=" document.querySelector('#main')"
    html='''
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    h5
    { margin-top: 30px;
    margin-bottom: 60px;}
    #ligne
    {display:flex;
    }
    #button {
     margin-right:70px;
     margin-top:20px;
     border-radius: 10px;
     padding: 10px 3px;
     background-color: white;
     font-family: 'Courier New', Courier, monospace;
     border-color: whitesmoke;}
    table#jeu { 
    display:flex
    border-spacing:10px;
    border-collapse: separate;
    display: inline-block;
    }
    #mmm
    {display:flex;}


   table#jeu td {
    font-size:20px
    background-color: #white;
    border-color: white;
    width: 60px;
    height: 80px;
    background-position: center;
    background-size: cover;
    }

 </style>
 <meta charset="UTF-8">
 <title>Test8</title>
 <script type="text/python" src="test8.py"></script>
 </head>
 
 <body >
 <div id="ligne">
    <div>
        <button id=button onclick="lancerPartie()" >
            Nouvelle <br>random </button>
      </div>
       <table id="jeu">
    <tbody id="table">
           <tr>
          <td onclick="click(0)" id="carte0"><img src="http://codeboot.org/cards/back.svg"></td>
          <td></td>
           </tr>
            </table>
          </tbody>

    <div>
     <table id="jeu">
    <tbody id="table">
    <tr>
<td onclick="click(1)" id="carte1"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(2)" id="carte2"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(3)" id="carte3"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(4)" id="carte4"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(5)" id="carte5"><img src=http://codeboot.org/cards/empty.svg></td>
<td id="s1"></td>
          </tr>
          <tr>
<td onclick="click(6)" id="carte6"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(7)" id="carte7"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(8)" id="carte8"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(9)" id="carte9"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(10)" id="carte10"><img src="http://codeboot.org/cards/empty.svg"></td>
<td  id="s2"></td>
          </tr>
          <tr>
<td onclick="click(11)" id="carte11"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(12)" id="carte12"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(13)" id="carte13"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(14)" id="carte14"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(15)" id="carte15"><img src=http://codeboot.org/cards/empty.svg></td>
            <td  id="s3"></td>
          </tr>
          <tr>
<td onclick="click(16)" id="carte16"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(17)" id="carte17"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(18)" id="carte18"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(19)" id="carte19"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(20)" id="carte20"><img src=http://codeboot.org/cards/empty.svg></td>
            <td  id="s4"></td>
          </tr>
<tr>
<td onclick="click(21)" id="carte21"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(22)" id="carte22"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(23)" id="carte23"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(24)" id="carte24"><img src=http://codeboot.org/cards/empty.svg></td>
<td onclick="click(25)" id="carte25"><img src=http://codeboot.org/cards/empty.svg></td>
<td  id="s5"></td>

          </tr>
            <tr>
            <td  id="m1"></td>
            <td  id="m2"></td>
            <td id="m3"></td>
            <td id="m4"></td>
            <td  id="m0"></td>
            <td  id="m6">0</td>
          </tr>
          </tbody>

        
          </div>
          </table>
      </div>
      </body >
      '''
    nom.innerHTML=html
grille=["cards/AH.svg","cards/AC.svg","cards/AS.svg","cards/AD.svg",
            "cards/2H.svg","cards/2C.svg","cards/2S.svg","cards/2D.svg",
            "cards/3H.svg","cards/3C.svg","cards/3S.svg","cards/3D.svg",
            "cards/4H.svg","cards/4C.svg","cards/4S.svg","cards/4D.svg",
            "cards/5H.svg","cards/5C.svg","cards/5S.svg","cards/5D.svg",
            "cards/6H.svg","cards/6C.svg","cards/6S.svg","cards/6D.svg",
            "cards/7H.svg","cards/7C.svg","cards/7S.svg","cards/7D.svg",
            "cards/8H.svg","cards/8C.svg","cards/8S.svg","cards/8D.svg",
            "cards/9H.svg","cards/9C.svg","cards/9S.svg","cards/9D.svg",
            "cards/10H.svg","cards/10C.svg","cards/10S.svg","cards/10D.svg",
            "cards/JH.svg","cards/JC.svg","cards/JS.svg","cards/JD.svg",
            "cards/QH.svg","cards/QC.svg","cards/QS.svg","cards/QD.svg",
            "cards/KH.svg","cards/KC.svg","cards/KS.svg","cards/KD.svg",
            "cards/empty.svg"]
nvPaqueCarte=grille.copy()

def click(i):#procédure qui place les cartes et donnent le score
    global tempCarte
    global nCarte
    s=1
    j=str(i)
    txtB='<img src="http://codeboot.org/cards/back.svg">'
    txt2="<img src=http://codeboot.org/"+nvPaqueCarte[nCarte]+">"
    if i==0 :
         txt="<img src=http://codeboot.org/"+nvPaqueCarte[nCarte]+">"
         document.querySelector("#carte0").innerHTML=txt
         selectionner(0)
         tempCarte=-1
    elif not vide(j) and tempCarte==-1:
        selectionner(j)
        déselectionner(0)
        tempCarte=i
    
    else:
         if tempCarte>0:
            swipe(i,tempCarte)
            doPoint()
            document.querySelector("#m"+"6").innerHTML=str(doPoint())
            déselectionner(tempCarte)
            tempCarte=-1
         elif nCarte>=0 and (document.querySelector("#carte0").innerHTML!=txtB):    
            document.querySelector("#carte"+j).innerHTML=txt2
            element=document.querySelector("#carte"+"0")
            element.setAttribute('style','background-color: normal')
            element=document.querySelector("#carte"+"0")
            element.innerHTML='<img src="http://codeboot.org/cards/back.svg">'
            doPoint()
            document.querySelector("#m"+"6").innerHTML=str(doPoint())
            nCarte+=1
            tempCarte=-1
            fin(doPoint())
init()
def fin(x):#fonction qui affiche le score lors de la fin du programme
     for i in range(1,26):
        j=str(i)
        if nCarte!=25:
            return 
     prompt("votre score est de "+str(x))

def randomi(tableau):#fonction qui mélanges les cases 
    for i in range(len(tableau)):
        
        x=int(random()*(len(tableau)-i))
        c=tableau[x]
        tableau[x]=tableau[~i]
        tableau[~i]=c
    return(tableau)
randomi(nvPaqueCarte)
nCarte=0
tempCarte=0

def pointH(i):#fonction qui calcul tous les points des mains horizentale 
    point=pointage(localiser(mainH(i)))
    if point==0:
        document.querySelector("#s"+conv(i)).innerHTML=""
    else:    
        document.querySelector("#s"+conv(i)).innerHTML=str(point)
    return point

def pointV(i):  #fonction qui calcul tous les points des mains verticales
    point=pointage(localiser(mainV(i)))
    if point==0:
        document.querySelector("#m"+str(i%5)).innerHTML=""
    else:
        document.querySelector("#m"+str(i%5)).innerHTML=str(point)
    return point

def selectionner(i):#fct qui sélectionne une case donner 
    i=str(i)
    element=document.querySelector("#carte"+i)
    return element.setAttribute('style', 'background-color: lime')

def déselectionner(i):#fct qui déselectionne une case 
    i=str(i)
    element=document.querySelector("#carte"+i)
    return element.setAttribute('style', 'background-color: normal')

def vide(i):#fct qui nous donnes true si la case est vide sinon, false
    i=str(i)
    print(générer(52))
    element=document.querySelector("#carte"+i)
    if ((element.innerHTML)!='<img src="http://codeboot.org/cards/empty.svg">'):
            return (False)
    else: return(True)
    
def swipe(j,i):#fonction qui échange deux cases du tableaux
    j=str(j)
    i=str(i)
    element=document.querySelector("#carte"+j)
    x=(document.querySelector("#carte"+j).innerHTML)
    (element.innerHTML)=(document.querySelector("#carte"+i).innerHTML)
    (document.querySelector("#carte"+i).innerHTML)=x


    
def lancerPartie():#fonction qui initialise la partie 
    global nvPaqueCarte
    nvPaquecarte=(randomi(nvPaqueCarte))
    init()

def pointage(t):#fonction qui calcule les points 
    point=0
    t=trie(t)

    if len(t)==5:
        for i in range (len(t)-1):
            if t[i]%4==t[i+1]%4 and (t[i]+4)//4==t[i+1]//4 and(point!=15 and point!=20) :
                point=75
                if t[i]in [45,46,47,48]:
                    point=100
            elif (t[i])%4==t[i+1]%4 and (point!=15):
                        point=20
            elif  (t[i]+4)//4==t[i+1]//4 and (point!=20):
                point=15    
            else:
                point=0
                break
    if (point!=0):return point    
    for i in range (len(t)):  
        for j in range (i+1,len(t)):
            if t[i]==52:
                break
            elif t[i]//4==t[j]//4 and point==2:
                    point=5 
            elif t[i]//4==t[j]//4 and point==5:
                    point=10
            elif t[i]//4==t[j]//4 and  point==0:
                    point=2
            elif t[i]//4==t[j]//4 and point==10:
                    point=25
            elif t[i]//4==t[j]//4 and point==25:
                    point=50
    return point

def conv(x):#fonction qui donne le  chiffre a partir de son nombre 
            #dans la grille 
    return str((math.ceil(x/5)))
 
def mainH(j):#fonction qui retourne une main horizentale avec un des
             #numéro d'un des cases 
    i=j
    mainn=[]
    if (j)%5==0:
        for i in range(5):
            mainn.append(j)
            j-=1
        return((mainn))    
    else:
        while ((j%5)!=0 and j!=0):
            mainn.append(j)
            j-=1
        while ((i%5)!=0 and i!=0):
            i+=1
            mainn.append(i)
    return((mainn))

def mainV(j):#fonction qui retourne une main verticale avec les numéros 
             #des cases
    mainn=[]
    i=j
    while j not in [-4,-3,-2,-1,0]:
        mainn.append(j) 
        j-=5

    while i not in [21,22,23,24,25]:
        i+=5
        mainn.append(i)
    return((mainn))
        


def localiser(t):#fonction qui localise les chiffres du premier tab dans le 
                 #2 éme tab 
    tab=[]
    for i in range(len(t)): 
        tab.append(grille.index(gen(t[i])))
    return (list(filter(lambda x : x!=52,tab)))

def générer(i):#fonction qui génere  la carte de la grille 
    return "<img src=http://codeboot.org/"+grille[i]+">"

def généreN(num):#fonction qui génere  la carte de la grille 
    num=num.upper()
    return "<img src=http://codeboot.org/cards/"+num+".svg>"
   
def  gen(j):#fonction qui génere  la carte d'une case 
    numberCarte=""
    i=str(j)
    carte=(document.querySelector("#carte"+i).innerHTML)
    for i in range (carte.rfind("/")-5,carte.find(">")-1):
                    numberCarte+=carte[i]
        
    return numberCarte

def doPoint():#fonction qui calcul les points et retourne le totale 
      total=0
      s=1
      for it in range(1,6):
           total+=pointV(it)
           total+=pointH(s)
           s+=5
      return total    

def trie(t):#fonction qui trie un tableau 
    test = True
    while test:
        test = False
        for i in range(len(t)-1):
            if t[i] > t[i+1]:
                temp = t[i]
                t[i] = t[i+1]
                t[i+1] = temp
                test = True
    return(t) 
def test():
    assert(pointage ([1,2,12,16,20]))==2
    assert(pointage ([1,8,12,13,27]))==2
    assert(pointage ([1,8,13,27,2]))==2
    assert(pointage ([1,36,12,16,20]))==0
    assert(pointage ([2,3,12,13,20]))==5
    assert(pointage ([20,2,12,3,13]))==5
    assert(pointage ([20,12,2,3,13]))==5
    assert(pointage ([2,3,1,13,20]))==10
    assert(pointage ([13,20,2,3,1]))==10
    assert(pointage ([2,13,20,3,1]))==10
    assert(pointage ([9,12,17,21,26]))==15
    assert(pointage ([17,9,21,26,12]))==15
    assert(pointage ([17,9,0,26,12]))==0
    assert(pointage ([5,17,21,33,41]))==20
    assert(pointage ([17,5,41,33,21]))==20
    assert((pointage ([4,17,33,41,37])))==0
    assert(pointage ([2,3,12,13,14]))==25
    assert(pointage ([12,2,13,14,3]))==25
    assert(pointage ([12,13,14,2,3]))==25
    assert(pointage ([12,0,50,40,4]))==0
    assert(pointage ([4,5,6,20,7]))==50
    assert(pointage ([22,23,21,20]))==50
    assert(pointage ([4,8,12,16,20]))==75
    assert(pointage ([16,8,12,4,20]))==75
    assert((pointage ([16,1,12,4,20])))==0
    assert(pointage ([51,47,43,39,35]))==100
    assert(pointage ([35,39,43,47,51]))==100
    assert(pointage ([35,39,43,47,0]))==0
    
    assert (conv(3))=="1"
    assert (conv(6))=="2"
    assert (conv(27))=="6"
    assert (conv((51)))=="11"
    
    assert(mainH(2))==[2, 1, 3, 4, 5]
    assert(mainH(5))==[5, 4, 3, 2, 1]
    assert(mainH(4))==[4, 3, 2, 1, 5]
    assert(mainH(25))==[25, 24, 23, 22, 21]
    assert(mainH(1))==[1, 2, 3, 4, 5]
    assert (mainH(25))==[25, 24, 23, 22, 21]
    
    assert (mainV(1))==[1, 6, 11, 16, 21]
    assert (mainV(11))==[11, 6, 1, 16, 21]
    assert (mainV(7))==[7, 2, 12, 17, 22]
    assert (mainV(25))==[25, 20, 15, 10, 5]
    
    assert(générer(5))=="<img src=http://codeboot.org/cards/2C.svg>"
    assert (générer(48))=="<img src=http://codeboot.org/cards/KH.svg>"
    assert (générer(21))=="<img src=http://codeboot.org/cards/6C.svg>"
  
    assert (généreN("ac"))=="<img src=http://codeboot.org/cards/AC.svg>"
    assert (généreN("AC"))=="<img src=http://codeboot.org/cards/AC.svg>"
    assert (généreN("7s"))=="<img src=http://codeboot.org/cards/7S.svg>"
    assert (généreN("6h"))=="<img src=http://codeboot.org/cards/6H.svg>"
    assert  (générer(52))=="<img src=http://codeboot.org/cards/empty.svg>"
    

    
test()
