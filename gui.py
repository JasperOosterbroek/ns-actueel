from tkinter import *
from tkinter import ttk
from apimanagement import apiManagement as Api
import xmltodict
import datetime


class Gui:
    """The gui system
    """

    def __init__(self, master):
        """Initializes the frames and the api"""
        self.nsapi = Api()
        self.settings = self.getsettings()
        self.master = master
        self.master.resizable(False, False)
        self.homepng = PhotoImage(file="NS.png")
        self.cleanpng = PhotoImage(file="NSClean.png")
        self.gobackpng = PhotoImage(file="home.png")
        self.background = Label(image=self.homepng)
        self.background.grid(row=0, column=0)
        # all frames need to be made in the init
        self.homepageframe = Frame(self.master, background="#feca24")
        self.testframe = Frame(self.master)
        self.gotoframe = Frame(self.master)
        self.travelinformationframe = Frame(self.master)
        self.interferenceframe = Frame(self.master)
        self.gohomeframe = Frame(self.master)
        # build first page
        self.buildhomepage()

    @staticmethod
    def getsettings():
        """
        writes the settings from file to dictionary

        :return: The settings as an ordered dictionary
        """
        with open('settings.xml') as settingsFile:
            return xmltodict.parse(settingsFile.read())

    @staticmethod
    def clearframe(frame):
        """
        clear's specified frame

        :param frame: The frame that needs to be removed
        """
        for widget in frame.winfo_children():
            widget.pack_forget()
            widget.grid_forget()
        frame.destroy()

    def changeframe(self, currentframe, newframe):
        """
        Change to desired frame

        :param currentframe: The frame that the function is called in
        :param newframe: The name of the frame the code has to change to
        """
        self.clearframe(currentframe)
        if newframe == 'storing':
            self.interferenceframe = Frame(self.master, background="#feca24")
            self.buildinterference()
        elif newframe == 'homepage':
            self.homepageframe = Frame(self.master, background="#feca24")
            self.buildhomepage()
            self.clearframe(self.gohomeframe)
        elif newframe == 'goto':
            self.gotoframe = Frame(self.master, background="#feca24")
            self.buildgoto()
        elif newframe == 'reisinformatie':
            self.travelinformationframe = Frame(self.master, background="#feca24")
            self.buildtravelinformation()

    def buildhomepage(self):
        """
        function that builds the homepage ui
        """
        self.homepageframe.grid(row=0, column=0, columnspan=1, )
        self.background.config(image=self.homepng)
        Button(self.homepageframe, text='Ik wil naar \nAmsterdam', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic'), command=lambda: self.changeframe(self.homepageframe, 'goto')).grid(row=0, column=0, padx=20, )
        Button(self.homepageframe, text='Kopen \n los kaartje', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=1, padx=20)
        Button(self.homepageframe, text='Kopen \n OV-Chipkaart', background='#493782', foreground="#fff", height=3, width=12,
               font=('Helvetica', 10, 'bold italic')).grid(row=0, column=2, padx=20)
        Button(self.homepageframe, text='Ik wil naar \nhet buitenland', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic')).grid(row=0, column=3, padx=20)
        Button(self.homepageframe, text='Reisinformatie \nopvragen', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic'), command=lambda: self.changeframe(self.homepageframe, 'reisinformatie')).grid(row=0, column=4, padx=20)
        Button(self.homepageframe, text='storingen \nopvragen', background='#493782', foreground="#fff", height=3,
               width=12, font=('Helvetica', 10, 'bold italic'),
               command=lambda: self.changeframe(self.homepageframe, 'storing')).grid(row=0, column=5, padx=20)
        self.homepageframe.place(y=500, x=35)

    def buildgoto(self):
        """
        function that builds the goto ui
        """
        self.buildgohome(self.gotoframe)
        self.background.config(image=self.cleanpng)
        fromstation = self.settings['settings']['station']
        gotostation = self.settings['settings']['goto']
        Label(self.gotoframe, text="De volgende trein naar station " + gotostation + ':', background="#feca24", foreground="#00236a", font=("Arial", 12)).grid(row=0, column=0)
        self.gotoframe.place(y=352, x=467, anchor="center")
        options = self.nsapi.getroute(fromstation, gotostation)
        if options != 'error':
            for reis in options['ReisMogelijkheden']['ReisMogelijkheid']:
                if reis['Optimaal'] == 'true':
                    actuelevetrektijd = self.fixtime(reis['ActueleVertrekTijd'], 'time')
                    actueleaankomstijd = self.fixtime(reis['ActueleAankomstTijd'], 'time')
                    reisdeel = reis['ReisDeel']
                    spoorstart = reisdeel['ReisStop'][0]['Spoor']['#text']
                    spoorend = reisdeel['ReisStop'][-1]['Spoor']['#text']
                    reisinfo = "gaat om {} vanaf spoor {} op station {}.\nDeze trein zal aankomen op station {} om {} op spoor {}.".format(actuelevetrektijd, spoorstart, fromstation, gotostation,actueleaankomstijd, spoorend)
                    Label(self.gotoframe, text=reisinfo, background='#feca24').grid(row=1, column=0)
        else:
            self.popupmsg('er is iets fout gegaan probeer het opnieuw\nAls de error aan blijft houden neem contact op met een ns medewerker.')
            self.changeframe(self.gotoframe, 'homepage')

    def buildgohome(self, currentframe):
        """
        function that builds the home button

        :param currentframe: the current frame the button is build in
        """
        self.gohomeframe = Frame(self.master, background="#00236a")
        self.gohomeframe.grid(row=0, column=0, columnspan=1, )
        Button(self.gohomeframe, image=self.gobackpng, height=34, width=34, borderwidth=0, cursor="man", command=lambda: self.changeframe(currentframe, 'homepage')).grid(row=0, column=0, padx=20, )
        self.gohomeframe.place(y=664, x=40)

    def buildtravelinformation(self):
        """
        function to build the reisinformatie ui
        """
        #frame settings
        self.travelinformationframe.grid(row=0, column=0)
        self.buildgohome(self.travelinformationframe)
        self.background.config(image=self.cleanpng)
        #label settings
        station = self.settings['settings']['station']
        Label(self.travelinformationframe, anchor=W ,text='Selecteer station:', background='#feca24', foreground="#00236a", font=("Arial", 12)).grid(row=0, column=0)
        travelinfolabel = Label(self.travelinformationframe, justify=LEFT ,text='Actuele reis informatie station {}'.format(station), background='#feca24', foreground="#00236a", font=("Arial", 12))
        travelinfolabel.grid(row=0, column=2)
        # get the column values
        columnvalues = self.settings['settings']['layout']['table']['rijsinformatie']['columns'].values()
        columnnames = tuple(item for sublist in columnvalues for item in sublist)
        # get all values for station (the select)
        stations = self.nsapi.getstationlijst()
        if stations != 'error':
            # building table and scrollbar using api data
            # configure table
            table = ttk.Treeview(self.travelinformationframe, columns=columnnames)
            table.grid(row=1, column=2)
            table['show'] = 'headings'
            # configure select
            select = Listbox(self.travelinformationframe)
            select.grid(row=1, column=0, sticky=N+S+W+E)
            select.bind('<<ListboxSelect>>', lambda e: self.selectstation(e, table,travelinfolabel))
            # configure table scroll
            tablescroll = ttk.Scrollbar(self.travelinformationframe, orient="vertical", command=table.yview)
            tablescroll.grid(row=1, column=3, sticky=N+S+W)
            # configure selectscroll
            selectscroll = ttk.Scrollbar(self.travelinformationframe, orient="vertical", command=select.yview)
            selectscroll.grid(row=1, column=1, sticky=N+S+W)
            # link scrolls
            table.configure(yscrollcommand=tablescroll.set)
            select.configure(yscrollcommand=selectscroll.set)
            # fill select
            for stationrow in stations['Stations']['Station']:
                if stationrow['Land'] == 'NL':
                    select.insert(END, stationrow['Namen']['Middel'])
            self.populatetravelinfotable(table, station)
        else:
            self.popupmsg('er is iets fout gegaan probeer het opnieuw\nAls de error aan blijft houden neem contact op met een ns medewerker.')
            self.changeframe(self.travelinformationframe, 'homepage')

    def buildinterference(self):
        """
        function that builds the interferences ui and fills it with data
        """
        self.interferenceframe.grid(row=0, column=0)
        self.buildgohome(self.interferenceframe)
        self.background.config(image=self.cleanpng)
        station = self.settings['settings']['station']
        data = self.nsapi.getstoring()
        if data['Storingen']['Gepland'] == None and data['Storingen']['Ongepland'] == None:
            Label(self.interferenceframe, justify=LEFT ,text='Er zijn geen storingen', background='#feca24', foreground="#00236a", font=("Arial", 12)).grid(row=1,column=1)
        else:
            # configure title
            Label(self.interferenceframe,text='Storingen', background='#feca24', foreground="#00236a", font=("Arial", 12)).grid(row=0,column=0)
            # configure textfield
            textfield = Text(self.interferenceframe, wrap=WORD,background='#feca24',borderwidth=0)
            textfield.grid(row=1, column=0)
            # configure table scroll
            textscroll = ttk.Scrollbar(self.interferenceframe, orient="vertical", command=textfield.yview)
            textscroll.grid(row=1, column=1, sticky=N + S + W)
            # check if there are planned interferences
            if data['Storingen']['Gepland']!= None:
                plannedinterferences = data['Storingen']['Gepland']
                textfield.insert(INSERT,'Gepland\n','a')
                if type(plannedinterferences['Storing']) == list:
                    for value in plannedinterferences['Storing']:
                        cleanmessage = self.removehtmlmarkup(value['Bericht'])
                        text = '\nTraject:{}\n{}\n\n'.format(value['Traject'],cleanmessage)
                        textfield.insert(INSERT,text,'a')
                else:
                    for value in plannedinterferences.values():
                        cleanmessage = self.removehtmlmarkup(value['Bericht'])
                        text = '\nTraject:{}\n{}\n\n'.format(value['Traject'], cleanmessage)
                        textfield.insert(INSERT, text, 'a')
            # check if there are unplanned interferences
            if data['Storingen']['Ongepland'] != None:
                unplannedinterferences = data['Storingen']['Ongepland']
                textfield.insert(INSERT, 'Ongepland\n', 'a')
                if type(unplannedinterferences['Storing']) == list:
                    for value in unplannedinterferences['Storing']:
                        cleanmessage = self.removehtmlmarkup(value['Bericht'])
                        text = '\nTraject:{}\n{}\n\n'.format(value['Traject'],cleanmessage)
                        textfield.insert(INSERT, text, 'a')
                else:
                    for value in unplannedinterferences.values():
                        cleanmessage = self.removehtmlmarkup(value['Bericht'])
                        text = '\nTraject:{}\n{}\n\n'.format(value['Traject'], cleanmessage)
                        textfield.insert(INSERT, text, 'a')
            textfield.config(state=DISABLED)

    def selectstation(self, evt, table, label):
        """
        This function gets an event and changes the table

        :param  evt: variable trown by the .bind function
        :param  table: the table that has to change
        :param  label: the label to make the text change
        """
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.populatetravelinfotable(table, value)
        label.config(text='Actuele reis informatie station {}'.format(value))

    def populatetravelinfotable(self, table, station):
        """
        function to populate the travelinfo table with values

        :param  table: the table that needs to change
        :param  station: the station that is used by the api
        """
        # empty current table
        table.delete(*table.get_children())
        # get all values for the table and transform them in tuples
        columnvalues = self.settings['settings']['layout']['table']['rijsinformatie']['columns'].values()
        rowvalues = self.settings['settings']['layout']['table']['rijsinformatie']['values'].values()
        columns = tuple(item for sublist in columnvalues for item in sublist)
        rows = tuple(item for sublist in rowvalues for item in sublist)
        # fill empty table
        for column in columns:
            table.heading(column, text=column)
            table.column(column, stretch=True, width=100)
        data = self.nsapi.getvertrektijden(station)
        #check if the api did not throw an error
        if data != 'error':
            for row in data['ActueleVertrekTijden']['VertrekkendeTrein']:
                rowlist = list()
                for value in rows:
                    if "|" in value:
                        splitvalue = value.split('|')
                        rowlist.append(row[splitvalue[0]][splitvalue[1]])
                    elif value == 'VertrekTijd':
                        # Format the given date back to a datetimeobject, from which we can construct our own format
                        strdisplaytime = self.fixtime(row['VertrekTijd'])
                        rowlist.append(strdisplaytime)
                    elif value == 'VertrekVertragingTekst':
                        # check if there is a delay
                        if 'VertrekVertragingTekst' in row:
                            rowlist.append(row[value])
                        else:
                            rowlist.append("")
                    else:
                        rowlist.append(row[value])
                table.insert('', 'end', values=rowlist)
        else:
            self.popupmsg('er is iets fout gegaan probeer het opnieuw\nAls de error aan blijft houden neem contact op met een ns medewerker.')

    @staticmethod
    def fixtime(time, timetype='full'):
        """
        This function fixed the nsapi time

        :param time: the time that needs to be fixed
        :param timetype: define what kind of return type you want

        :return: The formatted displaytime string
        """
        if timetype == 'full':
            datetimeobject = datetime.datetime.strptime(str(time), '%Y-%m-%dT%H:%M:%S%z')
            displaytime = datetime.datetime.strftime(datetimeobject, '%Y-%m-%d %H:%M')
            return displaytime
        elif timetype == 'time':
            datetimeobject = datetime.datetime.strptime(str(time), '%Y-%m-%dT%H:%M:%S%z')
            displaytime = datetime.datetime.strftime(datetimeobject, '%H:%M')
            return displaytime
        else:
            return 'Er is iets fout gegaan probeer het opnieuw!'

    @staticmethod
    def popupmsg(msg):
        """
        This function generates an error popup window
        """
        popup = Tk()
        popup.wm_title("Error")
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        b1 = ttk.Button(popup, text="Oke", command=popup.destroy)
        b1.pack()
        popup.mainloop()

    @staticmethod
    def removehtmlmarkup(htmltxt):
        """
        This function clears the nsapi text from html tags

        :param htmltxt: The text that needs its html tags removed
        :return: The formatted input
        """
        output = ""
        tag = False
        quote = False

        for text in htmltxt:
                if text == '<' and not quote:
                    tag = True
                elif text == '>' and not quote:
                    tag = False
                elif (text == '"' or text == "'") and tag:
                    quote = not quote
                elif not tag:
                    output = output + text
        return output

root = Tk()
root.title("NS")
gui = Gui(root)

root.mainloop()
