from google.cloud import vision
import os, io, types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Pavan/Project/GCP/client123-1c6497d3482c.json"

client = vision.ImageAnnotatorClient()
path = "Payment.png"
with io.open(path, 'rb') as image_file:
        content = image_file.read()
image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)
document = response.full_text_annotati
