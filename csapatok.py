from csv import DictReader
from csapat import Csapat
import datetime

class Csapatok:

    def __init__(self, fajlnev):
        self.fajlnev = fajlnev
        self.lista = []

        with open(self.fajlnev, "r", encoding="utf-8") as fh:
            reader = DictReader(fh, delimiter=";")
            for data in reader:
                cs = Csapat(stadion=data['stadion'], varos=data['város'], csapatok_szama=data['csapatok száma'], elso_merkozes=data['elsõ mérkõzés'], utolso_merkozes=data['utolsó mérkõzés'])
                self.lista.append(cs)

    def get_lista(self):
        return self.lista

    def varosi_lista(self, varos):
        return [i for i in self.lista if i.varos == varos]

    def elso_merkozes_honapja(self, honap):
        if 1 <= honap <= 12:
            return [i for i in self.lista if datetime.datetime.strptime(i.elso_merkozes, "%Y-%m-%d").month == honap]
        return []
