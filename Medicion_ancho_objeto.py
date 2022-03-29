#Importar las librerías por utilizar
import os
from skimage import io
from skimage.filters import threshold_otsu,sobel

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

#Conversión de distancia en pixeles a distancia real
def size_obj(image,work_dist):
    sensor_size_h = 4.2
    focal_dist = 3.31
    pxl_dist = dist_pxl(image)
    sens_res_h = sensor_size_h/320
    dist_sens = pxl_dist*sens_res_h
    width = work_dist*dist_sens/focal_dist
    return round(width,1)

#Medicion_ancho_objeto
def medir_ancho_objeto(Data):
    work_dist = Data[1]
    image = Data[0]
    img_sobel = sobel(image)
    img_bin = binarize(img_sobel)
    width = size_obj(img_bin,work_dist)
    return width

def main():
    #Obtener la direccion de las imagenes
    path = os.getcwd()
    IMG_ROSA= io.imread(path +r'\IMG_ROSA.jpeg',True)
    IMG_AZUL= io.imread(path +r'\IMG_AZUL.jpeg',True)
    IMG_VERDE= io.imread(path +r'\IMG_VERDE.jpeg',True)
    #Tuplas de datos para la Aplicación
    Data_Rosa = (IMG_ROSA,119)
    Data_Azul = (IMG_AZUL,139)
    Data_Verde = (IMG_VERDE,118)
    #Calculo de los anchos
    ancho_rosa = medir_ancho_objeto(Data_Rosa)
    ancho_azul = medir_ancho_objeto(Data_Azul)
    ancho_verde = medir_ancho_objeto(Data_Verde)
    val_real = [52,87,56]
    error = [round(abs(ancho_rosa-val_real[0])/ancho_rosa*100,2),
            round(abs(ancho_azul-val_real[1])/ancho_azul*100,2),
            round(abs(ancho_verde-val_real[2])/ancho_verde*100,2)]
    print(f"El ancho de las diferentes imagenes es:")
    print(f"Imagen   Ancho (mm)     Error (%)")
    print(f"Rosa     {ancho_rosa}           {error[0]}")
    print(f"Azul     {ancho_azul}           {error[1]}")
    print(f"Verde    {ancho_verde}           {error[2]}")

if __name__ == "__main__": main()