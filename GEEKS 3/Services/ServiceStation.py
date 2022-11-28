from Services.TextColors import TextColors


class ServiceStation:
    color = TextColors()

    @staticmethod
    def acces_eng_station(list_station, station, essence):
        verificateur = False
        for dict_element in list_station:
            if dict_element:
                for value in dict_element.values():
                    if value.get_nom_station() == station and value.get_type_essence() == essence:
                        return False
        if not verificateur:
            return True

    @staticmethod
    def if_list_station_vide(list_station):
        for i in list_station:
            if i:
                return True

    @staticmethod
    def if_eng_station_compete(list_station):
        n = 0
        for dict_element in list_station:
            if len(dict_element) == 2:
                n += 1
        if n == 4:
            return True

    @staticmethod
    def acces_commande(list_station, essence):
        n = 0
        for dict_element in list_station:
            if dict_element:
                for value in dict_element.values():
                    if value.get_type_essence() == essence:
                        n += 1
        if n == 4:
            return True

    @staticmethod
    def calcul_pourc_ut(qantite_commandee, qte_disponible):
        pourc_ut = 0.0
        if qantite_commandee != 0.0:
            pourc_ut = ((qantite_commandee - qte_disponible) * 100) / qantite_commandee
        return pourc_ut


    def auxilliare_modifier_quantite_gallon(self, dict, type_essence, new_capacite):
        for value in dict.values():
            if value.get_type_essence() == type_essence:
                value.set_capacite(new_capacite)
                print(f"{self.color.SUCCES}Modification avec succes ✅{self.color.ENDBG}")

    @staticmethod
    def total_gal_gaz_manquant(list_station):
        total_gal_gaz_manquant = 0
        for i in list_station:
            if i:
                for value in i.values():
                    if value.get_type_essence() == 'Gazoline':
                        total_gal_gaz_manquant += (value.get_capacite() - value.get_quantite_disponible())
        return total_gal_gaz_manquant

    @staticmethod
    def total_gal_dies_manquant(list_station):
        total_gal_dies_manquant = 0
        for i in list_station:
            if i:
                for value in i.values():
                    if value.get_type_essence() == 'Diesel':
                        total_gal_dies_manquant += (value.get_capacite() - value.get_quantite_disponible())
        return total_gal_dies_manquant


    @staticmethod
    def if_station_renfloueler(list_station, station, type_essence):
        for i in list_station:
            if i:
                for value in i.values():
                    if value.get_nom_station() == station and value.get_type_essence() == type_essence:
                        if value.get_quantite_disponible() != 0.0:
                            return True


    @staticmethod
    def renflouement(list_station, type_essence, quantite):
        for i in list_station:
            if i:
                for value in i.values():
                    if value.get_type_essence() == type_essence:
                        qte_manquante = value.get_capacite()-value.get_quantite_disponible()
                        quantite -= qte_manquante
                        qte = value.get_quantite_disponible() + qte_manquante
                        value.set_quantite_disponible(qte)
                        value.set_qte_commandee(value.get_quantite_disponible())
        return quantite





    @staticmethod
    def if_valide_defoulememt(list_station, station, type_essence, quantite):
        for i in list_station:
            if i:
                for value in i.values():
                    if value.get_nom_station() == station and value.get_type_essence() == type_essence:
                        if value.get_quantite_disponible() >= quantite:
                            return True



    @staticmethod
    def defoulememt(list_station, station, type_essence, quantite):
        for i in list_station:
            if i:
                for value in i.values():
                    if value.get_nom_station() == station and value.get_type_essence() == type_essence:
                        qte = value.get_quantite_disponible()-quantite
                        value.set_quantite_disponible(qte)








