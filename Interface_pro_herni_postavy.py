class ZvysitelnaUrovenInterface:
    def zvysitUroven(self):
        raise NotImplemented()


class Bojovnik(ZvysitelnaUrovenInterface):
    def __init__(self, sila):
        if type(sila) is not int or sila < 0 or sila > 3:
            raise Exception("Sila bojovnika neni dostatecne dlouhe")

        self.sila = sila

    def zvysitUroven(self):
        self.sila += 1


class Mag(ZvysitelnaUrovenInterface):
    def __init__(self, bilaMagie, cernaMagie):
        if type(bilaMagie) is not bool:
            raise Exception("Bila magie musi byt True/False")
        if type(cernaMagie) is not bool:
            raise Exception("Cerna magie musi byt True/False")

        self.cernaMagie = cernaMagie
        self.bilaMagie = bilaMagie

    def zvysitUroven(self):
        self.novaMagie = True


try:
    bobik = Bojovnik(1)
    print(bobik.sila)
    bobik.zvysitUroven()
    print(bobik.sila)

    martina = Mag(True, False)
    martina.zvysitUroven()
    print(martina.novaMagie)
except Exception as e:
    print(e)
