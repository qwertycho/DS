# SQLytics

## usage guide
Gebruik de importer.ipynb notebook om een sqlite database aan te maken die gebruikt kan worden voor analyse.
Voor dit script zijn er 3 bestanden nodig:

1. `OrderLines.csv` Dit is de ruwe orderlines dataset, met een komma gescheiden.
2. `ProductInfo.csv` Dit is de ruwe productinfo dataset, met een puntkomma gescheiden.
3. `known_alias.json` Dit json bestand bevat correcties voor de producten in de orderlines dataset.

Run het script van boven naar beneden. 
Het script maakt automatisch een `test.db` sqlite database aan (of een andere als de naam is veranderd).
Als dat bestand al bestaat worden de gegevens geimporteerd.