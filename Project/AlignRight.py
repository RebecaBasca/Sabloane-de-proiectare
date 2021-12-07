from AlignStrategy import AlignStrategy

class AlignRight(AlignStrategy):
    def render(self, paragraph):
        return f"{paragraph : >30}"


