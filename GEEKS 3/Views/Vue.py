from Services.Menu import Menu
from Services.ServiceStation import ServiceStation
from Controller.ControllerStation import ControllerStation
from Controller.ControllerCommande import CommandeController
from Controller.ApprovisionnementController import ApprovisionnementController
from Controller.ControllerVente import ControllerVente
from Services.TextColors import TextColors


class Vue:
    menu = Menu()
    serviceSt = ServiceStation()
    ctrlSt = ControllerStation()
    ctrlcmd = CommandeController()
    ctrlAp = ApprovisionnementController()
    ctrlV = ControllerVente()
    color = TextColors()

    def main(self):
        while True:
            match self.menu.menu_principal():
                # GESTION STATION
                case 1:
                    while True:
                        match self.menu.menu_gestion_station():
                            case 1:
                                if not self.serviceSt.if_eng_station_compete(self.ctrlSt.list_station):
                                    # Enregistrement Station
                                    station = self.menu.menu_nom_station()
                                    essence = self.menu.menu_type_essence()

                                    if type(essence) == str:
                                        if self.serviceSt.acces_eng_station(self.ctrlSt.list_station, station, essence):
                                            capacite = self.menu.cnt_B.valide_intervalle_saisie_float(12000, 9999999999,
                                                                                                      self.menu.cnt_B.decimal_number())
                                            self.ctrlSt.enregistrer_station(station, essence, capacite)
                                            self.menu.cnt_B.pause()
                                        else:
                                            print(
                                                f"{self.color.RED}Desole, cette station est deja enregistree,vous ne pouvez que modifier la capacite de cette station 🚫 ! {self.color.END}")
                                            self.menu.cnt_B.pause()
                                    else:
                                        for i in range(2):
                                            print(f"{self.color.BLUE}{self.color.BOLD}{essence[i]} : {self.color.END}")
                                            if self.serviceSt.acces_eng_station(self.ctrlSt.list_station, station,
                                                                                essence[i]):
                                                capacite = self.menu.cnt_B.valide_intervalle_saisie_float(12000,
                                                                                                          9999999999,
                                                                                                          self.menu.cnt_B.decimal_number())
                                                self.ctrlSt.enregistrer_station(station, essence[i], capacite)
                                                self.menu.cnt_B.pause()
                                            else:
                                                print(
                                                    f"{self.color.RED}Desole, cette station est deja enregistree, vous ne pouvez que modifier la capacite de cette station 🚫!{self.color.END}")
                                                self.menu.cnt_B.pause()
                                else:
                                    print(f"{self.color.RED}Cette option est interdite, car la liste des stations est complete 🚫!{self.color.END}")
                                    self.menu.cnt_B.pause()
                            case 2:
                                # Modification Station
                                station = self.menu.menu_nom_station()
                                essence = self.menu.menu_type_essence()

                                if type(essence) == str:
                                    if not self.serviceSt.acces_eng_station(self.ctrlSt.list_station, station, essence):
                                        new_capacite = self.menu.cnt_B.valide_intervalle_saisie_float(12000, 9999999999,
                                                                                                      self.menu.cnt_B.decimal_number())
                                        self.ctrlSt.modifier_quantite_gallon(station, essence, new_capacite)
                                        self.menu.cnt_B.pause()
                                    else:
                                        print(f"{self.color.RED}Veuillez verifier l'existence de ces informations SVP 🚫!{self.color.END}")
                                        self.menu.cnt_B.pause()
                                else:
                                    for i in range(2):
                                        print(f"{self.color.BLUE}{self.color.BOLD}{essence[i]} : {self.color.END}")
                                        if not self.serviceSt.acces_eng_station(self.ctrlSt.list_station, station,
                                                                                essence[i]):
                                            new_capacite = self.menu.cnt_B.valide_intervalle_saisie_float(12000,
                                                                                                          9999999999,
                                                                                                          self.menu.cnt_B.decimal_number())
                                            self.ctrlSt.modifier_quantite_gallon(station, essence[i], new_capacite)
                                            self.menu.cnt_B.pause()
                                        else:
                                            print(f"{self.color.RED}Veuillez verifier l'existence de ces informations SVP 🚫!{self.color.END}")
                                            self.menu.cnt_B.pause()

                            case 3:
                                # Affichage Station
                                self.ctrlSt.afficher_stations()
                                self.menu.cnt_B.pause()
                            case 4:
                                # Retour
                                break

                # GESTION COMMANDE
                case 2:
                    while True:
                        match self.menu.menu_gestion_commande():
                            case 1:
                                # Enregistrement commande
                                essence = self.menu.menu_type_essence()
                                if self.serviceSt.acces_commande(self.ctrlSt.list_station, essence) or self.serviceSt.if_eng_station_compete(self.ctrlSt.list_station):
                                    self.ctrlSt.afficher_stations()
                                    print(f"{self.color.BLUE}Voulez vous vraiment faire une commande ❓ [1-oui : 2- non]{self.color.END}")
                                    reponse = self.menu.cnt_B.valide_intervalle_sasie_entier(1, 2,
                                                                                             self.menu.cnt_B.int_number())
                                    if reponse == 1:
                                        # essence = self.menu.menu_type_essence()
                                        self.ctrlcmd.enregister_commande(essence)
                                    else:
                                        print(f"{self.color.WARNING}Merci pour votre choix... ⚠️{self.color.END}")
                                    self.menu.cnt_B.pause()
                                else:
                                    print(f"{self.color.RED}Vous devez d\'abord enregistrer toutes ces citerne 🚫!{self.color.END}")
                                    self.menu.cnt_B.pause()
                            case 2:
                                # affichage commande
                                self.ctrlcmd.afficher_commande()
                                self.menu.cnt_B.pause()
                            case 3:
                                # Retour
                                break

                case 3:
                    while True:
                        match self.menu.menu_gestion_approvisionnement():
                            case 1:
                                # Enregistrement approvisionnement
                                if self.ctrlcmd.commande_list:
                                    self.ctrlcmd.afficher_commande()
                                    print(f"{self.color.BLUE}vous voulez vraiment faire une commande ❓ [1-oui : 2- non]{self.color.END}")
                                    reponse = self.menu.cnt_B.valide_intervalle_sasie_entier(1, 2,
                                                                                             self.menu.cnt_B.int_number())
                                    if reponse == 1:
                                        essence = self.menu.menu_type_essence()
                                        self.ctrlAp.enregistrer_approvisionnement(essence)
                                        self.menu.cnt_B.pause()
                                    else:
                                        print(f"{self.color.WARNING}Merci pour votre choix...⚠️{self.color.END}")
                                        self.menu.cnt_B.pause()
                                else:
                                    print(f"{self.color.RED}Vous devez d'abord enregistrer une commande 🚫!{self.color.END}")
                                    self.menu.cnt_B.pause()
                            case 2:
                                # affichage approvisionnement
                                self.ctrlAp.afficher_approvisionnement()
                                self.menu.cnt_B.pause()
                            case 3:
                                # Retour
                                break
                case 4:
                    while True:
                        match self.menu.menu_gestion_vente():
                            case 1:
                                # enregistrement vente
                                if self.ctrlAp.set_app:
                                    station = self.menu.menu_nom_station()
                                    essence = self.menu.menu_type_essence()
                                    if type(essence) == str:
                                        if self.ctrlSt.serviceSt.if_station_renfloueler(self.ctrlSt.list_station, station, essence):
                                            quantite = self.menu.cnt_B.decimal_number()
                                            self.ctrlV.enregistrer_vente(station, essence, quantite)
                                            self.menu.cnt_B.pause()
                                        else:
                                            print(f"{self.color.RED}Cette citerne est vide 🚫!{self.color.END}")
                                            self.menu.cnt_B.pause()
                                    else:
                                        if self.ctrlSt.serviceSt.if_station_renfloueler(self.ctrlSt.list_station, station, essence[0]) and self.ctrlSt.serviceSt.if_station_renfloueler(self.ctrlSt.list_station, station, essence[1]):
                                            quantite = []
                                            for i in range(2):
                                                print(f"{self.color.BLUE}{self.color.BOLD}{essence[i]}: {self.color.END}")
                                                quantite.append(self.menu.cnt_B.decimal_number())
                                            self.ctrlV.enregistrer_vente(station, essence, quantite)
                                            self.menu.cnt_B.pause()
                                        else:
                                                print(f"{self.color.RED}vous ne pouvez pas effectuer de vente pour Gazoline et Diesel 🚫!{self.color.END}")
                                                self.menu.cnt_B.pause()
                                else:
                                    print(f"{self.color.RED}Vous devez d'abord effectuer un approvisionnement 🚫!{self.color.END}")
                                    self.menu.cnt_B.pause()

                            case 2:
                                # affichage vente
                                self.ctrlV.afficher_ventes()
                                self.menu.cnt_B.pause()
                            case 3:
                                # Retour
                                break
                case 5:
                    exit()
