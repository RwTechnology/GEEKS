from Model.Commande import Commande
from Services.CommandeService import CommandeService
import uuid
from datetime import datetime
from Services.TextColors import TextColors


class CommandeController:
    commande_list = []
    color = TextColors()

    service_cmd = CommandeService()

    def enregister_commande(self, essence):
        id = str(uuid.uuid4().fields[-1])[:5]
        date_commande = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
        etat = self.service_cmd.gerer_etat_commande(self.commande_list, essence)
        quantite = self.service_cmd.gerer_quantite_commande(essence)

        if type(essence) == str:
            if quantite != 0.0:
                cmd_objet = Commande(id, essence, quantite, date_commande, etat)
                self.commande_list.append(cmd_objet)
                print(f"\n{self.color.SUCCES}Enregistrement avec succes ✅{self.color.ENDBG}")
            else:
                print(f"{self.color.RED}Vous ne pouvez pas effectuer cette commande pour le moment 🚫!{self.color.END}")
        else:
            if quantite[0] !=0.0 and quantite[1] !=0.0:
                cmd_objet = Commande(id, essence, quantite, date_commande, [etat, etat])
                self.commande_list.append(cmd_objet)
                print(f"\n{self.color.SUCCES}Enregistrement avec succes ✅{self.color.ENDBG}")
            else:
                print(f"{self.color.RED}Vous ne pouvez pas effectuer cette commande pour le moment 🚫!{self.color.END}")

    def afficher_commande(self):
        if self.commande_list:
            n=1
            for i in self.commande_list:
                print(f"\n{self.color.GREEN}{self.color.BOLD}-------------Commande no {n}{self.color.END}")
                print(f"{self.color.BLUE}ID                  : {i.get_id()}")

                if type(i.get_type_essence()) == str:
                    print(f"quantite {i.get_type_essence()}   : {i.get_quantite()} Gallon(s)")
                else:
                    print(f"quantite {i.get_type_essence()[0]} : {i.get_quantite()[0]} Gallon(s)")
                    print(f"quantite {i.get_type_essence()[1]} : {i.get_quantite()[1]} Gallon(s)")

                print(f"Date Commande : {i.get_date_commande()}")
                print(f"Etat Commande : {i.get_etat()}{self.color.END}")
                n += 1
        else:
            print(f"\n{self.color.RED}Desole, aucune Commande n'est encore effectuee 🚫!{self.color.END}")







