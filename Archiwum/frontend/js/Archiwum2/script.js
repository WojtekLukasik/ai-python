// import Agent from './Agent.js'

// //Klasy


// class Field {
//     constructor(x, y, isEmpty) {
//         this.xField = x;
//         this.yField = y;
//         this.isFieldEmpty = isEmpty;
//     }
//     getCoordinates(){
//         return this.xField + this.yField;
//     }

//     getStatus(){
//         return this.isFieldEmpty;
//     }
// }

// class Product {
//     constructor(name, type, farcing, price) {
//         this.name = name;
//         this.type = type;
//         this.farcing = farcing;
//         this.price = price
//     }
// }

// class Rack{
//     constructor(noOfShelf, typOfProduct) {
//         this.noOfShelf = noOfShelf;
//     }

//     addShelf(){
//         this.noOfShelf = this.noOfShelf + 1;
//     }

//     isEmpty(){
//         if (this.noOfShelf === 0){
//             return true;
//         }else {
//             return false;
//         }
//     }
// }

// class Shelf {
//     constructor(number) {
//         this.number = number;
//     }
// }


// //Objekty i zmienne
// var regaly = ['1-1', '1-3', '1-4', '1-6', '1-7', '1-9', '2-1', '2-9', '3-3', '3-4', '3-6', '3-7', '4-1', '4-9', '5-1', '5-3', '5-4', '5-6', '5-7', '5-9']
// const agent1 = new Agent(3, 0);

// //Funkcja uruchamiająca prace calego scriptu 
// function start(){
//     //ponumerujPola();
//     pokolorujRegaly();
//     umiescAgenta(agent1);
//     droga(agent1);
// }

// //Funkcja kolorujaca miejsca na planszy gdzie znajduja sie regaly
// function pokolorujRegaly(){
//     let x;
//     for(x = 0; x < regaly.length; x++){
//         document.getElementById(regaly[x]).className = 'regal';
//     }
// }

// //Funkcja wyswietlajaca id pol
// function ponumerujPola(){
//     let x,y
//     for(x = 0; x < 7; x++){
//         for(y = 0; y < 11; y++){
//             id = x.toString() + "-" + y.toString();
//             document.getElementById(id).innerHTML = id;
//         }
//     }
// }

// //Funkcja usuwająca agenta z pola, przed przemieszczeniem
// function usunAgenta(agent){
//     document.getElementById(agent.getId()).style.backgroundImage = "none";
// }


// //Funckja wyswietlajaca agenta gdy ten zmieni polozenie
// function umiescAgenta(agent) {
//     document.getElementById(agent.getId()).style.backgroundImage = "url('Agent.jpg')";
// }

//Funkcja zmieniajaca polozenie agenta o 1 pole
function przemieszczenie(side, time, agent){
    const lastPosition = agent.getId();
    setTimeout(function(){
        usunAgenta(agent)
        if(side == "left")
            agent.left();
        if(side == "right")
            agent.right();
        if(side == "up")
            agent.up();
        if(side == "down")
            agent.down();
        umiescAgenta(agent);
    }, time);
}

// //Funkcja ktora ustala droge agenta do przebycia
// function droga(agent) {
//     przemieszczenie("right", 1000, agent);
//     przemieszczenie("right", 2000, agent);
//     przemieszczenie("up", 3000, agent);
//     przemieszczenie("right", 4000, agent);
//     przemieszczenie("right", 5000, agent);
//     przemieszczenie("right", 6000, agent);
//     przemieszczenie("right", 7000, agent);
//     przemieszczenie("right", 8000, agent);
//     przemieszczenie("right", 9000, agent);
// }
