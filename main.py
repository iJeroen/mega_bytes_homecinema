__author__ = 'Megabytes'
from time import strftime
from tkinter import messagebox
import tkinter as tk
import requests
import codecs
import xmltodict
import random
import csv
#Variabelen
api_key = 'avu3ndzhd6lzuvpphoijz4gsex1wgfd3'
dag = strftime("%d-%m-20%y")
sorteer = '0'
 
 
#Opvragen API en omzetten in bruikbare data
 
response = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=' + api_key + '&dag=' + dag + '&sorteer=' + sorteer)
xmlomzet = (response.text)
 
def schrijf_xml(reponse):
    bestand = open('films.xml', 'w')
    bestand = codecs.open('films.xml', "w", "utf-8")
    bestand.write(str(response.text))
    bestand.close()
 
schrijf_xml(response)
 
def verwerk_xml():
    bestand = open('films.xml','r')
    xml_string=bestand.read()
    return(xmltodict.parse(xml_string))
 
 
film_dict=verwerk_xml()
eerste_naam = (film_dict['filmsoptv']['film'][0]['titel'])
 
 
#Lettertypes
font_title = ("Segoe UI Light", 24, "bold")
font_huur = ("Segoe UI Light", 20, "bold")
font_medium = ("Segoe UI Light", 16, "bold")
font_small = ("Segoe UI Light", 12)
 
 
class HomeCinema(tk.Tk):
 
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(column = 0, row = 0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
 
        self.frames = {}
        for F in (StartPage, Jeroen, Daan, Rick, Aanbieder, film_1, film_2, film_3, film_4, film_5, film_6):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame(StartPage)
 
    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()
 
 
class StartPage(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welkom bij HomeCinema", font=font_title)
        label.grid(column = 0, row = 0)
 
        button_jeroen = tk.Button(self, text="Aanbieder\nJeroen",
                            command=lambda: controller.show_frame(Jeroen), font=font_medium)
        button_daan = tk.Button(self, text="Aanbieder\nDaan",
                            command=lambda: controller.show_frame(Daan), font=font_medium)
        button_rick = tk.Button(self, text="Aanbieder\nRick",
                            command=lambda: controller.show_frame(Rick), font=font_medium)
        button_aanbieder = tk.Button(self, text="Ik ben een\naanbieder", bg="blue", fg="white",
                            command=lambda: controller.show_frame(Aanbieder), font=font_medium)
        button_jeroen.grid(column = 2, row = 2, sticky="W", columnspan = 1, rowspan = 1)
        button_daan.grid(column = 3, row = 2, sticky="W", columnspan = 1, rowspan = 1)
        button_rick.grid(column = 4, row = 2, sticky="W", columnspan = 1, rowspan = 1)
        button_aanbieder.grid(column=5, row=2, sticky="W", columnspan = 1, rowspan = 1)

        uitlog_button = tk.Button(text="Afsluiten", command=exit, font=font_medium, bg="red", fg="white")
        uitlog_button.grid(column = 1, row = 11)

        def filmtip():
            #Opvragen API en omzetten in bruikbare data
            api_key = 'avu3ndzhd6lzuvpphoijz4gsex1wgfd3'
            dag = strftime("%d-%m-20%y")
            filmtip_sorteer = '1'
 
            response = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=' + api_key + '&dag=' + dag + '&sorteer=' + filmtip_sorteer)
            xmlomzet = (response.text)
 
            def schrijf_xml(reponse):
                bestand = open('filmtip.xml', 'w')
                bestand = codecs.open('filmtip.xml', "w", "utf-8")
                bestand.write(str(response.text))
                bestand.close()
 
            schrijf_xml(response)
 
            def verwerk_xml():
                bestand = open('filmtip.xml','r')
                xml_string=bestand.read()
                return(xmltodict.parse(xml_string))
 
            filmtip_dict=verwerk_xml()
            filmtip_label = tk.Label(self, text="Filmtip:\n" + (filmtip_dict['filmsoptv']['film'][0]['titel']), font=font_medium, bg="black", fg="white")
            filmtip_label.grid(column = 1, row = 2, columnspan = 1, rowspan = 1)
 
        def film_van_de_dag():
            #FVDD = Film Van De Dag
            #Opvragen API en omzetten in bruikbare data
            api_key = 'avu3ndzhd6lzuvpphoijz4gsex1wgfd3'
            dag = strftime("%d-%m-20%y")
            fvdd_sorteer = '2'
 
            response = requests.get('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=' + api_key + '&dag=' + dag + '&sorteer=' + fvdd_sorteer)
            xmlomzet = (response.text)
 
            def schrijf_xml(reponse):
                bestand = open('fvdd.xml', 'w')
                bestand = codecs.open('fvdd.xml', "w", "utf-8")
                bestand.write(str(response.text))
                bestand.close()
 
            schrijf_xml(response)
 
            def verwerk_xml():
                bestand = open('fvdd.xml','r')
                xml_string=bestand.read()
                return(xmltodict.parse(xml_string))
 
            fvdd_dict=verwerk_xml()
            fvdd_label = tk.Label(self, text="Film van de dag:\n" + (fvdd_dict['filmsoptv']['film']['titel']), font=font_medium, bg="black", fg="white")
            fvdd_label.grid(column = 6, row = 2, columnspan = 1, rowspan = 1)
 
        filmtip()
        film_van_de_dag()
 
 
 
 
class Jeroen(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Jeroen's films", font=font_title)
        label.grid(column = 0, row = 0)
 
        button_film1 = tk.Button(self, text=(film_dict['filmsoptv']['film'][0]['titel']),
                           command=lambda: controller.show_frame(film_1), font=font_medium)
        button_film1.grid(column = 1, row = 1, columnspan = 3, rowspan = 2)
 
        button_film2 = tk.Button(self, text=(film_dict['filmsoptv']['film'][1]['titel']),
                           command=lambda: controller.show_frame(film_2), font=font_medium)
        button_film2.grid(column = 4, row = 1, columnspan = 3, rowspan = 2)
 
 
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 9, row = 5)
 
 
class Daan(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Daan's films", font=font_title)
        label.grid(column = 0, row = 0)
 
        button_film3 = tk.Button(self, text=(film_dict['filmsoptv']['film'][2]['titel']),
                           command=lambda: controller.show_frame(film_3), font=font_medium)
        button_film3.grid(column = 1, row = 1, columnspan = 3, rowspan = 2)
 
        button_film4 = tk.Button(self, text=(film_dict['filmsoptv']['film'][3]['titel']),
                           command=lambda: controller.show_frame(film_4), font=font_medium)
        button_film4.grid(column = 4, row = 1, columnspan = 3, rowspan = 2)
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 9, row = 5)
 
class Rick(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Rick's films", font=font_title)
        label.grid(column = 0, row = 0)
 
        button_film5 = tk.Button(self, text=(film_dict['filmsoptv']['film'][4]['titel']),
                           command=lambda: controller.show_frame(film_5), font=font_medium)
        button_film5.grid(column = 1, row = 1, columnspan = 3, rowspan = 2)
 
        button_film6 = tk.Button(self, text=(film_dict['filmsoptv']['film'][5]['titel']),
                           command=lambda: controller.show_frame(film_6), font=font_medium)
        button_film6.grid(column = 4, row = 1, columnspan = 3, rowspan = 2)
 
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 9, row = 5)
 
class Aanbieder(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Aanbieder Login", font=font_title)
        label.grid(column = 0, row = 0)
        entry_label1 = tk.Label(self, text="Naam Aanbieder")
        entry_label1.grid(column = 0, row = 8)
        entry1 = tk.Entry(self)
        entry1.grid(column = 1, row = 8)
 
        entry_label2 = tk.Label(self, text="Wachtwoord")
        entry_label2.grid(column = 0,  row = 9)
        entry2 = tk.Entry(self)
        entry2.grid(column = 1, row = 9)
        def show_afnemers():
            Naam = entry1.get()
            Wachtwoord = entry2.get()
            if Naam == "Daan" and Wachtwoord=="Mobach":
                bestand = 'daan_films.csv'
                file = open(bestand, 'r', newline='')
                fieldnames=['Naam', 'mail', 'film', 'starttijd', 'code']
                reader = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)
                result = sorted(reader, key=lambda d:(d['starttijd']))
                i=10
                for row in result:
                    tk.Label(self, text=("Naam: " , row['Naam'], "E-mail: " , row['mail'], "Film: " , row['film'], "Start tijd: " , row['starttijd'], "Code: " , row['code']), font=font_small).grid(column=6, row=i)
                    i+=1
            elif Naam=="Rick" and Wachtwoord=="Westerhoff":
                bestand = 'rick_films.csv'
                file = open(bestand, 'r', newline='')
                fieldnames=['Naam', 'mail', 'film', 'starttijd', 'code']
                reader = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)
                result = sorted(reader, key=lambda d:(d['starttijd']))
                i=10
                for row in result:
                    tk.Label(self, text=("Naam: " , row['Naam'], "E-mail: " , row['mail'], "Film: " , row['film'], "Start tijd: " , row['starttijd'], "Code: " , row['code']), font=font_small).grid(column=6, row=i)
                    i+=1
            elif Naam=="Jeroen" and Wachtwoord=="Hattem":
                bestand = 'jeroen_films.csv'
                file = open(bestand, 'r', newline='')
                fieldnames=['Naam', 'mail', 'film', 'starttijd', 'code']
                reader = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)
                result = sorted(reader, key=lambda d:(d['starttijd']))
                i=10
                for row in result:
                    tk.Label(self, text=("Naam: " , row['Naam'], "E-mail: " , row['mail'], "Film: " , row['film'], "Start tijd: " , row['starttijd'], "Code: " , row['code']), font=font_small).grid(column=6, row=i)
                    i+=1
            else:
                messagebox.showinfo("beste klant","Ga terug naar t hoofdmenu jonge, je ben geen aanbieder")
 
        check_button = tk.Button(self, text="Bevestig", command=show_afnemers, font=font_medium)
        check_button.grid(column = 1, row = 10, columnspan = 2)
        uitlog_button = tk.Button(self, text="Uitloggen", command=exit, font=font_medium)
        uitlog_button.grid(column = 1, row = 11, columnspan = 2)
 
        button = tk.Button(self, text="Ga terug naar 'Home'", command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 1, row = 15, columnspan = 2)
 
 
