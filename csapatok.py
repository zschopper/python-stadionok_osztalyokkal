from csv import DictReader
from csapat import Csapat

class Csapatok:

    def __init__(self, fajlnev):
        self.__fajlnev = fajlnev
        self.__lista = []
        self.betolt()

    def betolt(self):
        self.__lista = []
        with open(self.__fajlnev, mode="r", encoding="utf-8") as fh:
            reader = DictReader(fh, delimiter=";")
            for data in reader:
                cs = Csapat(stadion=data['stadion'], varos=data['város'], csapatok_szama=int(data['csapatok száma']), elso_merkozes=data['elsõ mérkõzés'], utolso_merkozes=data['utolsó mérkõzés'])
                self.__lista.append(cs)

    def get_lista(self):
        return self.__lista

    def csapatok_szama(self):
        return len(self.__lista)

    def stadionok_szama_a_megadott_varosban(self, varos):
        db = 0
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].varos == varos:
                db += 1
            i += 1
        return db

    def csapatok_szama_a_megadott_varosban(self, varos):
        db = 0
        i = 0
        while i < len(self.__lista):
            csapat = self.__lista[i]
            if csapat.varos == varos:
                db += csapat.csapatok_szama
            i += 1
        return db

    def elso_merkozesek_szama_a_megadott_datum_elott(self, datum):
        db = 0
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].elso_merkozes < datum:
                db += 1
            i += 1
        return db

    def utolso_merkozesek_szama_a_megadott_datum_elott(self, datum):
        db = 0
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].utolso_merkozes < datum:
                db += 1
            i += 1
        return db
