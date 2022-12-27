from csv import DictReader
from csapat import Csapat
import datetime

class Csapatok:

    def __init__(self, fajlnev):
        self.__fajlnev = fajlnev
        self.__lista = []

        with open(self.__fajlnev, mode="r", encoding="utf-8") as fh:
            reader = DictReader(fh, delimiter=";")
            for data in reader:
                cs = Csapat(stadion=data['stadion'], varos=data['város'], csapatok_szama=data['csapatok száma'], elso_merkozes=data['elsõ mérkõzés'], utolso_merkozes=data['utolsó mérkõzés'])
                self.__lista.append(cs)

    def get_lista(self):
        return self.__lista

    def varosi_lista(self, varos):
        return [i for i in self.__lista if i.varos == varos]

    def elso_merkozes_honapja(self, honap):
        return [i for i in self.__lista if datetime.datetime.strptime(i.elso_merkozes, "%Y-%m-%d").month == honap]

    def elso_merkozes_datum_elott(self, datum):
        datum_obj = datetime.datetime.strptime(datum, "%Y-%m-%d")
        return [i for i in self.__lista if datetime.datetime.strptime(i.elso_merkozes, "%Y-%m-%d") < datum_obj]

    def utolso_merkozes_datum_utan(self, datum):
        datum_obj = datetime.datetime.strptime(datum, "%Y-%m-%d")
        return [i for i in self.__lista if datetime.datetime.strptime(i.utolso_merkozes, "%Y-%m-%d") >= datum_obj]