class film_1(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
 
        def save_user():
            global unieke_code
            unieke_code = random.randrange(10000000, 100000000)
            name = entry1.get()
            mail = entry2.get()
            film_naam = (film_dict['filmsoptv']['film'][0]['titel'])
            starttijd = (film_dict['filmsoptv']['film'][0]['starttijd'])
            code = unieke_code
            bestand = "jeroen_films.csv"
            file = open(bestand, 'a', newline='')
            fieldnames = ['Naam', 'mail', 'film', 'starttijd', 'code']
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writerow({'Naam':name, 'mail':mail, 'film':film_naam, 'starttijd':starttijd, 'code':code})
            messagebox.showinfo(film_naam, ("Uw film is gereserveerd!\nGebruik aub de volgende code: " + str(code)))
 
 
        label = tk.Label(self, text=(film_dict['filmsoptv']['film'][0]['titel']), font=font_title)
        label.grid(column = 1, row = 0)
        jaar_label = tk.Label(self, text= ("Jaar van uitgave: " + film_dict['filmsoptv']['film'][0]['jaar']), font=font_small)
        jaar_label.grid(column = 1, row = 2)
        samenvatting_label = tk.Label(self, text= ("Samenvatting: " + film_dict['filmsoptv']['film'][0]['synopsis']), font=font_small, wraplength = 500)
        samenvatting_label.grid(column = 1, row = 3)
        filmduur_label = tk.Label(self, text= ("Filmduur: " + film_dict['filmsoptv']['film'][0]['duur'] + " minuten"), font=font_small)
        filmduur_label.grid(column = 1, row = 4)
        zender_label = tk.Label(self, text= ("Te zien op zender: " + film_dict['filmsoptv']['film'][0]['zender']), font=font_small)
        zender_label.grid(column = 1, row = 5)


        entry_label1 = tk.Label(self, text="Naam", font=font_medium)
        entry_label1.grid(column = 0, row = 8)
        entry1 = tk.Entry(self)
        entry1.grid(column = 1, row = 8)

        entry_label2 = tk.Label(self, text="E-mail", font=font_medium)
        entry_label2.grid(column = 0,  row = 9)
        entry2 = tk.Entry(self)
        entry2.grid(column = 1, row = 9)

        check_button = tk.Button(self, text="Huur!", command=save_user, font=font_huur)
        check_button.grid(column = 1, row = 10)



        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 1, row = 15)

