# Raport 2

### Definicja pętli głownej strategi przeszukiwania
Naszą główną funkcją jest funkcja `aStar(startField, goalField)`, przyjmuje ona dwa argumenty: `startField` - pole z którego wyrusza agent `goalField` - cel drogi agenta. Zwraca ona ścieżkę z `startField` do `goalField`.

#### Opis

`closedSet` - lista zawierająca sprawdzane i sprawdzone pola z listy `openSet`

`openSet` - lista zawierająca pola do sprawdzenia 

`path` - lista zawierająca pola tworzące ścieżkę do wybranego celu

<br>

- Dodajemy pierwszy element który będziemy sprawdzać do listy openSet: `openSet.push(startField);`
- Kolorujemy punkt startowy na zielono: `colorGreen(startField, animationFrame);`
- Dopóki lista `openSet` nie bedzie pusta sprawdzamy jej elementy: `while(openSet.length > 0)`
- Wybieramy najbardziej obiecujący element z zbioru `openSet`:

```javascript
let winner = 0;
for(let i = 0; i < openSet.length; i++){
    if (openSet[i].f < openSet[winner].f){
        winner = i
    }
}

let current = openSet[winner];
```
- Jeśli pole `current` okaże się naszym celem tworzymy ścieżkę z punktu startowego do naszego celu.

```javascript
if(current === goalField){
    path = []
    var temp = current;
    path.push(temp);
    while(temp.previous){
    path.push(temp.previous);
    temp = temp.previous
}
```
- Następnie kolorujemy tą ścieżkę i kończymy funkcję zwracając ścieżkę `path`

```javascript
for(var i = 0; i < path.length; i++){
    animationFrame = colorYellow(path[i], animationFrame);
}
return path;
```
- Jeśli pole `current` nie jest naszym celem, to usuwamy je z listy `openSet`, dodajemy do listy `closedSet` oraz kolorujemy je na czerwono.

```javascript
removeFromSet(openSet, current);
closedSet.push(current);
animationFrame = colorRed(current, animationFrame);
```
- Pobieramy sąsiadów pola `current`: `var neighbors = current.neighbors;`
- Dla każdego sąsiada obliczamy koszt dotarcia do niego z punktu początkowego najlepszą ścieżką.

```javascript
for(var i = 0; i < neighbors.length; i++){
    var neighbor = neighbors[i];
    if(!closedSet.includes(neighbor)){
        var tempG = current.gScore + neighbor.costOfTravel;
        if(openSet.includes(neighbor)){
            if(tempG < neighbor.gScore){
                neighbor.gScore = tempG;
            }
        } else {
            neighbor.g = tempG;
            openSet.push(neighbor);
            animationFrame = colorGreen(neighbor,animationFrame);
        }
```
- Po przypisaniu kosztu do sąsiada przypisujemy jego odległość do celu:<br>`neighbor.h = getDistance(neighbor, goalField);

- sumę jego kosztu oraz heurystki: `neighbor.f = neighbor.g + neighbor.h;` gdzie `neighbor.g` to koszt dotarcia do danego pola, a `neighbor.h` to szacowana odległość od danego pola do celu.
- oraz jego poprzednika: `neighbor.previous = current;`

### Definicja funkcji następnika

Następnik wybierany jest z listy sąsiadów poprzednio wybranych pól. Jest to najbardziej obiecujące pole `current`,
tzn. pole o najmniejszej sumie kosztu przejścia do niego z punktu startowego oraz heurystki.

```javascript
let winner = 0;
    for(let i = 0; i < openSet.length; i++){
        if (openSet[i].f < openSet[winner].f){
            winner = i
        }
    }
let current = openSet[winner];
```

### Definicja przyjętej heurystyki
Jest to szacowana odległość od sprawdzanego pola do celu. Obliczana jest jako `Manhattan Distance`, ponieważ w naszym modelu Agent nie może poruszać się po skosie.

distance = `|x1 - x2| + |y1 - y2|`

### Przykładowe działanie implementacji algorytmu A*

https://youtu.be/b5RHlOqqs4Y 