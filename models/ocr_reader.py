import easyocr

class OcrReader:
    def __init__(selfself):
        self.reader = easyocr.Reader(['en'])

    def read_text(selfself, image):
        return self.reader.readtext(image)