class film_2(tk.Frame):

    def __init__(self, parent, controller):
        film_naam = (film_dict['filmsoptv']['film'][1]['titel'])
        tk.Frame.__init__(self, parent)

        def save_user():
            global unieke_code
            unieke_code = random.randrange(10000000, 100000000)
            name = entry1.get()
            mail = entry2.get()
            film_naam = (film_dict['filmsoptv']['film'][1]['titel'])
            starttijd = (film_dict['filmsoptv']['film'][1]['starttijd'])
            code = unieke_code
            bestand = "jeroen_films.csv"
            file = open(bestand, 'a', newline='')
            fieldnames = ['Naam', 'mail', 'film', 'starttijd', 'code']
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writerow({'Naam':name, 'mail':mail, 'film':film_naam, 'starttijd':starttijd, 'code':code})
            messagebox.showinfo(film_naam, ("Uw film is gereserveerd!\nGebruik aub de volgende code: " + str(code)))

        label = tk.Label(self, text=(film_dict['filmsoptv']['film'][1]['titel']), font=font_title)
        label.grid(column = 1, row = 0)
        jaar_label = tk.Label(self, text= ("Jaar van uitgave: " + film_dict['filmsoptv']['film'][1]['jaar']), font=font_small)
        jaar_label.grid(column = 1, row = 2)
        samenvatting_label = tk.Label(self, text= ("Samenvatting: " + film_dict['filmsoptv']['film'][1]['synopsis']), font=font_small, wraplength = 500)
        samenvatting_label.grid(column = 1, row = 3)
        filmduur_label = tk.Label(self, text= ("Filmduur: " + film_dict['filmsoptv']['film'][1]['duur'] + " minuten"), font=font_small)
        filmduur_label.grid(column = 1, row = 4)
        zender_label = tk.Label(self, text= ("Te zien op zender: " + film_dict['filmsoptv']['film'][1]['zender']), font=font_small)
        zender_label.grid(column = 1, row = 5)



        entry_label1 = tk.Label(self, text="Naam", font=font_medium)
        entry_label1.grid(column = 0, row = 8)
        entry1 = tk.Entry(self)
        entry1.grid(column = 1, row = 8)

        entry_label2 = tk.Label(self, text="E-mail", font=font_medium)
        entry_label2.grid(column = 0,  row = 9)
        entry2 = tk.Entry(self)
        entry2.grid(column = 1, row = 9)

        check_button = tk.Button(self, text="Huur!", command=save_user, font=font_huur)
        check_button.grid(column = 1, row = 10)
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 1, row = 15)

