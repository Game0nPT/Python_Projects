import cv2
import numpy as np


color = cv2.imread('cat.jpg')
cv2.imshow("Original", color)

#exercico 1
# Using cv2.cvtColor() method 
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imshow("exercicio 1", gray)

# exercico 2
# Using cv2.GaussianBlur() 
# (17,17)-> Definem o tamanho do kernel(tipo se a matriz é de 3x3 tem de ser esse o valor a usar)  
#       Caso aumente o vaslor: mais desfocada a imagem
gauss =cv2.GaussianBlur(gray, (17,17), 3.7) 
cv2.imshow("exercicio 2", gauss)

#exercico 3
# Using cv2.medianBlur() method (bom metodo para remover ...(nao ouvi)) 
#Kernel size para ambas as direções, que neste caso é 3
#                           |
median=cv2.medianBlur(gray, 3)
cv2.imshow("exercicio 3", median)

#exercico 4
# Using cv2.flip() method 
# Use Flip code 0 to flip vertically 
#Case 1 the flip is horizontali
fliping=cv2.flip(gray, 0)
cv2.imshow("exercicio 4", fliping)


#exercico 5

#Este valor serve para mexer com o brilho no caso de o valor ser mais baixo
#a imagem sera mais escura
Z = 70

#Pra obter o numero de rows and cols
#                   Posição 0-numero de rows  
#                   Psoção 1- numero de cols

rows,cols=gray.shape[0:2]
print("rows=", rows)
print("cols=", cols)

#cria uma imagem vazia para nao destruir a original, neste caso chamada "brightness";
#np- numpy library; 
# np.zeros()->contruindo um novo array , e todos os elementos do array preenchidos 
#(cont) a zeros do tamanho do array da imagem originbal "gray";
#np.uitn8->tipo de elementos do array;
brightness = np.zeros((gray.shape), np.uint8)

for i in range(rows):       #scan the rows
    for j in range(cols):   #scan the cols
        v = gray.item(i,j)  #metodo que extrai o valor de um pixel

        #exerc6
        if v+Z > 255:
            o = 255
        elif v+Z < 0:
            o = 0
        else:
            o = v+Z
        
        #OR
        #o = np.clip(v+Z, 0, 255)
        
        brightness.itemset((i,j), o )
cv2.imshow("exercicio 5 e 6", brightness)

#exercicio7
not_flip_xx_axis = np.zeros((gray.shape), np.uint8)
#index da ultima linha
i = rows - 1
#para cada loop estamos a retirar uma linha da imagem original(gray) 
for line in gray:
    not_flip_xx_axis[i] = line
    i = i-1

cv2.imshow("exercicio 7", not_flip_xx_axis)


#exercicio8
#not_flip_yy_axis = np.zeros((gray.shape), np.uint8)
#index da ultima linha
#i = cols - 1
#for nao da para retirar colunas so linhas
# transp... 
#for colum in gray:
#    not_flip_yy_axis[i] = colum
#    i = i-1

#cv2.imshow("exercicio 8", not_flip_yy_axis)


#exercicio9
#extrair uma zona da imagem usandol sliders
#o primeiro 20 sao as coordenadas do canto superior esquerdo
#o 160 e a largura
#A segunda zon aé ate onde queremos remover
roi = gray[20:20+160, 30:30+160]
cv2.imshow("exercicio 9", roi)


#exerc10
#frequencias altas: zonas onde temos transicoes altas entre pixels de cores
#1º argumeto : imagem a ser processada
#2º argumento: numero de bits por cada elemento (escolhe se 8 porque é o que normalmente se usa)
lap = cv2.Laplacian(gray, 8)
cv2.imshow("exercicio 10", lap)


#exerc11
#copiar tanto a forma como a unfomação de cada pixel
cir = np.copy(gray)
#tranformsar uma imagem(cada pixel é formada em um unico bit), em uma
#(cont)imagem colorida em que cada pixel é formada por 3 pixels
#A imagem continua a ser cinzenta
#                               |-> tipo de conversão a fazer(conzento para bgr)
cir = cv2.cvtColor(cir, cv2.COLOR_GRAY2BGR)
#
cir = cv2.circle(cir, (int(cols/2), int(rows/2)), 50, (0,255,0), 4)
cv2.imshow("exercicio 11", cir)



#exerc12
#
sobel1 = [ [1.0, 2.0 ,1.0], 
            [0.0, 0.0 ,0.0], 
            [-1.0, -2.0, -1.0]  ]
#python nao e capaz de manipular listas em termos matematicos
#(cont)entao é necessario transformar esta lista em um array
k = np.array(sobel1)
#
sob = cv2.filter2D(gray, 8, k)
cv2.imshow("exercicio 12", sob)

#exerc13
def noise(img, n):
   
    nRows = img.shape[0]
    nCols = img.shape[1]
    
    r = np.random.randint(nRows, size=n)
    c = np.random.randint(nCols, size=n)

    for i in range(n):
        #
        img.itemset((r[i],c[i]), 255 )


noiseImg = gray.copy()
noise(noiseImg, 10000)  # add noise
cv2.imshow("noise", noiseImg)

filt = cv2.medianBlur(noiseImg, 3) # remove noise
cv2.imshow("w/noise", filt)
filt=cv2.medianBlur(noiseImg,3)
cv2.imshow("filt",filt)

cv2.waitKey()
