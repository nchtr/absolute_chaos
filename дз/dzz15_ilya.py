class MainClass:
    def __init__(self, text):
        self.text_field = text

    def set_text(self, text=None):
        if text:
            self.text_field = text
        else:
            self.text_field = input("Enter text: ")


class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number_field = number
