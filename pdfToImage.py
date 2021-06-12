from zipfile import ZipFile
import pdf2image

def pdfToImage(page_bytes):
    images = pdf2image.convert_from_bytes(page_bytes , dpi=350)

    for i, image in enumerate(images):
        fname = "image" + str(i) + ".png"
        imagesArray = []
        imagesArray.append(fname)

        image.save("C:\\Users\\Victo\\Documents\\Repositorios\\pdf-converter-api\\" + fname, "PNG")

    with ZipFile("Images.zip", 'w') as zipObj:
        for i, images in enumerate(images):
            zipObj.write("image" + str(i) + ".png") 
