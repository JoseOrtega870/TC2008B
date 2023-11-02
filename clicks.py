# importing the module
import cv2
import numpy
# function to display the coordinates of
# of the points clicked on the image
nodos = []

def click_event(event, x, y, flags, params):
    escala = 497/175
    x2 = round(x / escala, 2)
    y2 = round(y / escala, 2)
    
    
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:

        # displaying the coordinates
        # on the Shell

        print(x2, ' ', y2)
        par=(x2,y2)
        nodos.append(par)
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x2) + ',' +
                    str(y2), (x, y), font,
                    1, (255, 255, 255), 2)
        cv2.imshow('image', img)

    
        
        

# driver function
if __name__ == "__main__":

    # reading the image
    img = cv2.imread('Custom Size.png', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
    

print("Agrega conexiones ('n' para terminar)")
n = len(nodos)
A=numpy.zeros((n,n))
escape = ''
while escape!='n':
    nodoInicial=int(input("Nodo inicial: "))-1
    nodoFinal=int(input("Nodo final: "))-1
    distanciaX=(nodos[nodoFinal][1]-nodos[nodoInicial][0])**2
    distanciaY=(nodos[nodoFinal][1]-nodos[nodoInicial][1])**2
    distancia=round((distanciaX+distanciaY)**.5,2)
    A[nodoInicial,nodoFinal]=distancia
    A[nodoFinal,nodoInicial]=distancia
    escape = input("continuar?")
print(A)