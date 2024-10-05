img = '10'
file = '/content/drive/MyDrive/PC/TIPE spé/Images/' + str(img) + '.jpg'  # on importe notre image
Original = cv2.imread(file)
plt.imshow(Original)
# quand on aura toutes nos images d'affilees, on pourra faire :
# nb_image = 10
# Original = []
# for i in range(nb_image) :
# file = '/content/drive/MyDrive/TIPE spé/IMG_'+str(i)+'.jpg'
# Original.append(cv2.imread(file))


# Redimensionnage
Taille = 400
CoordX = 1860  # point de depart
CoordY = 1200  # point de depart
Original_resized = Original[CoordY:CoordY + Taille // 2, CoordX:CoordX + Taille]
plt.imshow(Original_resized)

teinte = 50
plt.imshow(NoirBlanc(Original_resized, teinte), cmap='gray', vmin=0, vmax=255)
plt.imshow(Contour(NoirBlanc(Original_resized, teinte)), cmap="gray")
X, Y = Courbe(Contour(NoirBlanc(Original_resized, teinte)))
plt.figure()
plt.grid()
plt.plot(X, Y)

courbe(Original_resized)

# Et on laisse la magie faire !
# print("A l'instant initiale, on aura :")
courbe(Original_resized)
print("L'angle est de", round(Angle(Original_resized), 0), '°')
