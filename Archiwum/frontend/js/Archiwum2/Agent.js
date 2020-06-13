export default class Agent{
    constructor(positionX, positionY, turn){
        this.positionX = positionX;
        this.positionY = positionY;
        this.turn = turn;
    }

    getParams(){
        let params = {};

        positionX = this.positionX;
        positionY = this.positionY;
        turn = this.turn;

        params = {positionX, positionY, turn};

        return params;
    }

    goForward(){
        if(this.turn == 'Up'){
            this.positionY += 1;
        }
        else if(this.turn == 'Down'){
            this.positionY -= 1;
        }
        else if(this.turn == 'Left'){
            this.positionX -= 1;
        }
        else if(this.turn == 'Right'){
            this.positionX += 1;
        }
    }

    turnLeft(){
        if(this.turn == 'Up'){
            this.turn = 'Left';
        }
        else if(this.turn == 'Down'){
            this.turn = 'Right';
        }
        else if(this.turn == 'Left'){
            this.turn = 'Down';
        }
        else if(this.turn == 'Right'){
            this.turn = 'Up'
        }
    }

    turnRight(){
        if(this.turn == 'Up'){
            this.turn = 'Right';
        }
        else if(this.turn == 'Down'){
            this.turn = 'Left';
        }
        else if(this.turn == 'Left'){
            this.turn = 'Up';
        }
        else if(this.turn == 'Right'){
            this.turn = 'Down'
        }
    }

    showAgent(){
        console.log(this.turn)
        if(this.turn === "Up"){
            document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Up.png')";
        }
        else if(this.turn === "Down"){
            document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Down.png')";
        }
        else if(this.turn === "Right"){
            document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Right.png')";
        }
        else if(this.turn === "Left"){
            document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "url('img/Left.png')";
        }
        
    }

    hideAgent(){
        document.getElementById(this.positionX + "-" + this.positionY).style.backgroundImage = "";
    }


}