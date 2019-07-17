import cv2

arqCasc = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)

#Instancia o uso da webcam
webcam = cv2.VideoCapture(0)  

while True:
    #Captura a imagem da webcam
    s, imagem = webcam.read()
    #Espelha a imagem
    imagem = cv2.flip(imagem,180) 

    faces = faceCascade.detectMultiScale(
        imagem,
        minNeighbors=5,
        minSize=(80, 80),
	maxSize=(200,200)
    )

    #Desenha um retângulo em torno das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (255,0,0), 2)

    #Mostra a imagem capturada
    cv2.imshow('Video', imagem) 

    #Para o codigo e fecha a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Dispensa o uso da webcam
webcam.release()
#Fecha todas a janelas abertas
cv2.destroyAllWindows() 
