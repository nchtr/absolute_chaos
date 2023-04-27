class MainClass:
    def __init__(self, text):
        self.text = text
    
    def set_text(self, text=None):
        if text is not None:
            self.text = text
        else:
            self.text = ""

class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number
