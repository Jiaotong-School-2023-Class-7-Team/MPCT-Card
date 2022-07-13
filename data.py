import sqlite3
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMessageBox
from PIL import Image, ImageQt

class Data:
    quesTypes = ["CHOICE", "FILL", "MULTI_CHOICE", "CHOICE_FILL"]
    cardsTypes = ["MATH", "PHYSICS", "CHEMISTRY", "TOOLS"]

    def __init__(self):
        self.db = sqlite3.connect("db/cards.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM `cards`")
        self.cards = self.cursor.fetchall()
        self.cardsData = self.getCardsData()
        self.cursor.execute("SELECT * FROM `questions`")
        self.ques = self.cursor.fetchall()
        self.quesData = self.getCardsData()

    def getCardsData(self):
        cards = list()
        for i in self.cards:
            name = i[0]
            link = i[1]
            support_level = i[2]
            image_name = i[3]
            try:
                with open(link, "r", encoding="utf-8") as file:
                    thing = file.read()
            except Exception as e:
                QMessageBox.warning(None, "Error", str(e), QMessageBox.Ok)
                thing = "（加载失败）"
            bs = BeautifulSoup(thing, "html.parser")
            text_element = bs.find("p", id="text")
            text = text_element.text.replace(" ", "").replace("\n", "")
            info_element = bs.find("p", id="info")
            info = info_element.text.replace(" ", "")
            type_element = bs.find("p", id="type")
            type_ = type_element.text.replace(" ", "")
            try:
                image_file = Image.open(image_name)
                image = ImageQt.ImageQt(image_file)
            except Exception as e:
                QMessageBox.warning(None, "Error", str(e), QMessageBox.Ok)
                image = ImageQt.ImageQt(Image.open("img/dataNotLoaded.png"))
            cards.append([name, text, info, support_level, type_, image])
        return cards

    def getQuesData(self):
        ques = list()
        for i in self.ques:
            thing = i[0]
            type_ = i[1]
            assert type_ in self.quesTypes


if __name__ == "__main__":
    d = Data()
    for i in d.cardsData:
        for j in i:
            print(j)
        print("\n")
