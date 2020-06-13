# Raport 1

### Środowisko 
Środowiskiem agenta jest plansza (mapa magazynu), która jest podzielona na pola. Każde pole może być puste lub zajęte. 
Agent może się poruszać tylko po polach pustych. Na polach zajętych znajdują się regały, na których przechowywane jest towar. Regały są zaznaczone za pomocą funkcji `pokolorujRegaly()`
Plansza ma wymiar 11 kolumn indeksowanych od 0 do 11 i 7 wierszy indeksowanych od 0 do 6. Pola mogą być ponumerowane dzięki funkcji `ponumerujPola()`.

### Agent

Agent jest reprezentowany za pomocą klasy `Agent`.
Agent jest wyświetlany na planszy przy użyciu ikony wózka widłowego (`umiescAgenta()`). 
Agent porusza się po dzięki metodzie `przemieszczenie()`, która najpierw usuwa agenta z planszy (funkcja: `usunAgenta()`) nasępnie przesuwa go metodami `right()`, `left()`, 
`up()`, `down()` i umieszcza go na nowej pozycji (funkcja: `umiescAgenta()`). Droga agenta jest ustala funkcją `droga()`.Przykład drogi agenta https://youtu.be/RLe2ZN5SFLo.

### Reprezentacja wiedzy

Klasa `Field` - reprezentuje pola w magazynie. Posiada pola:
- `x` - współrzędna x
- `y` - współrzędna y
- `isEmpty` - określa czy pole jest puste, czy nie.

<br>

Klasa `Product` - reprezentuje poszczególne produkty znajdujące się w magazynie. Posiada pola:
- `name` - nazwa produktu
- `type` - rodzaj produktu
- `specs` - krótki opis produktu
- `price` - cena produktu

<br>

Klasa `Rack` - reprezentuje regały, które znajdują się w magazynie. Na jednym regale mogą znajdować się pordukty tego samego typu. Posiada pola:
- `noOfShelf` - liczbę półek danego regału 


Metody:
- `addShelf()` - dodającą półkę do regału
- `isEmpty()` - zwracającą **true**, jeśli regał nie ma żadnych półek lub **false** w przeciwnym wypadku

<br>

Klasa `Shelf` - reprezentuje półkę, w regale. Na jednej półce mogą znajdować się produkty o tej samej specyfikacji. Posiada pola:
- `number` - numer półki
- `typOfProduct` - rodzaj produktu, jaki znajduję się na półce