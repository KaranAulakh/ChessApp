// Define a Pawn class that inherits from Piece
class Pawn extends Piece {
    constructor(color) {
        super(color);
        super(x);
        super(y);
    }

    move() {
        console.log("Pawn moved");
    }
}