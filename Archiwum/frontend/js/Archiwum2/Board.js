import Field  from './Field.js'

export function createBoard(rangeX, rangeY){
    const board = [];

    for(let y = 0; y < rangeY; y++){
        const row = [];
        for(let x = 0; x < rangeX; x++){
            let field = new Field(x, y, false, false, 1);
            row.push(field)
        }
        board.push(row)
    }
    return board
}

export function showBoard(board){
    for(let y = board.length - 1; y >= 0 ; y--){
        document.getElementById("board").innerHTML += "<div class='row' id='row-" + y + "'> </div>";

        for(let x = 0; x < board[y].length; x++){
            document.getElementById("row-" + y).innerHTML += "<div class='field' id=" + x + "-" + y + "> </div>"
        }
    }
}





