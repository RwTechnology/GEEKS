class Approvisionnement:

    def __init__(self, id, type_essence, quantite, date):
        self._id = id
        self._type_essence = type_essence
        self._quantite = quantite
        self._date = date

    def get_id(self):
        return self._id

    def get_type_essence(self):
        return self._type_essence

    def get_quantite(self):
        return self._quantite

    def get_date(self):
        return self._date

    def set_quantite(self, quantite):
        self._quantite = quantite






