
class TableOfContents():
    def __init__(self,obj):
        self.obj = obj
        self.toc = ""


    def generateToC(self,obj,k=1):
        prefix = k * "-"
        try:
            if(obj._children):
                self.toc += f"{prefix} {obj.title} \n"
                for elem in obj._children:
                    self.generateToC(elem,k+1)

        except:
            self.toc += f"{prefix} {obj.content} \n"


    def getToc(self):
        self.generateToC(self.obj)
        return self.toc