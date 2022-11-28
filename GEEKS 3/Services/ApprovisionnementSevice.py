from Controller.ControllerCommande import CommandeController


class ApprovisionnementService:
    ctrlcmd = CommandeController()

    def acces_one_approvisionnement(self, type_essence):
        for i in self.ctrlcmd.commande_list:
            if i:
                if type(type_essence) == str:
                    if type(i.get_type_essence()) == str and i.get_type_essence() == type_essence and i.get_etat() == "N":
                        return True
                    elif type(i.get_type_essence()) == list and i.get_type_essence()[0] == type_essence or i.get_type_essence()[1] == type_essence :
                        if type_essence == 'Gazoline' and i.get_etat()[0] == "N":
                            return True
                        elif type_essence == 'Diesel' and i.get_etat()[1] == "N":
                            return True
                elif type(i.get_type_essence()) == list and i.get_etat() == ['N', 'N']:
                    return True

    @staticmethod
    def acces_two_approvisionnement(quantite_approv,quantite):
        if quantite_approv != quantite:
            return True
        else:
            return False

    def update_etat(self, type_essence):
        for i in self.ctrlcmd.commande_list:
            if i:
                if type(type_essence) == str:
                    if type(i.get_type_essence()) == str:
                        if i.get_type_essence() == type_essence and i.get_etat() == "N":
                            i.set_etat('P')
                            break
                    else:
                        if type_essence == 'Gazoline' and i.get_etat()[0] == "N":
                            i.set_etat(['P', i.get_etat()[1]])
                            break
                        elif type_essence == 'Diesel' and i.get_etat()[1] == "N":
                            i.set_etat([i.get_etat()[0], 'P'])
                            break
                else:
                    if type(i.get_type_essence()) == list and type(type_essence) == list and i.get_etat() == ["N", "N"]:
                        i.set_etat(['P', 'P'])
                        break



    def rechercher_qte_cmd(self, type_essence):
        for i in self.ctrlcmd.commande_list:
            if i:
                if type(i.get_type_essence()) == list and type_essence == "Gazoline" and i.get_etat()[0] == 'N':
                    return i.get_quantite()[0]
                elif type(i.get_type_essence()) == list and type_essence == "Diesel" and i.get_etat()[1] == 'N':
                    return i.get_quantite()[1]
                elif i.get_type_essence() == type_essence and i.get_etat() == 'N' or i.get_etat() == ['N', 'N']:
                        return i.get_quantite()
