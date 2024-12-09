# CORRECTION DU DEVOIR 2023/2024
# 				Harouna Goumbane (ISE ECO) et Moussa Dieme (ISE MATH)
# Une section de teste est inclu a la fin du code pour executer directement le code


# ---------------------------------- Notes generales -----------
# Nous ne proposerons pas un code typiquement pythonesque
# nous nous attacherons aux valeurs de notre cour 
# d'algorithmique,des concept tel que <<elif>>  et <<breack>>
# par exemple ne serons pas present dans notre code 

#-------------------------------------------------------------------

# ----------------- Exercice 1---------------------------------
# Sujet: algorithme permettant de décaler les valeurs nulles d'un tableau
#        vers la fin du tableau en gardant l'ordre des éléments 

#-------------------------
import math
import numpy as np
import os # pour la team windows
# -----------------------

def decalZerro(tab_list):
	"""
	prennd une liste et renvoi le resultat comme une liste
	"""
	if type(tab_list)is not list:raise TypeError("l'argument doit etre une liste")
	if (not all(isinstance(x,int) for x in tab_list) ):raise TypeError("ce n'est pas une liste d'entier")
	len_tab=len(tab_list)
	for i in range(len_tab-1):
		if tab_list[i]==0:
			y=tab_list[i]
			j=i+1
			while j<len_tab-1 and tab_list[j]==0:
				j+=1
			tab_list[i]=tab_list[j]
			tab_list[j]=y
	return tab_list

#-------------------------------------------------------------------

# ----------------- Exercice 2---------------------------------
# Sujet:Algorithme qui retourne le nombre de sous_séquences croissante d'un tableau
# ainsi que les indices de début et de fin de la plus longue sous-séquence
def sous_seq_crois(tab_list):
	"""
	prennd une liste et renvoi un tuple (nb_sous_sequ_croissant,(ind_deb_max,ind_fin_max))
	"""
	if type(tab_list)is not list:raise TypeError("l'argument doit etre une liste")
	if (not all(isinstance(x,int) for x in tab_list) ):raise TypeError("ce n'est pas une liste d'entier")
	len_tab=len(tab_list)
	debut=0
	fin=0
	nb_sousséquences=0
	l=0
	i=1
	while i <=len_tab-2:
		nb_sousséquences=nb_sousséquences+1
		j=i
		compteur=1
		while  j<=len_tab-2 and tab_list[j]<=tab_list[j+1]:
			compteur=compteur+1
			j+=1
		valeur= compteur
		if compteur>l:
			l=compteur
			debut=i
			fin=j
		i=i+valeur
	return (nb_sousséquences,(debut,fin))	

#-------------------------------------------------------------------

# ----------------- Exercice 3---------------------------------
# Sujet:1) algorithme permettant de calculer la valeur de l'expression donnée de sinus de x
# jusqu'au rang N ,lorsque x est proche de zéro
def puissance(x,n):
	res=1
	for i in range (n):
		res *=x
	return res
def factor(n):
	if n==0:
		return 1
	else:
		return factor(n-1)
def formule_sin(x,k):
	return puissance(-1,k)*puissance(x,2*k+1)/factor(2*k+1)

def approxim_sin_x(x,N):
	"""
	x reel proche de zero et N entier indice de la suite
	retourne U_N(x) ,approximation de math.sin(x) 
	"""
	res=0
	for i in range(N):
		res +=formule_sin(x,i)
	return res
#-------------------------------------------------------------------
# 2)Algorithme qui calcul le plus petit entier n 
# permettant d'obtenir une approximation de pi , a une précision donné 
############ petite precision :la convergence de la suite est assez lente:
############  resultat : cela donne l'impression d'une boucle infini
############  un conseil: prendre une precision faible 
def formule_pi(n):
	return (puissance(-1,n)/(2*n+1))

def approxim_pi_N(pi=math.pi,precision=puissance(10,-50),limite_boucle=40000):
	"""
	agrs :pi est une approximation de pi a une precision donnee
		  precision est la precision de l'aproximation
		  limite_boucle :pour eviter les boucles infini
	retourne le plus petit entier n tel que | U_n - pi|<= precision
			 si la limite_boucle est atteint:retourne None
	"""
	if precision>1:raise ValueError("precision non coherent") 
	if abs(pi-math.pi)>1:raise ValueError("approximation de pi non coherent")
	n=0
	somme_forume_pi=0
	while abs(somme_forume_pi -pi)>precision and n<=limite_boucle:
		somme_forume_pi += 4*formule_pi(n)
		n +=1
	if n==limite_boucle+1:
		return None
	else:
		return n

#-------------------------------------------------------------------

