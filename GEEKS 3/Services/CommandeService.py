from Controller.ControllerStation import ControllerStation
from Services.ServiceStation import ServiceStation


class CommandeService:

    list_station = ControllerStation().list_station
    srv_station = ServiceStation()

    @staticmethod
    def gerer_etat_commande(commande_list, type_essence):
        if commande_list:
            for i in commande_list:
                if i.get_type_essence() == type_essence and type(i.get_type_essence()) == str:
                    i.set_etat('P')
                else:
                    if i.get_type_essence() == type_essence:
                        i.set_etat(['P', 'P'])
            return 'N'
        else:
            return 'N'


    def gerer_quantite_commande(self, type_essence):
        if type(type_essence) == str:
            if type_essence == 'Gazoline':
                return 1.25 * self.srv_station.total_gal_gaz_manquant(self.list_station)
            else:
                return 1.10 * self.srv_station.total_gal_dies_manquant(self.list_station)
        else:
            qte_gal_gaz = 1.25 * self.srv_station.total_gal_gaz_manquant(self.list_station)
            qte_gal_dies = 1.10 * self.srv_station.total_gal_dies_manquant(self.list_station)
            return [qte_gal_gaz, qte_gal_dies]



