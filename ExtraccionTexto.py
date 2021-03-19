from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError)
import os 

#Ruta del OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta de los pdfs
entries = os.scandir('/Users/Mateo/Documents/OCR/resoluciones')
  

for entry in entries:
    ''' 
    Part #1 : Convertir pdfs a imagenes
    '''
    PDF_file = entry.name
    print(PDF_file)
    # Arreglo de paginas ... convertidas a bytes
    pages = convert_from_bytes(open('/Users/Mateo/Documents/OCR/resoluciones/'+PDF_file,'rb').read())

    # Contador para recorrer arreglo
    image_counter = 1
    
    for page in pages: 
        filename = "page_"+str(image_counter)+".jpg"
        # Guardo la imagen en el sistema
        page.save('/Users/Mateo/Documents/OCR/corpus/'+filename, 'JPEG') 
    
        image_counter = image_counter + 1
    
    ''' 
    Parte #2 - OCR 
    '''
    # Variable to get count of total number of pages 
    filelimit = image_counter-1
    
    # Creacion del archivo plano de salida
    outfile = PDF_file.replace("pdf","txt")
       
    # el texto de todas las imagenes es añadido al archivo plano 
    f = open('/Users/Mateo/Documents/OCR/corpus/'+outfile,"a") 
    
    # ciclo para todas las paginas 
    for i in range(1, filelimit + 1): 
        filename = '/Users/Mateo/Documents/OCR/corpus/page_'+str(i)+'.jpg'    
        # usamos pytesseract para convertir la imagen a texto 
        text = str(((pytesseract.image_to_string(Image.open(filename))))) 
        ### Eliminar esta linea para seguir jugando, con los mismos pdfs
        os.remove(filename)
        text = text.replace('-\n', '')     
        # escribo el texto en el archivo plano 
        f.write(text) 

    f.close()