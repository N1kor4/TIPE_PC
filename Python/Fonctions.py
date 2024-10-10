import matplotlib.pyplot as plt
import numpy as np
import cv2


# Contraste / Couleurs
def NoirBlanc(Image, teinte):
    Original_2 = []  # creation nouvelle image
    for j in Image:  # on prend une colone
        lst = []  # on crée la future ligne
        for i in j:  # parcours des différents éléments de la colone (donc une ligne)
            teinte_de_gris = i[0] * 0.2125 + i[1] * 0.7174 + i[
                2] * 0.0721  # on remplace RGB par une teinte de gris (0,255)
            if teinte_de_gris < teinte:  # si la teinte de gris est trop foncée, on la remplace par du noir
                teinte_de_gris = 0
            lst.append(teinte_de_gris)  # on met dans la ligne les pixels en teinte gris ou noir
        Original_2.append(lst)  # on ajoute la ligne a la j ieme colone
    return Original_2


# plt.imshow(NoirBlanc(Original_resized),cmap='gray', vmin=0, vmax=255)

def Contour(Image):
    Courbe = [[] for k in range(len(Image))]  # creation de la nouvelle matrice
    for i in range(len(Image[0])):  # on parcours d'abord les lignes
        n = 0
        for j in range(len(Image)):  # puis les colones
            if Image[j - 3][i] == 0 and Image[j][
                i] > 0:  # si sur la colone j et j-3, sur une meme ligne, il y a des pts noirs...
                Courbe[n].append(0)  # on ajoute tous les points qui pourraient faire parti de la courbe
            else:
                Courbe[n].append(255)  # et sinon, on laisse en blanc
            n += 1
    return Courbe


# plt.imshow(Contour(NoirBlanc(Original_resized)), cmap="gray")

def Courbe(Image):
    Image = [[Image[j][i] for j in range(len(Image))] for i in range(len(Image[0]) - 1, -1, -1)]
    # on tourne la matrice parce au'on va parcourir l'image ligne par ligne mais comme on veut reperer le 1er point
    # sur chaque colone, on tourne la matrice de 90 degre
    X, Y = [], []  # on cree la liste de nos coordonnees
    coordX = -1  # on commence a l'origine x=0
    for i in Image:  # on parcourt les colones (la ce sont les lignes de l'image d'au dessus)
        coordX += 1  # on incremente X
        lst = []
        coordY = -1
        for j in i:  # on parcourt les lignes
            coordY += 1
            if j == 0:  # on prend tous les pts noirs
                lst.append(coordY)
        if len(lst) != 0:  # si il y a des pts pts noirs sur une lignes
            coordY = lst[0]  # on prend le 1er de ces elements
            X.append(coordX)
            Y.append(coordY)
    return X, Y


# X,Y = Courbe(Contour(NoirBlanc(Original_resized))) plt.figure() plt.grid() plt.plot(X,Y) #la courbe est a l'envers,
# normal, j'ai tourne la matrice dans le "mauvais sens" (c'est bien le bon sens mais faudrait changer jsp quoi mais
# apres ca marche plus)

def coeff_angle1(X, Y):
    # Support et recherche du pts d'intersection
    err = 1
    nb = len(X) // 3  # nombre de pts mais on restreint l'intervalle de recherche
    # for i in range(5,nb) :
    # [a1,b1] = np.polyfit(X[0:i],Y[0:i],1)  # a et b sont les coefficients de la régression linéaire : y=ax+b
    # y = a1*X[i] + b1
    # nb2 = i - 5
    # if Y[i] - y > err : #on cherche le point a partir duquel l'erreur entre la regression et la courbe est trop elevee
    #   break #on sort de la boucle

    # ca marche pas dcp j'ai trouve le point tout seul :( enft normalement, ca marche mais le support est pas plat
    # avec 26
    nb = 90
    [a1, b1] = np.polyfit(X[0:nb], Y[0:nb], 1)
    Y_reg1 = [a1 * X[i] + b1 for i in range(len(X))]  # on a notre petite courbe

    # Goutte
    nb2 = nb
    nb3 = nb2 + 10  # nombre de points utilises pour la reg de la courbe, il ne faut pas en prendre bcp sinon on
    # risque de couper l'arc que forme la goutte
    [a2, b2] = np.polyfit(X[nb2:nb3], Y[nb2:nb3], 1)  # a et b sont les coefficients de la régression linéaire : y=ax+b
    Y_reg2 = [a2 * X[i] + b2 for i in range(len(X))]

    # point d'intersection
    x0 = (b2 - b1) / (a1 - a2)  # c'est le coef entre les deux courbes
    y0 = a1 * x0 + b1  # on prend le pts de coef lineaire x0 en 1

    return Y_reg1, Y_reg2, x0, y0


def coeff_angle2(X, Y):
    # faut mettre la meme qu'en haut mais en parcourant la courbe dans le sens oppose
    return None


def courbe(Image):
    X, Y = Courbe(Contour(NoirBlanc(Image, teinte)))
    Y_reg1, Y_reg2, x0, y0 = coeff_angle1(X, Y)
    plt.figure()
    plt.grid()
    plt.plot(X, Y)
    plt.plot(X, Y_reg1, 'k')
    plt.plot(X, Y_reg2, 'r')
    plt.scatter(x0, y0, color='g')
    plt.ylim([400, 0])
    plt.show()


# https://fr.moonbooks.org/Articles/Comment-tracer-un-angle-entre-deux-droites-avec-matplotlib-de-python-/

def Angle(Image):
    position = 100
    X, Y = Courbe(Contour(NoirBlanc(Image, teinte)))
    Y_reg1, Y_reg2, x0, y0 = coeff_angle1(X, Y)
    num = Y_reg1[position] - x0
    den = np.sqrt((Y_reg1[position] - x0) ** 2 + (Y_reg2[position] - y0) ** 2)
    theta = np.arccos(num / den)
    if not Y_reg2[position] - y0 >= 0: theta = 2 * np.pi - theta
    theta = abs(theta * 360 / (2 * np.pi) - 180)
    return theta
