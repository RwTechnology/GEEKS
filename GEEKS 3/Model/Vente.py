class Vente:

    def __init__(self, id, nom_station, type_essence, quantite, date_vente):
        self._id = id
        self._nom_station = nom_station
        self._type_essence = type_essence
        self._quantite = quantite
        self._date_vente = date_vente

    def get_id(self):
        return self._id

    def get_nom_station(self):
        return self._nom_station

    def get_type_essence(self):
        return self._type_essence

    def get_quantite(self):
        return self._quantite

    def get_date_vente(self):
        return self._date_vente
