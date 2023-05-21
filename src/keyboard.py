from electronics_shop_project.src.item import Item


class MixinLang:
    def __init__(self):
        self.__language = "EN"


    @property
    def language(self):
        return self.__language


    def change_lang(self):
        self.__language = ({"RU", "EN"} - {self.__language}).pop()
        return self


class KeyBoard(Item, MixinLang):
    def __init__(self, *args):
        super().__init__(*args)
        MixinLang.__init__(self)