class film_3(tk.Frame):

    def __init__(self, parent, controller):
        film_naam = (film_dict['filmsoptv']['film'][2]['titel'])
        tk.Frame.__init__(self, parent)

        def save_user():
            global unieke_code
            unieke_code = random.randrange(10000000, 100000000)
            name = entry1.get()
            mail = entry2.get()
            film_naam = (film_dict['filmsoptv']['film'][2]['titel'])
            starttijd = (film_dict['filmsoptv']['film'][2]['starttijd'])
            code = unieke_code
            bestand = "daan_films.csv"
            file = open(bestand, 'a', newline='')
            fieldnames = ['Naam', 'mail', 'film', 'starttijd', 'code']
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writerow({'Naam':name, 'mail':mail, 'film':film_naam, 'starttijd':starttijd, 'code':code})
            messagebox.showinfo(film_naam, ("Uw film is gereserveerd!\nGebruik aub de volgende code: " + str(code)))

        label = tk.Label(self, text=(film_dict['filmsoptv']['film'][2]['titel']), font=font_title)
        label.grid(column =1, row = 0)
        jaar_label = tk.Label(self, text= ("Jaar van uitgave: " + film_dict['filmsoptv']['film'][2]['jaar']), font=font_small)
        jaar_label.grid(column =1, row = 2)
        samenvatting_label = tk.Label(self, text= ("Samenvatting: " + film_dict['filmsoptv']['film'][2]['synopsis']), font=font_small, wraplength = 500)
        samenvatting_label.grid(column =1, row = 3)
        filmduur_label = tk.Label(self, text= ("Filmduur: " + film_dict['filmsoptv']['film'][2]['duur'] + " minuten"), font=font_small)
        filmduur_label.grid(column =1, row = 4)
        zender_label = tk.Label(self, text= ("Te zien op zender: " + film_dict['filmsoptv']['film'][2]['zender']), font=font_small)
        zender_label.grid(column = 1, row = 5)



        entry_label1 = tk.Label(self, text="Naam", font=font_medium)
        entry_label1.grid(column = 0, row = 8)
        entry1 = tk.Entry(self)
        entry1.grid(column = 1, row = 8)

        entry_label2 = tk.Label(self, text="E-mail", font=font_medium)
        entry_label2.grid(column = 0,  row = 9)
        entry2 = tk.Entry(self)
        entry2.grid(column = 1, row = 9)

        check_button = tk.Button(self, text="Huur!", command=save_user, font=font_huur)
        check_button.grid(column = 1, row = 10)
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 1, row = 15)

