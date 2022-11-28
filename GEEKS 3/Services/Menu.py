from Services.ContrainteBase import ContrainteBase
from Services.TextColors import TextColors


class Menu:
    cnt_B = ContrainteBase()
    color = TextColors()

    def menu_principal(self):
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}{self.color.BOLD} Menu principal  :                                                                 {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 1 : Gestion Station 📊                                                      {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 2 : Gestion Commandes 📊                                                    {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 3 : Gestion Approvisionnement 📊                                            {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 4 : Gestion Vente  📊                                                       {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 5 : Quiter Le Programme  ❌                                                 {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(f'{self.color.BLUE}{self.color.BOLD}Choisir une  option dans l\'intervalle  [1...5]  {self.color.END}')
        choix_menu_principal = self.cnt_B.valide_intervalle_sasie_entier(1, 5, self.cnt_B.int_number())
        return choix_menu_principal

    def menu_gestion_station(self):
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}{self.color.BOLD} Gestion Station 📊 :                                                              {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 1 : Enregistrement stations 🗃                                              {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 2 : Modifier quantité gallon de gazoline et/ou de Diesel d’une station 📝   {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 3 : Afficher toutes les stations  🖥                                        {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END}  {self.color.BLUE}Taper 4 : Retour  ⬅ ︎                                                             {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(f'{self.color.BLUE}{self.color.BOLD}Choisir une  option dans l\'intervalle [1...4]  {self.color.END}')
        choix_menu_gestion_station = self.cnt_B.valide_intervalle_sasie_entier(1, 4, self.cnt_B.int_number())
        return choix_menu_gestion_station

    def menu_nom_station(self):
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}{self.color.BOLD} Station  📛:                                                                      {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 1 : Lalue                                                                    {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 2 : Tabarre                                                                  {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 3 : Clercine                                                                 {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 4 : Pétion-ville                                                             {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(f'{self.color.BLUE}{self.color.BOLD}Choisir une  option dans l\'intervalle [1...4]  {self.color.END}')
        choix_nom_station = self.cnt_B.valide_intervalle_sasie_entier(1, 4, self.cnt_B.int_number())
        match choix_nom_station:
            case 1:
                return "lalue"
            case 2:
                return "tabarre"
            case 3:
                return "clercine"
            case 4:
                return "petion_ville"

    def menu_type_essence(self):
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}{self.color.BOLD} Type Essence 🚭📛:                                                                {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 1 : Gazoline  📛                                                             {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 2 :  Diesel    📛                                                            {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 3 :  Gazoline et Diesel 📛                                                   {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(f'{self.color.BLUE}{self.color.BOLD}Choisir une  option dans l\'intervalle [1...3]  {self.color.END}')
        choix_type_essence = self.cnt_B.valide_intervalle_sasie_entier(1, 3, self.cnt_B.int_number())
        match choix_type_essence:
            case 1:
                return "Gazoline"
            case 2:
                return "Diesel"
            case 3:
                return ["Gazoline", "Diesel"]

    def menu_gestion_commande(self):
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}{self.color.BOLD} Gestion Commande  📊:                                                              {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 1 : Enregistrement commande 🗃                                                {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 2 : Afficher toutes les commandes  🖥                                         {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 3 : Retour  ⬅︎                                                                 {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(f'{self.color.BLUE}{self.color.BOLD}Choisir une  option dans l\'intervalle [1...3]  {self.color.END}')
        choix_menu_gestion_commande = self.cnt_B.valide_intervalle_sasie_entier(1, 3, self.cnt_B.int_number())
        return choix_menu_gestion_commande

    def menu_gestion_approvisionnement(self):
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}{self.color.BOLD} Gestion Approvisionnement  📊:                                                      {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 1 : Enregistrement approvisionnement  🗃                                       {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 2 : Afficher toutes les Approvisionnements   🖥                                {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 3 : Retour    ⬅︎                                                                {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(f'{self.color.BLUE}{self.color.BOLD}Choisir une  option dans l\'intervalle [1...3]  {self.color.END}')
        choix_menu_gestion_approvisionnement = self.cnt_B.valide_intervalle_sasie_entier(1, 3, self.cnt_B.int_number())
        return choix_menu_gestion_approvisionnement

    def menu_gestion_vente(self):
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}{self.color.BOLD} Gestion vente  📊:                                                                   {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 1 : Enregistrement vente  🗃                                                    {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 2 : Afficher toutes les ventes   🖥                                             {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}|{self.color.END} {self.color.BLUE}Taper 3 : Retour    ⬅︎                                                                 {self.color.END}{self.color.GREEN}{self.color.BOLD}|{self.color.END}")
        print(
            f"{self.color.GREEN}{self.color.BOLD}--------------------------------------------------------------------------------------{self.color.END}")
        print(f'{self.color.BLUE}{self.color.BOLD}Choisir une  option dans l\'intervalle [1...3]  {self.color.END}')
        choix_menu_gestion_vente = self.cnt_B.valide_intervalle_sasie_entier(1, 3, self.cnt_B.int_number())
        return choix_menu_gestion_vente
