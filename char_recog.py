client = vision.ImageAnnotatorClient()
with io.open(image_file, 'rb') as image_file:
        content = image_file.read()
image = types.Image(content=content)
response = client.document_text_detection(image=image)
document = response.full_text_annotati
djdd
