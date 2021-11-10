from Element import Element
from Image import Image

class ImageProxy(Element):
    def __init__(self, url):
        self.url = url
        self.realImage = None

    def add(self, component):
        pass;

    def remove(self, component):
        pass

    def print(self):
        self.loadImage()
        self.realImage.print()
        pass

    def loadImage(self):
        if(self.realImage == None):
            self.realImage = Image(self.url)