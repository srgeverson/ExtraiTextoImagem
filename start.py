import cv2
import pytesseract

print('Olá Python')

# image = cv2.imread("Thumbnail.jpg")
image = cv2.imread("p1.jpg")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(image, lang="por")

print(text)