# ----------------- Exercice 4---------------------------------
# 1) algo qui calcule le reste de la division entiere entière par 10
def res_div_int(nb):
	"""
	renvoi le reste de la division entiere
	"""
	res=nb
	while res>=10:
		res -=10
	return res
# 2-1) calcul le nombre et la somme de chiffre qui compose un entier donné
def nb_chiffre_somme_chiffre(n):
	"""
	renvoi un tuple (nombre de chiffre, somme chiffre)
	"""
	nbr_chiffre=0
	somme_chiffre=0
	while n>0:
		nbr_chiffre +=1
		somme_chiffre += res_div_int(n)
		n=n - res_div_int(n)
		n=n/10
	return (nbr_chiffre,somme_chiffre)
def teste_divisible_9(n):
	"""
	premet de savoir si n est divisible par 9 ou pas
	"""
	# un nombre est divisible par 9 lorsque la somme de ses chiffres est un multiple de 9
	somme_chiffre=nb_chiffre_somme_chiffre(n)[1]
			# on a bessoin du reste de la division euclidienne de somme_chiffre par 9
			# astuce: on vas soustraire 9 jusqu'a ce que on soit dans [0,9]
			# mathematiquement new_var = 9*p + somme_chiffre
			# mathematiquement c'est la division euclidienne donc 
			# somme_chiffre divisible par 9 Sssi new_var  == 9
	while somme_chiffre>9:
		somme_chiffre -=9
	return somme_chiffre==9

#-------------------------------------------------------------------

# ----------------- Exercice 5---------------------------------
# 1) la moyenne de chaque élève et met les resultats dans un tableau tab_moy
def tab_moy_eleve(tab_notes):
	"""
	args: tab_notes tabeleau 2D  des notes 
		   Eleve sur les lignes et matieres sur les colonnes
		  renvoi un tab_moy contenant la moyenne de chaque eleve
	"""
	n,m=tab_notes.shape
	tab_moy=np.zeros(n)
	for i in range(n): # i em eleve
		sommecoef=0
		N=0
		coef=1
		for j in range(m): # j em matiere
			coef=sommecoef+j+1 # matiere indice j  a pour coef 1+2+...+j+1
			tab_moy[i] +=coef*tab_notes[i,j]
			sommecoef=sommecoef+coef
			N +=sommecoef
		tab_moy[i]=tab_moy[i]/N
	return tab_moy
#2) le nombre d'élève avec une moyenne inférieur à celle de la classe
	# on commence par calculer la moyenne de la classe
def verif_eleve_low_moy_class(tab_notes):
	"""
	agrs : tab_notes tableau 2D des notes des eleves
		retourne le nombre d'eleve avec une moyenne inferieure ou egale a celle de la classe
	"""
	tab_moy=tab_moy_eleve(tab_notes)
	moy_classe=sum(tab_moy)/len(tab_moy)
	nb=sum(tab_moy<=moy_classe) # True == 1 et False ==0 ,c'est l'astuce avec sum
	return nb

if __name__=="__main__":
    print("********************* Exercice 1 *********************************")
    tab=[1,2,4,8,0,0,2,0,7]
    print(tab)
    print("apres decallage : \n")
    print(decalZerro(tab))
    print("# ----------------- Exercice 2---------------------------------")
    print(tab)
    print(f"ce tableau   a {sous_seq_crois(tab)[0]} sous sequence\
          croissante et le max des sequ a pour coordonne ({sous_seq_crois(tab)[1]}) ")
    print("# ----------------- Exercice 3---------------------------------")
    print("x=0.001")
    print(f"valeur usuel de sin(x) = {math.sin(0.001)}")
    print(f"valeur de notre fonction pour N=200: {approxim_sin_x(0.001,200)}")
    print("valeur usuel de pi: {math.pi}")
    print("precision =0.01")
    print(f"le plus petit entier est {approxim_pi_N(precision=0.01)}")
    print("# ----------------- Exercice 4---------------------------------")
    print(f"nombre de chiffre de 425: {nb_chiffre_somme_chiffre(425)[0]}")
    print(f"sommes des chiffre de 425: {nb_chiffre_somme_chiffre(425)[1]}")
    print(f"18 est t-il divisible par 9: {teste_divisible_9(18)}")
    print(f"90001 est t-il divisible par 9: {teste_divisible_9(90001)}")
    print("# ----------------- Exercice 5---------------------------------")
    tab_notes=np.random.randint(0,21, size=(11, 6))
    print("les notes des eleves :")
    print(tab_notes)
    print("La moyenne de chaque eleve :")
    print(tab_moy_eleve(tab_notes))
    print("nombre d'eleve avec une moyenne <= moyenne classe")
    print(verif_eleve_low_moy_class(tab_notes))
    print("***************************************************************")
    print("Fin du programme")
    os.system(" pause")
    
    
    
          
















