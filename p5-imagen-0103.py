import cv2
# leer la imagen con cv2 = computer vision
img = cv2.imread('golden retriever.jpg')
#determinar el tipo de imagen numpy.ndarray
print(type(img))
#mostrar pixeles (554, 554, 3)
print(img.shape)
#mostrando imagen en ventana barra de titulo
cv2.imshow('golden retriver 0103', img)
## tiempo de espera 
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()