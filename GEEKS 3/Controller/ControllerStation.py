from Model.Station import Station
from Services.ServiceStation import ServiceStation
from Services.TextColors import TextColors


class ControllerStation:
    # dictionnaire differentes stations
    lalue, tabarre, clercine, petion_ville = {}, {}, {}, {}

    # liste des dictionnaire station
    list_station = [lalue, tabarre, clercine, petion_ville]

    serviceSt = ServiceStation()
    color = TextColors()

    def enregistrer_station(self, station, type_essence, capacite):
        station_object = Station(station, type_essence, capacite, 0.0, 0.0, 0.0)
        if station == "lalue":
            self.lalue.update({type_essence: station_object})
        elif station == "tabarre":
            self.tabarre.update({type_essence: station_object})
        elif station == "clercine":
            self.clercine.update({type_essence: station_object})
        else:
            self.petion_ville.update({type_essence: station_object})
        print(f"{self.color.SUCCES}enregistrement avec succes ✅{self.color.ENDBG}")


    def modifier_quantite_gallon(self, station, type_essence, new_capacite):
        if station == "lalue":
            self.serviceSt.auxilliare_modifier_quantite_gallon(self.lalue, type_essence, new_capacite)
        elif station == "tabarre":
            self.serviceSt.auxilliare_modifier_quantite_gallon(self.tabarre, type_essence, new_capacite)
        elif station == "clercine":
            self.serviceSt.auxilliare_modifier_quantite_gallon(self.clercine, type_essence, new_capacite)
        else:
            self.serviceSt.auxilliare_modifier_quantite_gallon(self.petion_ville, type_essence, new_capacite)

    def afficher_stations(self):
        if self.serviceSt.if_list_station_vide(self.list_station):
            for i in self.list_station:
                n = 0
                nom_station = None
                if i:
                    check = True
                    n = 1
                    for value in i.values():
                        if nom_station != value.get_nom_station():
                            print(f"\n{self.color.GREEN}---------------- {value.get_nom_station()} ----------------\n{self.color.END}")
                            nom_station = value.get_nom_station()

                        # update pourcentage utilisation
                        pourc_ut = self.serviceSt.calcul_pourc_ut(value.get_quantite_commandee(),value.get_quantite_disponible())
                        value.set_pourcentage_utilisation(pourc_ut)

                        # affichage
                        print(f"{self.color.GREEN}{self.color.BOLD}Reservoir  : no {n}{self.color.END}")
                        n = n + 1
                        print(f"{self.color.BLUE} Nom Station        :  {value.get_nom_station()}")
                        print(f" Type Essence       :  {value.get_type_essence()}")
                        print(f" Capacite           :  {value.get_capacite()} Gallons")
                        print(f" % d'utilisation    :  {value.get_pourcentage_utilisation()} %")
                        print(f" Quantite disponible :  {value.get_quantite_disponible()} Gallons\n{self.color.END}")
        else:
            print(f"{self.color.RED}\nDesole, aucune station n'est encore enregistree 🚫! {self.color.END}")
