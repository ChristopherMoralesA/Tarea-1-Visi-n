#Importar las librerías por utilizar
import os
from skimage import io
from skimage.filters import threshold_otsu

#Obtener la direccion de las imagenes
path = os.getcwd()
IMG_ROSA= io.imread(path +r'\IMG_ROSA.jpeg',True)
IMG_AZUL= io.imread(path +r'\IMG_AZUL.jpeg',True)
IMG_AMARILLA= io.imread(path +r'\IMG_AMARILLA.jpeg',True)
IMG_VERDE= io.imread(path +r'\IMG_VERDE.jpeg',True)

#Tuplas de datos para la Aplicación
Data_Rosa = (IMG_ROSA,128)
Data_Azul = (IMG_AZUL,157)
Data_Amarilla = (IMG_AMARILLA,120)
Data_Verde = (IMG_VERDE,136)

#Binarización de las Imagenes
def binarize(image,thresh=0):
    if thresh==0:
        thresh = threshold_otsu(image)
    binary = image > thresh
    return binary

#Calculo del ancho del objeto en pixeles
def dist_pxl(image):
    v,h = image.shape
    c1 = 0
    c2 = 0
    found = False
    for col in range(h):
        for row in range(v):
            if found == False and image[row][col] == True:
                c1 = col
                found = True
                break
        if found == True:
            break
    found = False
    for col in range(1,h):
        for row in range(0,v):
            if found == False and image[row][-col] == True:
                c2 = h-col
                found = True
                break
        if found == True:
            break
    if found == True:
        return c2-c1+1
    else:
        return 0



