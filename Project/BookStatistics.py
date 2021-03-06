from Visitor import Visitor

class BookStatistics(Visitor):
    def __init__(self):
        self.obj = None

    def visit(self, obj):
        self.obj = obj
        if (str(type(obj)).split('.')[1].split("'")[0] == "Section"):
            self.obj.content = self.obj.title

    def printStatistics(self):
        stats = {}
        for elem in self.obj._children:
            obj_type = str(type(elem)).split('.')[1].split("'")[0]

            if (obj_type in stats):
                stats[obj_type] += 1
            else:
                stats[obj_type] = 1

        print(f"{self.obj.title}'s statistics: ")
        for key in stats:
            print(f"Number of {key}(s):  {stats[key]}");