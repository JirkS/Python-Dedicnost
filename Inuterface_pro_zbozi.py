class VazitelneInterface:
    def get_vaha_v_kg(self, vaha: float):
        return vaha/1000

    def get_cena_za_kg(self, x: float):
        return x


class KusoveInterface:
    def get_pocet_kusu_v_baleni(self, x: float):
        return x

    def get_cena_za_kus(self, x: float):
        return x

    def get_cena_za_baleni(self, x: float):
        return x


class ZlevnitelneInterface :
    def set_sleva(self, x: float):
        self.sleva = x

    def get_cena_po_sleve(self, cena: float):
        return cena - (cena * self.sleva)
