export default class Field{
    constructor(x, y, isShelf, isOccupiedByAgent, costOfTravel){
        this.xField = x;
        this.yField = y;
        this.isShelf = isShelf;
        this.isOccupiedByAgent = isOccupiedByAgent;
        this.costOfTravel = costOfTravel;
    }

    getParams(){
        let params = {};

        xField = this.xField;
        yField = this.yField;
        isShelf = this.isShelf;
        isOccupiedByAgent = this.isOccupiedByAgent;
        costOfTravel = this.costOfTravel;
        params = {xField, yField, isShelf, isOccupiedByAgent, costOfTravel}

        return params;
    }
}