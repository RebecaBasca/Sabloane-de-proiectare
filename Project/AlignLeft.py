from AlignStrategy import AlignStrategy

class AlignLeft(AlignStrategy):
    def render(self, paragraph):
        return f"{paragraph : <30}"