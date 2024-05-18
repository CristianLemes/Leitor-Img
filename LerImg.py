# opencv
import cv2
import pytesseract

# Lendo a imagem com OpenCV
img = cv2.imread("imgteste.jpeg")

# Apontando para o executável do pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

resultado = pytesseract.image_to_string(img)

print(resultado)
