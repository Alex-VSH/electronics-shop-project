from src.item import Item


class MixinLog:

    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"


class Keyboard(Item, MixinLog):
    pass