class film_4(tk.Frame):

    def __init__(self, parent, controller):
        film_naam = (film_dict['filmsoptv']['film'][3]['titel'])
        tk.Frame.__init__(self, parent)

        def save_user():
            global unieke_code
            unieke_code = random.randrange(10000000, 100000000)
            name = entry1.get()
            mail = entry2.get()
            film_naam = (film_dict['filmsoptv']['film'][3]['titel'])
            starttijd = (film_dict['filmsoptv']['film'][3]['starttijd'])
            code = unieke_code
            bestand = "daan_films.csv"
            file = open(bestand, 'a', newline='')
            fieldnames = ['Naam', 'mail', 'film', 'starttijd', 'code']
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writerow({'Naam':name, 'mail':mail, 'film':film_naam, 'starttijd':starttijd, 'code':code})
            messagebox.showinfo(film_naam, ("Uw film is gereserveerd!\nGebruik aub de volgende code: " + str(code)))

        label = tk.Label(self, text=(film_dict['filmsoptv']['film'][3]['titel']), font=font_title)
        label.grid(column = 1, row = 0)
        jaar_label = tk.Label(self, text= ("Jaar van uitgave: " + film_dict['filmsoptv']['film'][3]['jaar']), font=font_small)
        jaar_label.grid(column =1, row = 2)
        samenvatting_label = tk.Label(self, text= ("Samenvatting: " + film_dict['filmsoptv']['film'][3]['synopsis']), font=font_small, wraplength = 500)
        samenvatting_label.grid(column = 1, row = 3)
        filmduur_label = tk.Label(self, text= ("Filmduur: " + film_dict['filmsoptv']['film'][3]['duur'] + " minuten"), font=font_small)
        filmduur_label.grid(column = 1, row = 4)
        zender_label = tk.Label(self, text= ("Te zien op zender: " + film_dict['filmsoptv']['film'][3]['zender']), font=font_small)
        zender_label.grid(column = 1, row = 5)



        entry_label1 = tk.Label(self, text="Naam", font=font_medium)
        entry_label1.grid(column = 0, row = 8)
        entry1 = tk.Entry(self)
        entry1.grid(column = 1, row = 8)

        entry_label2 = tk.Label(self, text="E-mail", font=font_medium)
        entry_label2.grid(column = 0,  row = 9)
        entry2 = tk.Entry(self)
        entry2.grid(column = 1, row = 9)

        check_button = tk.Button(self, text="Huur!", command=save_user)
        check_button.grid(column = 1, row = 10)
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 1, row = 15)

