import base64


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./"+fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(imgPath):
    with open(imgPath, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


