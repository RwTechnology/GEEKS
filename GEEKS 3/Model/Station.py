class Station:

    def __init__(self, nom_station, type_essence, capacite, pourcentage_utilisation, quantite_disponible,
                 qte_commandee):
        self._nom_station = nom_station
        self._type_essence = type_essence
        self._capacite = capacite
        self._pourcentage_utilisation = pourcentage_utilisation
        self._quantite_disponible = quantite_disponible
        self._qte_commandee = qte_commandee

    def get_nom_station(self):
        return self._nom_station

    def get_type_essence(self):
        return self._type_essence

    def get_capacite(self):
        return self._capacite

    def get_pourcentage_utilisation(self):
        return self._pourcentage_utilisation

    def get_quantite_disponible(self):
        return self._quantite_disponible

    def get_quantite_commandee(self):
        return self._qte_commandee

    def set_capacite(self, capacite):
        self._capacite = capacite

    def set_pourcentage_utilisation(self, pourcentage_utilisation):
        self._pourcentage_utilisation = pourcentage_utilisation

    def set_quantite_disponible(self, quantite_disponible):
        self._quantite_disponible = quantite_disponible

    def set_qte_commandee(self, qte_commandee):
        self._qte_commandee = qte_commandee