class film_5(tk.Frame):

    def __init__(self, parent, controller):
        film_naam = (film_dict['filmsoptv']['film'][4]['titel'])
        tk.Frame.__init__(self, parent)

        def save_user():
            global unieke_code
            unieke_code = random.randrange(10000000, 100000000)
            name = entry1.get()
            mail = entry2.get()
            film_naam = (film_dict['filmsoptv']['film'][4]['titel'])
            starttijd = (film_dict['filmsoptv']['film'][4]['starttijd'])
            code = unieke_code
            bestand = "rick_films.csv"
            file = open(bestand, 'a', newline='')
            fieldnames = ['Naam', 'mail', 'film', 'starttijd', 'code']
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writerow({'Naam':name, 'mail':mail, 'film':film_naam, 'starttijd':starttijd, 'code':code})
            messagebox.showinfo(film_naam, ("Uw film is gereserveerd!\nGebruik aub de volgende code: " + str(code)))

        label = tk.Label(self, text=(film_dict['filmsoptv']['film'][4]['titel']), font=font_title)
        label.grid(column = 1, row = 0)
        jaar_label = tk.Label(self, text= ("Jaar van uitgave: " + film_dict['filmsoptv']['film'][4]['jaar']), font=font_small)
        jaar_label.grid(column = 1, row = 2)
        samenvatting_label = tk.Label(self, text= ("Samenvatting: " + film_dict['filmsoptv']['film'][4]['synopsis']), font=font_small, wraplength = 500)
        samenvatting_label.grid(column = 1, row = 3)
        filmduur_label = tk.Label(self, text= ("Filmduur: " + film_dict['filmsoptv']['film'][4]['duur'] + " minuten"), font=font_small)
        filmduur_label.grid(column = 1, row = 4)
        zender_label = tk.Label(self, text= ("Te zien op zender: " + film_dict['filmsoptv']['film'][4]['zender']), font=font_small)
        zender_label.grid(column = 1, row = 5)
 
 
 
        entry_label1 = tk.Label(self, text="Naam", font=font_medium)
        entry_label1.grid(column = 0, row = 8)
        entry1 = tk.Entry(self)
        entry1.grid(column = 1, row = 8)
 
        entry_label2 = tk.Label(self, text="E-mail", font=font_medium)
        entry_label2.grid(column = 0,  row = 9)
        entry2 = tk.Entry(self)
        entry2.grid(column = 1, row = 9)
 
        check_button = tk.Button(self, text="Huur!", command=save_user, font=font_huur)
        check_button.grid(column = 1, row = 10)
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 1, row = 15)
 
class film_6(tk.Frame):
 
    def __init__(self, parent, controller):
        film_naam = (film_dict['filmsoptv']['film'][5]['titel'])
        tk.Frame.__init__(self, parent)
 
        def save_user():
            global unieke_code
            unieke_code = random.randrange(10000000, 100000000)
            name = entry1.get()
            mail = entry2.get()
            film_naam = (film_dict['filmsoptv']['film'][5]['titel'])
            starttijd = (film_dict['filmsoptv']['film'][5]['starttijd'])
            code = unieke_code
            bestand = "rick_films.csv"
            file = open(bestand, 'a', newline='')
            fieldnames = ['Naam', 'mail', 'film', 'starttijd', 'code']
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writerow({'Naam':name, 'mail':mail, 'film':film_naam, 'starttijd':starttijd, 'code':code})
            messagebox.showinfo(film_naam, ("Uw film is gereserveerd!\nGebruik aub de volgende code: " + str(code)))
 
        label = tk.Label(self, text=(film_dict['filmsoptv']['film'][5]['titel']), font=font_title)
        label.grid(column = 1, row = 0)
        jaar_label = tk.Label(self, text= ("Jaar van uitgave: " + film_dict['filmsoptv']['film'][5]['jaar']), font=font_small)
        jaar_label.grid(column = 1, row = 2)
        samenvatting_label = tk.Label(self, text= ("Samenvatting: " + film_dict['filmsoptv']['film'][5]['synopsis']), font=font_small, wraplength = 500)
        samenvatting_label.grid(column = 1, row = 3)
        filmduur_label = tk.Label(self, text= ("Filmduur: " + film_dict['filmsoptv']['film'][5]['duur'] + " minuten"), font=font_small)
        filmduur_label.grid(column = 1, row = 4)
        zender_label = tk.Label(self, text= ("Te zien op zender: " + film_dict['filmsoptv']['film'][5]['zender']), font=font_small)
        zender_label.grid(column = 1, row = 5)
 
 
 
        entry_label1 = tk.Label(self, text="Naam", font=font_medium)
        entry_label1.grid(column = 0, row = 8)
        entry1 = tk.Entry(self)
        entry1.grid(column = 1, row = 8)
 
        entry_label2 = tk.Label(self, text="E-mail", font=font_medium)
        entry_label2.grid(column = 0,  row = 9)
        entry2 = tk.Entry(self)
        entry2.grid(column = 1, row = 9)
 
        check_button = tk.Button(self, text="Huur!", command=save_user, font=font_huur)
        check_button.grid(column = 1, row = 10)
        button = tk.Button(self, text="Ga terug naar 'Home'",
                           command=lambda: controller.show_frame(StartPage), font=font_medium)
        button.grid(column = 1, row = 15)
 
 
if __name__ == "__main__":
    app = HomeCinema()
    w, h = app.winfo_screenwidth(), app.winfo_screenheight()
    app.geometry("%dx%d+0+0" % (w, h))
    app.mainloop()