__author__ = 'Doryan Valentin Thomas'

from tkinter import *
from tkinter import ttk
from os import *
import os

def charger_images(l = list, repertoire = str, titre = str):
    global Catalogue
    listewidget = Listbox(Catalogue)
    listewidget.bind('<<ListboxSelect>>', change_selection)
    liste_fichier = os.listdir(repertoire)
    for nomfichier in liste_fichier:
        nomcomplet = repertoire + os.sep + nomfichier
        photo = PhotoImage(file = nomcomplet)
        l.append(photo)
        nouveau_nom = '.'.join(nomfichier.split('.')[:-1])  #On retire l'extension dans le nom du fichier
        nouveau_nom = str.capitalize(nouveau_nom)
        listewidget.insert(END, nouveau_nom)
    Catalogue.add(listewidget, text = titre)

def change_catalogue(event):
    global catalogue_choisi
    catalogue_choisi = event.widget.index("current")

def change_selection(event):
    global listes_image
    print(event.widget.curselection())

fenetre = Tk()
fenetre.title('Outil de création de visage type portrait robot')
fenetre['bg']='white'

#Création de l'interface
FrameCatalogue = Frame(fenetre, borderwidth=2, relief=GROOVE, width = 250, height = 400)
FrameCatalogue.pack(side=LEFT, padx=2, pady=2)
Catalogue = ttk.Notebook(FrameCatalogue)
Catalogue.bind_all("<<NotebookTabChanged>>", change_catalogue)

#Chargement des images
catalogue_choisi = 0
listes_image = []

liste_visages = []
charger_images(liste_visages, "Images/Visages", "Visages")
listes_image.append(liste_visages)
liste_nez = []
charger_images(liste_nez, "Images/Nez", "Nez")
listes_image.append(liste_nez)
liste_yeux = []
charger_images(liste_yeux, "Images/Yeux", "Yeux")
listes_image.append(liste_yeux)
liste_moustaches = []
charger_images(liste_moustaches, "Images/Moustaches", "Moustaches")
listes_image.append(liste_moustaches)
liste_cheveux = []
charger_images(liste_cheveux, "Images/Cheveux", "Cheveux")
listes_image.append(liste_cheveux)

Catalogue.pack(side = LEFT)

#Boucle Principale
fenetre.mainloop()


    

