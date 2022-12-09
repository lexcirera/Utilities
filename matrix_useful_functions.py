import numpy as np
def dilatation(M,i,a): #on fera attention à bien compter les lignes à partir de 0
    M[i] = [coeff * a for coeff in M[i]]
    return M

def permutation(M,i,j): #idem
    M[i], M[j] = M[j], M[i]
    return M

def transvection(M,i,j,a):
    M[i] = [M[i][k] + a * M[j][k] for k in range(len(M[i]))]
    return M

def pivot(M,k):
    m=abs(M[k][k])
    pivot_partiel=k
    for i in range (k+1,len(M)):
        if abs(M[k][pivot_partiel])>m:
            pivot_partiel=i
    return pivot_partiel #connaissant l'indice de la ligne on restitue celui de la colonne, on a ainsi la position sur la colonne (pivot_partiel) et sur la ligne (k)


def triangle(M):
    compteur_permutations=0 #on compte le nombre de permutations qui sera utile pour le calcul du determinant
    for i in range (len(M)):
        pivot_partiel=pivot(M,i) #ont trouve le pivot partiel pour chaque ligne
        if pivot_partiel!=i:
            permutation(M,i,pivot_partiel) #on effectue une permutation si nécessaire
            compteur_permutations+=1 #si il y a permutation on la comptabilise
        if M[i][i] != 0: #on vérifie qu'on ne divise pas par 0
            for j in range (i+1, len(M)):
                transvection(M,j,i,-M[j][i]/M[i][i])
    return M,compteur_permutations #on restitue la nouvelle matrice et le nb de permutations

def determinant(M):
    det=1 #on part du principe qu'il vaut 1 (élément neutre de la multiplication)
    M,nombre_permutations= triangle(M) #on récupère les valeurs de la fonctions d'avant ( la matrice triangulaire sup et le nombre de permutations
    for i in range (len(M)):
        det=det*M[i][i] #le det d'une matrice triangulaire sup est égal au produit des coeff diagonaux
    return (-1)**(nombre_permutations)*det #le signe du det varie selon le nomre de permutations




import matplotlib.pyplot as pl #importation de l bibliothèque pour le tracé
import math # importation de la bibliothèque pour les fonctions trigonométriques

L=4 #longueur du la queue
beta=0#valeur de départ de beta
valeur_max_beta=5 #valeur max de beta que l'on veut sur le graph
pas_de_variation=0.01 #écart entre chaque mesure de beta (ici tout les 0.01
Abscisses=[] #introduction de la liste abscisses pour le tracé
Ordonnées=[] #idem pour les ordonnées

def construction_Mm(beta): #j'introduis une fonction pour contruire Mm car plus simple pour la suite (question 8)
    return [[1,0,1,0],[0,1,0,1],[math.cosh(beta*L),math.sinh(beta*L),-math.cos(beta*L),-math.sin(beta*L)],[math.sinh(beta*L),math.cosh(beta*L),math.sin(beta*L),-math.cos(beta*L)]]

while beta<=valeur_max_beta:
    Mm=construction_Mm(beta) #construction de Mm en fonction de beta
    Abscisses.append(beta) #on récupère l'abscisse beta
    Ordonnées.append(determinant(Mm)) # et le déterminant en ordonnée
    beta+=pas_de_variation

pl.plot(Abscisses,Ordonnées,'r') #on fait le tracé et le 'r' pour mettre la courbe en rouge c'est plus joli :-)
pl.xlabel('Valeur de Beta') #on nomme l'axe des abscisses
pl.ylabel('Valeur du déterminant') #idem pour les ordonnées
pl.title("Evolution du déterminant en fonction de Beta") #un petit titre
pl.xlim(0,6) #limitation de l'axe des abscisses
pl.ylim(-50,50) #limitation de l'axe des ordonnées
pl.show() #enfin on montre le graph


def dichotomie(binf,bsup,err):
    if determinant(construction_Mm(binf))*determinant(construction_Mm(bsup))>0: #TVI pour être sur qu'une solution existe
        return 'Pas de solution dans l’intervalle de recherche' #on renvoit le message qu'il n'y a pas de solutions
    else:
        while abs(bsup-binf)>err: #on regarde à quelle précision on en est
            milieu=(binf+bsup)/2 #on construit le milieu de l'intervalle
            if determinant(construction_Mm(binf))*determinant(construction_Mm(milieu))<=0: #on regarde si le TVI est respecté
                bsup=milieu #si oui on changde la borne sup
            else:
                binf=milieu #sinon on change la borne inf
    return (binf+bsup)/2 #on renvoit la valeur approchée à err près

print(dichotomie(0,1,0.00001))

def fV(X,t):
    return [X[1],(X[1]+4)/t,X[3],X[3]/t] #pour les derivées du premier et troisième terme, on les a déjà dans X donc on ne fait que remplacer. Pour la deuxièeme et quatrième on se sert du taux d'accroissement et de zpoint(0) et tetapoint(0)


def resolutionEuler(fonction, CIni, tmin, tmax, n):
    Résolution=[] #liste des solutions
    Résolution.append(CIni) #on entre les condition initiale
    temps=tmin #on suppose tmin inférieur à tmax
    pas_temps=abs((tmax-tmin)/n) #on crée le pas de temps
    Vect_temps=0
    i=0 #on s'en sert pour récupérer les valeurs dans les listes
    while temps<tmax: #on va continuer d'incrémenter jusqu'à atteindre tmax
        Résolution.append(Résolution[i]+pas_temps*fonction(Résolution[i],temps)) #on ajoute la sol selon Euler
        if (Résolution[i]+pas_temps*fonction(Résolution[i],temps))-fonction(Résolution[i],temps)==0:
            Vect_temps=temps #on teste si cette valeur est sol de l'équa dif
        i+=1 #on incrémente i de 1 pour au tour suivant récupérer la valeur suivante dans la liste pour de nouveau faire Euler
        temps+=pas_temps #on incrémente le temps
    return Résolution , Vect_temps



def derivation(temps,liste):
    n=len(temps) #on recupère la longueur de la liste
    Der=[] #on crée une liste vide où l'on va par la suite mettre les valeurs dérivées
    Der.append((liste[1]-liste[0])/(temps[1]-temps[0])) #dérivée décentrée à droite pour la première valeur
    for i in range(1,n-1):
        Der.append((liste[i+1]-liste[i-1])/(temps[i+1]-temps[i-1])) #on fait une dérivée centrée du deuxième à l'avant   dernier terme
    Der.append((liste[n-1]-liste[n-2])/(temps[n-1]-temps[n-2])) #dérivée décentrée à gauche pour la dernière valeur



te=1.5*10**(-3) #donné par l'énoncé
def filtre(temps,liste,tf):
    n=len(liste)
    liste_filtrée=liste[0] #on suppose que la première valeur n'a pas besoin d'être filtrée
    for i in range (1,n): #on fait une boucle pour la deuxième à la nième valeur (la boucle s'arrète à n-1)
        liste_filtrée.append((te*liste[i]+tf*liste_filtrée[i-1])/(te+tf)) #on se sert de la question 15
    return liste_filtrée

def fV_exp(X,t):
    Xpoint=fV(X,t)
    return [Xpoint[1],Xpoint[1]/t ,Xpoint[3],Xpoint[3]/t] #le premier et troisième terme on les a directement dans Xpoint et on obtient les deux autre par dérivation milieu







