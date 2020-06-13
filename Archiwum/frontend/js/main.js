// //Klasy
// class Agent{
//     constructor(positionX, positionY, turn){
//         this.positionX = positionX;
//         this.positionY = positionY;
//         this.turn = turn;
//     }
//
//     getParams(){
//         let params = {};
//
//         positionX = this.positionX;
//         positionY = this.positionY;
//         turn = this.turn;
//
//         params = {positionX, positionY, turn};
//
//         return params;
//     }
//
//     turnLeft(){
//         if(this.turn == 'Up'){
//             this.turn = 'Left';
//         }
//         else if(this.turn == 'Down'){
//             this.turn = 'Right';
//         }
//         else if(this.turn == 'Left'){
//             this.turn = 'Down';
//         }
//         else if(this.turn == 'Right'){
//             this.turn = 'Up'
//         }
//     }
//
//     turnRight(){
//         if(this.turn == 'Up'){
//             this.turn = 'Right';
//         }
//         else if(this.turn == 'Down'){
//             this.turn = 'Left';
//         }
//         else if(this.turn == 'Left'){
//             this.turn = 'Up';
//         }
//         else if(this.turn == 'Right'){
//             this.turn = 'Down'
//         }
//     }
//
//     showAgent(){
//         if(this.turn === "Up"){
//             document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Up.png')";
//         }
//         else if(this.turn === "Down"){
//             document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Down.png')";
//         }
//         else if(this.turn === "Right"){
//             document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Right.png')";
//         }
//         else if(this.turn === "Left"){
//             document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Left.png')";
//         }
//
//     }
//
//     hideAgent(){
//         document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "";
//     }
//
//     goForward(){
//         this.hideAgent()
//         if(this.turn == 'Up'){
//             this.positionY += 1;
//         }
//         else if(this.turn == 'Down'){
//             this.positionY -= 1;
//         }
//         else if(this.turn == 'Left'){
//             this.positionX -= 1;
//         }
//         else if(this.turn == 'Right'){
//             this.positionX += 1;
//         }
//         this.showAgent()
//     }
//
//     goToField(field){
//         if(field.yField > this.positionY){
//             //pole jest nad agentem
//
//         }
//         if(field.yField < this.positionY){
//             //pole jest pod agentem
//
//         }
//         if(field.xField > this.positionX){
//             //pole jest na prawo
//
//         }
//         if(field.xField < this.positionX){
//             //pole jest na lewo
//
//         }
//     }
//
//
// }
//
// class Field{
//     constructor(x, y, isShelf, isOccupiedByAgent, costOfTravel){
//         this.xField = x;
//         this.yField = y;
//         this.isShelf = isShelf;
//         this.isOccupiedByAgent = isOccupiedByAgent;
//         this.costOfTravel = costOfTravel;
//         this.neighbors = [];
//         this.g = 0;
//         this.h = 0;
//         this.f = 0;
//         this.previous = undefined;
//     }
//
//     getParams(){
//         let params = {};
//
//         xField = this.xField;
//         yField = this.yField;
//         isShelf = this.isShelf;
//         isOccupiedByAgent = this.isOccupiedByAgent;
//         costOfTravel = this.costOfTravel;
//         params = {xField, yField, isShelf, isOccupiedByAgent, costOfTravel}
//
//         return params;
//     }
//
// 	setIsShelf(isShelf){
// 		this.isShelf = isShelf;
// 	}
//
// 	getIsShelf(){
// 		return this.isShelf;
// 	}
//
// 	setIsOccupiedByAgent(isOccupiedByAgent){
// 		this.isOccupiedByAgent = isOccupiedByAgent;
// 	}
//
// 	setCostOfTravel(costOfTravel){
// 		this.costOfTravel = costOfTravel;
//     }
//
//     setNeighbors(field){
//         if(field.isShelf == false){
//             this.neighbors.push(field)
//         }
//     }
// }
//
// class Shelf{
// 	constructor(accessY, accessX, havePlace, box1, box2, box3){
//         this.accessX = accessX;
//         this.accessY = accessY;
// 		this.havePlace = true;
// 		this.box1 = box1;
// 		this.box2 = box2;
// 		this.box3 = box3;
//     }
//
// 	getParams(){
//         let params = {};
//
//         xField = this.xField;
//         yField = this.yField;
// 		havePlace = this.havePlace;
// 		box1 = this.box1;
// 		box2 = this.box2;
// 		box3 = this.box3;
//         params = {xField, yField, havePlace, box1, box2, box3}
//
//         return params;
//     }
//
// 	setbox1(box1){
// 		this.box1 = box1;
// 	}
//
// 	setbox2(box1){
// 		this.box2 = box2;
// 	}
//
// 	setbox3(box1){
// 		this.box3 = box3;
// 	}
//
// 	setHavePlace(havePlace){
// 		this.havePlace = havePlace;
// 	}
// }
//
// class Candy{
// 	constructor(type, taste, mark, id){
//         this.type = type;
// 		this.taste = taste;
//         this.mark = mark;
// 		this.id = id;
//     }
//
// 	getId(){
// 		return this.id;
// 	}
//
// }
//
// //funkcje
//
// function createBoard(rangeX, rangeY){
//     const board = [];
//
//     for(let y = 0; y < rangeY; y++){
//         const row = [];
//         for(let x = 0; x < rangeX; x++){
//             let field = new Field(x, y, false, false, 1);
//             row.push(field)
//         }
//         board.push(row)
//     }
//     return board
// }
//
// function createShelfOnBoard(board){
// 	//pierwszy poziom
// 	board[2][2].setIsShelf(true);
// 	board[3][2].setIsShelf(true);
//
// 	board[2][4].setIsShelf(true);
// 	board[3][4].setIsShelf(true);
//
// 	board[2][6].setIsShelf(true);
// 	board[3][6].setIsShelf(true);
//
// 	board[2][8].setIsShelf(true);
// 	board[3][8].setIsShelf(true);
//
// 	//drugi poziom
// 	board[5][2].setIsShelf(true);
// 	board[5][3].setIsShelf(true);
//
// 	board[5][7].setIsShelf(true);
// 	board[5][8].setIsShelf(true);
//
// 	//trzeci poziom
// 	board[7][2].setIsShelf(true);
// 	board[8][2].setIsShelf(true);
//
// 	board[7][4].setIsShelf(true);
// 	board[8][4].setIsShelf(true);
//
// 	board[7][6].setIsShelf(true);
// 	board[8][6].setIsShelf(true);
//
// 	board[7][8].setIsShelf(true);
// 	board[8][8].setIsShelf(true);
// 	return board
// }
//
// function createCostofField(board, rangeX, rangeY){
// 	let cost;
// 	let number;
// 	for(let y = 0; y < rangeY; y++){
// 		for(let x = 0; x < rangeX; x++){
// 			number = 0;
// 			if(y<9 && board[y+1][x].getIsShelf()){
// 				number = number + 1;
// 			}
// 			if(y>0 && board[y-1][x].getIsShelf()){
// 				number = number + 1;
// 			}
// 			if(x<9 && board[y][x+1].getIsShelf()){
// 				number = number + 1;
// 			}
// 			if(x>0 && board[y][x-1].getIsShelf()){
// 				number = number + 1;
// 			}
// 			cost = number*2;
// 			if(cost==0){
// 				cost = 1;
// 			}
// 			board[y][x].setCostOfTravel(cost);
// 		}
// 	}
// 	return board;
// }
//
// function createShelf(){
// 	const listOfShelf = [];
//
// 	//pierwszy poziom
// 	let shelf = new Shelf(2, 1, true, 211, 212, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(3, 1, true, 311, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	shelf = new Shelf(4, 4, false, 441, 442, 443);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(1, 4, true, 0, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	shelf = new Shelf(4, 6, true, 461, 462, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(1, 6, true, 161, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	shelf = new Shelf(3, 9, true, 391, 0, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(2, 9, true, 291, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	//drugi poziom
// 	shelf = new Shelf(5, 1, true, 511, 0, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(5, 4, true, 541, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	shelf = new Shelf(5, 6, true, 561, 0, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(5, 9, true, 591, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	//trzeci poziom
// 	shelf = new Shelf(7, 1, true, 711, 0, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(8, 1, true, 811, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	shelf = new Shelf(6, 4, true, 641, 0, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(9, 4, true, 941, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	shelf = new Shelf(6, 6, true, 661, 0, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(9, 6, true, 961, 0, 0);
// 	listOfShelf.push(shelf)
//
// 	shelf = new Shelf(7, 9, true, 791, 0, 0);
// 	listOfShelf.push(shelf)
// 	shelf = new Shelf(8, 9, true, 891, 0, 0);
// 	listOfShelf.push(shelf)
//
//
// 	return listOfShelf;
// }
//
// function showBoard(board){
//     for(let y = board.length - 1; y >= 0 ; y--){
//         document.getElementById("board").innerHTML += "<div class='row' id='row-" + y + "'> </div>";
//
//         for(let x = 0; x < board[y].length; x++){
// 			if(board[y][x].getIsShelf())
// 				document.getElementById("row-" + y).innerHTML += "<div class='regal2' id=" + x + "-" + y + "> </div>"
// 			else
// 				document.getElementById("row-" + y).innerHTML += "<div class='field' id=" + x + "-" + y + ">"+ board[y][x].costOfTravel + "</div>"
//         }
//     }
// }
//
// function getDistance(field, goalField){
//     // var a = field.xField - goalField.xField;
//     // var b = field.yField - goalField.yField;
//     // var c = Math.sqrt(a*a + b*b);
//     var d = Math.abs(field.xField - goalField.xField) + Math.abs(field.yField - goalField.yField)
//     return d
// }
//
// function addNeighbors(board){
//     for(var y = 0; y < 10; y++){
//         for(var x = 0; x < 10; x++){
//             var leftNeigbor, rightNeighbor, topNeighbor, bottomNeighbor;
//             if(x > 0){
//                 leftNeigbor = board[y][x - 1];
//                 board[y][x].setNeighbors(leftNeigbor);
//             }
//             if(x < board[y].length - 1){
//                 rightNeighbor = board[y][x + 1];
//                 board[y][x].setNeighbors(rightNeighbor);
//             }
//             if(y > 0){
//                 bottomNeighbor = board[y - 1][x];
//                 board[y][x].setNeighbors(bottomNeighbor);
//             }
//             if(y < board.length - 1){
//                 topNeighbor = board[y + 1][x];
//                 board[y][x].setNeighbors(topNeighbor);
//             }
//         }
//     }
// }
//
// // function colorGreen(field){
// //     document.getElementById(field.xField + "-" + field.yField).style.backgroundColor = "green";
// // }
//
// // function colorRed(field){
// //     document.getElementById(field.xField + "-" + field.yField).style.backgroundColor = "red";
// // }
//
// // function colorYellow(field){
// //     document.getElementById(field.xField + "-" + field.yField).style.backgroundColor = "yellow";
// // }
//
// const colorFactory = color => (field, animationFrame) => {
//     const delay = animationFrame * 50
//     console.log(delay)
//     setTimeout(() => {
//         document.getElementById(field.xField + "-" + field.yField).style.backgroundColor = color;
//     }, delay);
//     return ++animationFrame
// }
//
// const colorYellow = colorFactory('yellow')
// const colorGreen = colorFactory('green')
// const colorRed = colorFactory('red')
//
// // function addNeighborsToOpenSet(set, neigbors){
// //     for(x = 0; x < neigbors.length; x++){
// //         set.push(neigbors[x]);
// //         colorGreen(neigbors[x]);
// //     }
// // }
//
// function addToClosedSet(set, field){
//     set.push(field);
//     colorRed(field);
// }
//
//
// function addToOpenSet(set, field){
//     set.push(field);
//     colorGreen(field);
// }
//
// function calculateFScore(field, goalField){
//     let fscore, distanceToGoal, costOfTravel;
//     distanceToGoal = getDistance(field, goalField);
//     costOfTravel = field.costOfTravel;
//     fscore = costOfTravel + distanceToGoal;
//     return fscore;
// }
//
// function findLowestFScore(openSet, goalField){
//     let bestField = openSet[0];
//     for(var x = 1; x < openSet.length; x++){
//         if(calculateFScore(openSet[x], goalField) < calculateFScore(bestField, goalField)){
//             bestField = openSet[x];
//         }
//     }
//     return bestField;
// }
//
// function removeFromSet(openSet, promisingField){
//     for(var x = openSet.length - 1; x >= 0; x--){
//         if(openSet[x] == promisingField){
//             openSet.splice(x,1);
//         }
//     }
// }
//
// function aStar(startField, goalField){
//     let closedSet = [];
//     let openSet = [];
//     var path;
//     let animationFrame = 0
//
//     // addToOpenSet(openSet, startField)
//     openSet.push(startField);
//     colorGreen(startField, animationFrame);
//
//     while(openSet.length > 0){
//
//         // let current = findLowestFScore(openSet, goalField);
//         let winner = 0;
//         for(let i = 0; i < openSet.length; i++){
//             if (openSet[i].f < openSet[winner].f){
//                 winner = i
//             }
//         }
//
//         let current = openSet[winner];
//
//         if(current === goalField){
//             path = []
//             var temp = current;
//             path.push(temp);
//             while(temp.previous){
//                 path.push(temp.previous);
//                 temp = temp.previous
//             }
//             console.log("A* COMPLETED");
//
//             for(var i = 0; i < path.length; i++){
//                 animationFrame = colorYellow(path[i], animationFrame);
//             }
//             return path;
//         }
//
//         removeFromSet(openSet, current);
//         // addToClosedSet(closedSet, current);
//         closedSet.push(current);
//         animationFrame = colorRed(current, animationFrame);
//
//         var neighbors = current.neighbors;
//
//         for(var i = 0; i < neighbors.length; i++){
//             var neighbor = neighbors[i];
//
//             if(!closedSet.includes(neighbor)){
//                 var tempG = current.g + neighbor.costOfTravel;
//
//                 if(openSet.includes(neighbor)){
//                     if(tempG < neighbor.g){
//                         neighbor.g = tempG;
//                     }
//                 } else {
//                     neighbor.g = tempG;
//                     // addToOpenSet(openSet, neighbor);
//                     openSet.push(neighbor);
//                     animationFrame = colorGreen(neighbor,animationFrame);
//                 }
//                 neighbor.h = getDistance(neighbor, goalField);
//                 neighbor.f = neighbor.g + neighbor.h;
//
//                 neighbor.previous = current;
//             }
//         }
//     }
// }
//
// function executePath(agent, path){
//
// }
//
//
// let board = createBoard(10,10);
// board = createShelfOnBoard(board);
// board = createCostofField(board, 10, 10);
// let candy = new Candy('zelek', 'truskawkowy', 'Jumbo', 541);
// let shelfs = createShelf();
// let agent = new Agent(0,0, 'Right');
//
// addNeighbors(board);
//
// function delayedFunction(func, index, time) {
//     setTimeout(() => func(), time * index);
// }
//
// function start(){
//     showBoard(board);
//
//     // for (let i = 0; i<9; i++) {
//     //     delayedStep(agent, i);
//     // }
//     const path = aStar(board[0][0], board[9][9]);
//     // agent.showAgent();
//     console.log(path.reverse())
// }
//
//
//
