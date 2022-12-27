class Csapat:
    def __init__(self, stadion, varos, csapatok_szama, elso_merkozes, utolso_merkozes):
        self.stadion = stadion
        self.varos = varos
        self.csapatok_szama = csapatok_szama
        self.elso_merkozes = elso_merkozes
        self.utolso_merkozes = utolso_merkozes

    def __str__(self):
        return f"stadion: {self.stadion:<40}  város: {self.varos:<16}  csapatok száma: {self.csapatok_szama:>3}  elsõ mérkõzés: {self.elso_merkozes:<14}  utolsó mérkõzés: {self.utolso_merkozes:<14}"
