# NS kaartmachine upgrade

In dit project is het kaartjessysteem van de ns verbeterd door het toevoegen van nieuwe functies.
De volgende functies zijn toegevoegd
1. Actuele storingen bekijken
2. Beste tijd krijgen om naar een voorafgedefineerd station te gaan
3. Actuele vertrijktijden van alle treinen op een geselecteerd station

## Configuratie

Er moeten een paar aanpassingen worden gemaakt om het product aftestemmen voor het huidige station

In het bestand settings.xml moeten het huidige station en het station voor de ik wil naar knop


```
    <station>
        Utrecht centraal
    </station>
    <goto>
        Amsterdam
    </goto>
```

Als dit is gedaan kan het programma worden opgestart

```
python3 gui.py
```
