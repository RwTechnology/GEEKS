from Services.TextColors import TextColors


class ContrainteBase:
    color = TextColors()

    # valider nombre entier
    def int_number(self):
        while True:
            try:
                value = int(input(" : "))
            except ValueError:
                print(f"{self.color.WARNING}{self.color.BOLD}Entrer une valeur valide ! Réessayer.⚠️ {self.color.WARNING}{self.color.END}")
                continue
            else:
                return value
                break

    # valider capacite
    def decimal_number(self):
        while True:
            try:
                value = float(input(f"{self.color.BLUE}Saisir la capacite ou quantite : {self.color.END}"))
            except ValueError:
                print(f"{self.color.WARNING}{self.color.BOLD}Entrer une valeur valide ! Réessayer. ⚠️{self.color.WARNING}{self.color.END}")
                continue
            else:
                return value
                break

    def valide_intervalle_sasie_entier(self,debut, fin, value_saisie):
        while value_saisie < debut or value_saisie > fin:
            print(f"{self.color.WARNING}{self.color.BOLD}Veuillez respecter l'intervalle [{debut}......{fin}]: ⚠️{self.color.WARNING}{self.color.END}")
            value_saisie = self.int_number()
        return value_saisie

    def valide_intervalle_saisie_float(self,debut, fin, value_saisie):
        while value_saisie < debut or value_saisie > fin:
            print(f"{self.color.WARNING}{self.color.BOLD}Veuillez respecter l'intervalle [{debut}......{fin}]: ⚠️{self.color.WARNING}{self.color.END}")
            value_saisie = self.decimal_number()
        return value_saisie

    def pause(self):
        input(f"{self.color.GREEN}{self.color.BOLD}\nAppuyer sur la touche enter pour continuer : ⛔🟢{self.color.WARNING}{self.color.BOLD}")


