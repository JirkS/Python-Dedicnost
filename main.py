# regex pro barvu HEX  a pro A-K a pro expiraci

class IkeaItem:
    def __init__(self, n_sh: float, n_st: str, n: str, p: float):
        self._num_shelf = n_sh
        self._num_street = n_st
        self._name = n
        self._price = p

    @property
    def num_shelf(self):
        return self._num_shelf

    @num_shelf.setter
    def num_shelf(self, x):
        if x < 1 or x > 100:
            raise Exception("Cislo regalu musi byt v rozmezi od 1 az po 100!")
        self._num_shelf = x

    @property
    def num_street(self):
        return self._num_street

    @num_street.setter
    def num_street(self, x):
        if len(x) != 1:
            raise Exception("Cislo ulicky musi byt jednoslovne a z abecedy!")
        self._num_street = x

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, x):
        if len(x) == 0:
            raise Exception("Nazev musi obsahovat alespon 1 znak!")
        self._name = x

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, x):
        if x < 0:
            raise Exception("Cena musi byt kladne cislo!")
        self._price = x

    def __str__(self):
        return "IkeaItem: number of shelf: " + str(self._num_shelf) + ", number of street: " + self._num_street + ", name: " + self._name + ", price: " + str(self._price)


class MeasureableIkeaItem:
    def __init__(self, h: float, w: float, l: float):
        self._height = h
        self._width = w
        self._length = l

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, x):
        if x < 0:
            raise Exception("Vyska musi byt kladna!")
        self._height = x

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, x):
        if x < 0:
            raise Exception("Sirka musi byt kladna!")
        self._width = x

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, x):
        if x < 0:
            raise Exception("Delka musi byt kladna!")
        self._length = x


class PlasticWasteIkeaItem:
    def __init__(self, w_o_p: float):
        self._weight_of_plastic = w_o_p

    @property
    def weight_of_plastic(self):
        return self._weight_of_plastic

    @weight_of_plastic.setter
    def weight_of_plastic(self, x):
        if x < 0:
            raise Exception("Vaah musi byt kladna!")
        self._weight_of_plastic = x

    def __str__(self):
        return "PlasticWasteIkeaItem: " + str(self._weight_of_plastic)


class LACK(IkeaItem, MeasureableIkeaItem):
    def __init__(self, h_c: str, n_sh: float, n_st: str, n: str, p: float, h: float, w: float, l: float):
        IkeaItem.__init__(self, n_sh, n_st, n, p)
        MeasureableIkeaItem.__init__(self, h, w, l)
        self._hex_color = h_c

    @property
    def hex_color(self):
        return self._hex_color

    @hex_color.setter
    def hex_color(self, x):
        if len(x) != 6:
            raise Exception("Barva musi obsahovat presne 6 znaku v hex tvaru!")
        self._hex_color = x


class SAMLA_BOX(IkeaItem, MeasureableIkeaItem, PlasticWasteIkeaItem):
    def __init__(self, v: float, n_sh: float, n_st: str, n: str, p: float, h: float, w: float, l: float, w_o_p: float):
        IkeaItem.__init__(self, n_sh, n_st, n, p)
        MeasureableIkeaItem.__init__(self, h, w, l)
        PlasticWasteIkeaItem.__init__(self, w_o_p)
        self._volume = v

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, x):
        if x < 0:
            raise Exception("Objem musi byt kladny!")
        self._volume = x


class SJORAPPORT(IkeaItem, PlasticWasteIkeaItem):
    def __init__(self, e: str, w: float, n_sh: float, n_st: str, n: str, p: float, w_o_p: float):
        IkeaItem.__init__(self, n_sh, n_st, n, p)
        PlasticWasteIkeaItem.__init__(self, w_o_p)
        self._expiration = e
        self._weight = w

    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, x):
        if len(x) == 0:
            raise Exception("Error!")
        self._expiration = x

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, x):
        if x < 0:
            raise Exception("Vaha musi byt kladna!")
        self._weight = x

    def __str__(self):
        return "SJORAPPORT: expiration: {}, weight: {}, ".format(self._expiration, self._weight)


try:
    s_m = SAMLA_BOX(12, 5, 9, "neco1", 1200, 12, 5, 6, 485)
    l = LACK("000000", 41, 5, "neco2", 500, 87, 56, 7)
    s = SJORAPPORT("2023-09-04", 85, 65, 85, "neco3", 899, 52)

    print(s)
except Exception as e:
    print(e)
