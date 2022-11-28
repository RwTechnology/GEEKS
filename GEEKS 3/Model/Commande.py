class Commande:

    def __init__(self, id,type_essence, quantite, date_commande, etat):
        self._id = id
        self._type_essence = type_essence
        self._quantite = quantite
        self._date_commande = date_commande
        self._etat = etat

    def get_id(self):
        return self._id

    def get_type_essence(self):
        return self._type_essence

    def get_quantite(self):
        return self._quantite

    def get_date_commande(self):
        return self._date_commande

    def get_etat(self):
        return self._etat

    def set_quantite(self, quantite):
        self._quantite = quantite

    def set_etat(self, etat):
        self._etat = etat





