import cv2
# Leer la imagen con cv2 = computer vision
img = cv2.imread('perrillo.webp')
# Determinar el tipo de imagen numpy.ndarray
print(type(img))
# Mostrar imagen en ventana barra de titulo perro 0113
cv2.imshow('perrillo 0113', img)
# Tiempo de espera
cv2.waitKey(0)
# Deestruir todas las ventanas
cv2.destroyAllWindows()