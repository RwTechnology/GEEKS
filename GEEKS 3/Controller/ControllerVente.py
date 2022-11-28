import uuid
from datetime import datetime
from Model.Vente import Vente
from Services.ServiceStation import ServiceStation
from Controller.ControllerStation import ControllerStation
from Services.ServiceVente import ServiceVente
from Services.TextColors import TextColors


class ControllerVente:
    list_vente = []
    sv_Station = ServiceStation()
    sv_vente = ServiceVente()
    list_station = ControllerStation().list_station
    color = TextColors()

    def enregistrer_vente(self, nom_station, type_essence, quantite):
        id = str(uuid.uuid4().fields[-1])[:5]
        date_vente = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
        vente = Vente(id, nom_station, type_essence, quantite, date_vente)

        if type(type_essence) == str:
            if self.sv_Station.if_valide_defoulememt(self.list_station, nom_station, type_essence, quantite):
                self.list_vente.append(vente)
                self.sv_Station.defoulememt(self.list_station, nom_station, type_essence, quantite)
                print(f"\n{self.color.SUCCES}Vente effectuee avec succes ✅{self.color.ENDBG}")
            else:
                print(f"{self.color.RED}La quantite disponible est insuffisante pour cette vente 🚫!{self.color.END}")

        else:
            if self.sv_Station.if_valide_defoulememt(self.list_station, nom_station, type_essence[0], quantite[0]) and self.sv_Station.if_valide_defoulememt(self.list_station, nom_station, type_essence[1], quantite[1]):
                self.list_vente.append(vente)
                self.sv_Station.defoulememt(self.list_station, nom_station, type_essence[0], quantite[0])
                self.sv_Station.defoulememt(self.list_station, nom_station, type_essence[1], quantite[1])
                print(f"\n{self.color.SUCCES}Ventes {type_essence[0]} et {type_essence[1]} effectuees avec succes ✅{self.color.ENDBG}")
            else:
                print(f"{self.color.RED} Veillez verifier vos quantites disponible 🚫!{self.color.END}")


    def afficher_ventes(self):
        if self.list_vente:
            n = 1
            for i in self.list_vente:
                print(f"{self.color.GREEN}{self.color.BOLD}\n------------- Vente # {n}{self.color.END}")
                print(f"{self.color.BLUE}ID                  : {i.get_id()}")
                print(f"Station             : {i.get_nom_station()}")

                if type(i.get_type_essence()) == str:
                    print(f"Quantite {i.get_type_essence()}   : {i.get_quantite()} Gallon(s)")
                    print(
                        f"Prix de vente : {self.sv_vente.calculer_prix_total_vente(i.get_type_essence(), i.get_quantite())} GDES")
                else:
                    print(f"{i.get_type_essence()[0]} : {i.get_quantite()[0]} Gallon(s)")
                    print(
                        f"Prix de vente : {self.sv_vente.calculer_prix_total_vente(i.get_type_essence()[0], i.get_quantite()[0])} GDES")
                    print(f"{i.get_type_essence()[1]} : {i.get_quantite()[1]} Gallon(s)")
                    print(
                        f"Prix Vente : {self.sv_vente.calculer_prix_total_vente(i.get_type_essence()[1], i.get_quantite()[1])} GDES")
                print(f"Date vente : {i.get_date_vente()}{self.color.END}")
                n += 1
        else:
            print(f"{self.color.RED}\nDesole, aucune vente n'est encore effectuee 🚫!{self.color.END}")
