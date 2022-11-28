import uuid
from datetime import datetime
from Controller.ControllerStation import ControllerStation
from Services.ServiceStation import ServiceStation
from Services.ApprovisionnementSevice import ApprovisionnementService
from Model.Approvisionnement import Approvisionnement
from Services.TextColors import TextColors


class ApprovisionnementController:
    set_app = set()
    list_station = ControllerStation().list_station
    service_app = ApprovisionnementService()
    service_station = ServiceStation()
    color = TextColors()

    def enregistrer_approvisionnement(self, essence):

        if self.service_app.acces_one_approvisionnement(essence):
            id = str(uuid.uuid4().fields[-1])[:5]
            date = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
            quantite = self.service_app.rechercher_qte_cmd(essence)

            # renflouement
            if type(essence) == str:
                quantite_approv = self.service_station.renflouement(self.list_station, essence, quantite)
                if self.service_app.acces_two_approvisionnement(quantite_approv,quantite):
                    self.service_app.update_etat(essence)
                    app_object = Approvisionnement(id, essence, quantite, date)
                    self.set_app.add(app_object)
                    print(f"\n{self.color.SUCCES} Enregistrement avec succes ✅{self.color.ENDBG}")
                else:
                    print(
                        f"\n{self.color.RED}Vous ne pouvez pas approvisionner ces citerne pour le moments 🚫!{self.color.END}")
            else:
                quantite_approv1 = self.service_station.renflouement(self.list_station, essence[0], quantite[0])
                quantite_approv2 = self.service_station.renflouement(self.list_station, essence[1], quantite[1])

                if self.service_app.acces_two_approvisionnement(quantite_approv1,quantite[0]) and self.service_app.acces_two_approvisionnement(quantite_approv2, quantite[1]):
                    self.service_app.update_etat(essence)
                    app_object = Approvisionnement(id, essence, quantite, date)
                    self.set_app.add(app_object)
                    print(f"\n{self.color.SUCCES} Enregistrement avec succes ✅{self.color.ENDBG}")
                else:
                    print(f"\n{self.color.RED}ces citernes  ne peuvent pas approvisionner pour le moment 🚫!{self.color.END}")
        else:
            print(f"\n{self.color.RED}approvisionnement impossible, veillez verifier ces informations 🚫!{self.color.END}")

    def afficher_approvisionnement(self):
        if len(self.set_app) != 0:
            n = 1
            for i in self.set_app:
                print(f"\n{self.color.GREEN}{self.color.BOLD}-------------Approvisionnement no {n}{self.color.END}")
                print(f"{self.color.BLUE}ID                       : {i.get_id()}")

                if type(i.get_type_essence()) == str:
                    print(f"quantite {i.get_type_essence()}   : {i.get_quantite()} Gallon(s)")
                else:
                    print(f"quantite {i.get_type_essence()[0]} : {i.get_quantite()[0]} Gallon(s)")
                    print(f"quantite {i.get_type_essence()[1]} : {i.get_quantite()[1]} Gallon(s)")

                print(f"Date approvisionnement   : {i.get_date()}{self.color.END}")
                n += 1
        else:
            print(f"\n{self.color.RED}Desole, aucun approvisionnement n'est encore effectue 🚫!{self.color.END}")
