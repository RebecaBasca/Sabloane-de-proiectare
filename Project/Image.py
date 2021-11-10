from Element import Element
import time

class Image(Element):
    def __init__(self, url):
        self.url = url
        time.sleep(5)

    def add(self, component):
        pass;

    def remove(self, component):
        pass;

    def print(self):
        print("Image with url:", self.url)

