#!/bin/python3.8
# coding: utf-8

import csv
import os


class Parking:
    """Classe Parking"""

    def __init__(self, name, capacity):
        """Constructeur"""

        self.file = "/home/sun/Documents/prog_Python/Zoo/vehicules.csv"
        self.occupation = 0  # nbre de place occupees
        self.name = name  # nom du parking
        self.capacity = capacity  # nbre Total de place
        self.vehicules = list()  # Liste des vehicules

    # ======================= GETTERS ===================================

    def getOccupation(self):
        """Cette Methode retourne le Nbre de Vehicule
        present dans le Parking"""

        return self.occupation

    def getName(self):
        """Cette Methode retourne le nom du Parking"""
        return self.name

    def getCapacity(self):
        """Cette methode retourne le nombre total de place du parking"""
        return self.capacity

    def getFile(self):
        """Cette Methode retourne le PATH du fichier CSV"""
        return self.file

    # ======================= SETTERS ===================================

    def setFile(self, file):
        """Cette Methode definit le PATH du fichier csv"""
        self.file = file

    # ====================== FUNCTIONS ==================================

    def add_vehicule(self, vehicule):
        """Methode qui ajoute un Vehicule dans le fichier CSV
        args:
           vehicule: Donnees d'un vehicule (immatriculation, marque,
                     modele, couleur, kilometrage)
        """

        if self.getOccupation() < self.getCapacity():
            if self.is_vehicule(vehicule[0]) is False:
                self.vehicules.append(vehicule)
                self.occupation += 1
                self.update_file()

    def remove_vehicule(self, matricule):
        """Supprime un vehicule
        Args:
            matricule: immatriculation du vehicule

        Returns:
            Bool: True si la Suppression a reussi, False si non"""

        if self.is_vehicule(matricule):
            for vehicule in self.vehicules:
                if matricule in vehicule:
                    self.vehicules.remove(vehicule)
                    self.occupation -= 1
                    self.update_file()
                    return True
        return False

    def list_vehicules(self):
        """Affiche la Liste des Vehicules"""

        number = 1
        if self.occupation > 0:
            for vehicule in self.vehicules:
                print(number, " - ", vehicule)
                number += 1
            return True
        else:
            return False

    def getVehicule(self, matricule):
        """Cette Methode Retourne un vehicule
        args:
           matricule: immatriculation du vehicule
        """

        for vehicule in self.vehicules:
            if matricule in vehicule:
                return vehicule
        return None

    # ====================== UTILITIESS ==================================

    def is_vehicule(self, matricule):
        """Cette Methode verifie si un vehicule est present ou non
        args:
           matricule: immatriculation du vehicule
        """

        if len(self.vehicules) > 0:
            for vehicule in self.vehicules:
                if matricule in vehicule:
                    return True
        return False

    def load_file(self, pathfile=""):
        """Cette Methode charge le contenu du fichier csv

        Args:
          [pathfile]: chemin vers le fichier csv
        """

        if pathfile == "":
            if self.file == "":
                return "Error. Empty PATH"
            pathfile = self.file

        if os.path.exists(pathfile):
            with open(pathfile, "r") as f:
                csv_reader = csv.reader(f, delimiter=",", quotechar='"')
                csv_reader.__next__()  # avance d'une ligne dans le fichier
                for element in csv_reader:
                    self.vehicules.append(element)
                self.occupation = csv_reader.line_num - 1

    def update_file(self):
        """Cette Fonction Met a jour le fichier"""

        if os.path.exists(self.file):
            with open(self.file, "w") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(
                    [
                        "immatriculation",
                        "marque",
                        "modele",
                        "couleur",
                        "kilometrage",
                    ]
                )
                for vehicule in self.vehicules:
                    csv_writer.writerow(vehicule)
                return True
        return False


# ======================= MAIN ===================================

if __name__ == "__main__":

    myPark = Parking("sudo", 7)
    print("\nCapacity:", myPark.getCapacity())
    print("Occupation before loading file:", myPark.getOccupation())

    myPark.load_file()
    print("Occupation after loading file:", myPark.getOccupation())

    print("\nList of Vehicules:", myPark.getOccupation())
    myPark.list_vehicules()
    print("\nVehicule 'OST8989': ", myPark.getVehicule("OST8989"))

    print("\nWe remove: HDT6542")
    myPark.remove_vehicule("HDT6542")
    print("\nList of Vehicules: ", myPark.getOccupation())
    myPark.list_vehicules()

    print("\nWe Add: NSU2022")
    myPark.add_vehicule(["NSU2022", "Lamborgini", "Gallardo", "noir", "70000.03"])
    print("\nList of Vehicules: ", myPark.getOccupation())
    myPark.list_vehicules()
    print()
