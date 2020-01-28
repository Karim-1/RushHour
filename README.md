# RushHour

Rush Hour is een spel dat bestaat uit een vierkant bord van 6x6, 9x9 of 12x12 vakjes. Het doel van het spel is om auto te verplaatsen zodat de rode auto (auto 'X' in de board csv file) het bord uit kan.

## Vereisten

De code is volledig geschreven in Python 3.7. Om de code te runnen moet matplotlib geinstalleerd worden. Dit kan d.m.v. de volgende code:

```
pip install -r requirements.txt
```

## Gebruik
Al onze code wordt gerund vanuit main.py.

```
python main.py
```

Momenteel is veel v.d. code uitgecomment en wordt alleen het het eerste bord gerunt met het random algoritme. Om alle algoritmes te runnen moeten delen code "ge-uncommment" worden. Zie main.py voor instructies met welke code "uncomment" moet worden om een bepaald algoritme te runnen.

## Algoritmes
Vanuit main.py kunnen de volgende vier algoritmes gerund worden:
- Randomize algorithme
  - Deze functie oplossing a.d.h.v. willekeurige bewegingen van willekeurige auto's.
- Cut algorithme
  - Het "cut algoritme" is een verbetering van het randomize algoritme. Het cut algoritme deelt de oplossing van het randomize algoritme op in stukjes en gaat voor elk van deze stukjes 1000 maal proberen een willekeurige snellere oplossing te vinden. Als dit niet lukt behoudt het algoritme de oude stappen.
  - Om het algoritme te runnen moet een "divider" meegegeven worden. In het main.py bestand is dit momenteel 10, wat inhoudt dat een oplossing van randomize in 10 stappen wordt verdeeld. Deze kan aangepast worden naar wens. Hoe hoger deze divider is, hoe intensiever het genereren van een oplossing voor je computer is.
- Breadthfirst search (BFS) algorithme
  - Het Breadthfirst search algorithme vindt de oplossing voor het RushHour probleem met de minste stapjes. Om hier te komen genereert de code alle mogelijke states waarin de borden zich kunnen bevinden. Dit gebeurt van links naar rechts. Het algoritme stopt pas als er een uitkomst is gevonden. Het kost erg veel tijd om al deze mogelijke statespaces te genereren. Daardoor is het alleen mogelijk om de 6x6 bordjes op een fijne manier met dit algoritme op te lossen.
- Random BFS
  - Dit algoritme is een combinatie van het BFS-, cut- en randomize algoritme. Dit algoritme zoekt het optimale resultaat voor kleine stukjes van het randomize algoritme.
  - T.o.v. van het BFS algoritme vindt dit algoritme een suboptimaal resultaat. Wel zorgt dit algoritme ervoor dat er een stuk minder computaties uitgevoerd hoeven te worden door de computer. Hierdoor kan met dit algoritme een "redelijk" resultaat gevonden worden voor het 12x12 bord, waar het met het BFS algoritme veel te lang kan duren voordat een oplossing wordt gevonden.

## Aanpak

*Randomize*
Dit algoritme kiest een willekeurige negatief of positief getal tussen de lengte van het bord - 1. Dit getal representeert een beweging. Zo betekent "-1" bij een horizontale auto dat de auto één stap naar links doet. Een willekeurige auto op het bord. Het algoritme blijft de auto's bewegen totdat de win conditie behaald is.

*Cut*
Dit algoritme genereert een oplossing met het randomize algoritme. Vervolgens worden de stappen opgedeeld in stukken o.b.v. de "divider". Dus als randomize een oplossing heeft gevonden in 200 stappen en de divider is 10, worden de stappen opgedeeld in 20 stappen per keer.  

Vervolgens wordt er een for loop gerund voor elke 20 stappen van de originele oplossing. Daarbij is het doel om in minder dan 20 stappen hetzelfde bord te bereiken als het hoe het bord eruitzag in de originele oplossing bij de 20e stap. Hoe dit bord eruitzag wordt het "goal_board" genoemd.

Het algoritme krijgt hiervoor 1000 pogingen, om te voorkomen dat het algoritme voor eeuwig doorloopt. Als er een snellere route naar het "goal_board" wordt gevonden worden deze stappen opgeslagen in een lijst. Zo niet, worden de 20 stappen van de originele oplossing behouden.

Dit wordt gedaan voor elke 20 stappen, uiteindelijk zal de nieuwe oplossing bijna altijd korter zijn dan de originele oplossing.



## Structuur

Hieronder is een lijst te vinden met de indeling van onze map-structuur.

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de classes waar de algoritmes gebruik van maken.
  - **/code/helpers**: bevat een aantal "hulp" functies voor de classes en algoritmes.
- **/gameboards**: bevat de 7 verschillende spelborden om het algoritme op te laten werken.

## Auteurs
- Lulu Kroon
- Karim Semin
- Siri Zomerplaag
