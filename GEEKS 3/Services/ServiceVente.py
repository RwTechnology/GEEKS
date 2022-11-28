from Controller.ControllerStation import ControllerStation


class ServiceVente:

    prix_gazoline = 250
    prix_diesel = 353

    ctrl_st = ControllerStation()
    list_station = ctrl_st.list_station

    def calculer_prix_total_vente(self, type_essence, quantite):
        if type_essence == "Gazoline":
            return quantite * self.prix_gazoline
        else:
            return quantite * self.prix_diesel
