# Assignment-2-Pig-Game
Detta projekt har utvecklats som en del av uppgiften Assignment 2 – Test Driven Development. Syftet är att visa hur testdriven utveckling (TDD) och objektorienterad programmering (OOP) kan användas för att skapa ett robust och välstrukturerat Python-program.

Applikationen är ett terminalbaserat spel baserat på den klassiska tärningsleken Pig. Spelarna turas om att kasta en tärning och samlar poäng. Om en etta kastas förloras alla rundpoäng, men spelaren kan välja att ”hålla” och spara sina poäng. Den första spelaren som når 100 poäng vinner spelet.

Programmet är uppdelat i flera klasser: Dice hanterar tärningskast, Player representerar varje spelares namn och poäng, Game styr spelets logik och turordning, och main.py fungerar som startpunkt. Varje klass ligger i en egen fil för att uppfylla principerna i OOP.

Spelet körs direkt i terminalen med kommandot python main.py. När spelet startar får spelarna ange sina namn och turas om att spela tills någon uppnår 100 poäng.

Projektet har utvecklats med fokus på ren kod enligt PEP 8 och testbarhet med unittest. Tester körs med make test och täckningsrapport genereras med make coverage. Kodkvaliteten säkerställs med pylint och flake8. Dokumentationen skapas automatiskt med Sphinx, medan UML-diagram genereras med pyreverse och sparas under doc/uml. Projektet är licensierat under MIT-licensen och kan fritt användas och vidareutvecklas.


UML Diagram
![UML Diagram](/docs/UML.jpeg)
