import SimpleCV

display = SimpleCV.Display() #crear la ventana para mostrar la imagen

cam = SimpleCV.Camera(0) # inicializar la camara

normaldisplay = True # opcion de mostrar solo un segmento de pantalla si es false

while display.isNotDone(): # ciclo hasta que detengamos el programa

	if display.mouseRight: # si el hacemos click derecho cambiar de modo

		normaldisplay = not(normaldisplay)

        	print "Modo de Ventana:", "Normal" if normaldisplay else "Segmentado"

    	img = cam.getImage().flipHorizontal() # obtenemos una imagen de la camara
	dist = img.colorDistance(SimpleCV.Color.BLACK).dilate(5) # separamos los colores que estamos obteniendo en la imagen
	segmented = dist.stretch(220,255) #tratamos de sacar los colores blancos
	blobs = segmented.findBlobs() #buscamos objetos o BLOBs en la imagen
	if blobs: #Si encontramos BLOBs
		circles = blobs.filter([b.isCircle(0.2) for b in blobs]) # filtramos unicamente los objetos con forma de circulo
		if circles:
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),SimpleCV.Color.BLUE,3) # dibujamos el circulo encontrado
		rect = blobs.filter([b.isRectangle(0.1) for b in blobs]) # filtramos por rectangulos
        	if rect:
            		x_position = rect[-1].x-rect[-1].width()/2 #obtenemos la posicion en x
            		y_position = rect[-1].y-rect[-1].height()/2 #obtenemos la posicion en y
            		img.drawRectangle(x_position, y_position, rect[-1].width(), rect[-1].height(),SimpleCV.Color.BLUE, 3 ) # dibujamos el rectangulo
            		
        #Lo siguiente que hacemos es el mismo procedimiento pero en vez de obtener objetos con colores claros obtendremos objetos con colores oscuros
	dist2 = img.colorDistance(SimpleCV.Color.WHITE).dilate(5)
	segmented2 = dist2.stretch(200,255) # tratamos de sacar los colores oscuros
	blobs2 = segmented2.findBlobs()
	if blobs2: # if blobs are found
		circles2 = blobs2.filter([b2.isCircle(0.2) for b2 in blobs2])
		if circles2:
			img.drawCircle((circles2[-1].x, circles2[-1].y), circles2[-1].radius(),SimpleCV.Color.RED,3)
		rect = blobs2.filter([b2.isRectangle(0.8) for b2 in blobs2])
        	if rect:
            		x_position = rect[-1].x-rect[-1].width()/2
            		y_position = rect[-1].y-rect[-1].height()/2
            		img.drawRectangle(x_position, y_position, rect[-1].width(), rect[-1].height(),SimpleCV.Color.RED, 3 )


	if normaldisplay: # si esta en modo normal
		img.show() # mostrar la imagen
	else: # modo segmentado
		segmented.show() # mostrar la imagen segmentada
