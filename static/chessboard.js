const DARK_SQUARE_COLOR = "#948979"
const LIGHT_SQUARE_COLOR = "#DFD0B8"
const POSSIBLE_MOVES_HIGHLIGHT_COLOR = "rgba(21, 52, 72, 0.15)"
const LIGHT_SQUARE_HIGHLIGHT_COLOR = "#E6E6FA"
const DARK_SQUARE_HIGHLIGHT_COLOR = "#A7D4CD"


Vue.component('chess-board', {
    template: `<canvas ref='canvas' width='512' height='512'></canvas>`,

    data() {
        return {
            images: {},
            sounds: {},
            piecePositions: {},
            selectedSquare: null,
            possibleMoves: [],
            whiteToMove: true,
            pawnCanPromote: null,
            gameState: null
        };
    },
    async mounted() {
        await this.loadImages();
        await this.loadSounds();
        await this.fetchStartPosition();

        // handle events for click and window resize
        this.$refs.canvas.addEventListener('click', this.handleClick);
        window.addEventListener('resize', this.handleResize);
        this.drawChessboard();
    },
    beforeDestroy() {
        this.$refs.canvas.removeEventListener('click', this.handleClick);
        window.removeEventListener('resize', this.handleResize);
    },
    methods: {
        /*
         * EVENT HANDLING METHODS
         */
        async handleClick(event) {
            const canvas = this.$refs.canvas;
            const rect = canvas.getBoundingClientRect();
            const clickPosition = Math.floor((event.clientX - rect.left) / 64).toString() + 
                                  Math.floor((event.clientY - rect.top) / 64).toString()

            this.pawnCanPromote = null;
            // Move piece
            if(!!this.selectedSquare && this.possibleMoves.includes(clickPosition)) {
                await this.movePiece(this.selectedSquare, clickPosition);
                this.whiteToMove = !this.whiteToMove;
                this.possibleMoves = [];
                this.selectedSquare = null;
                console.log(this.gameState)
                this.gameState === null ? this.sounds["move"].play() : this.sounds["check"].play()
            }
            // Select Piece
            else if (!!this.piecePositions[clickPosition] && this.piecePositions[clickPosition].includes(this.whiteToMove ? "White" : "Black")) {
                await this.fetchPossibleMoves(clickPosition);
                this.selectedSquare = clickPosition;
            } 
            // Invalid Selection
            else {
                this.possibleMoves = [];
                this.selectedSquare = null;   
            }

            if (this.pawnCanPromote != null) {
                promotePawnTo = prompt("Type in Queen, Knight, Bishop, or Rook");
                await this.promotePawn(this.pawnCanPromote, promotePawnTo);
            }
            this.drawChessboard()
        },
        handleResize() {
            // Redraw the chessboard, will probably need to send in new dimensions
            this.drawChessboard();
        },
        /*
         * GRAPHIC RENDERING METHODS
         */
        async drawChessboard() {
            const canvas = this.$refs.canvas;
            const context = canvas.getContext('2d');

            // draw chess board
            let light = true;
            for (let x = 0; x < 8; x++) {
                for (let y = 0; y < 8; y++) {
                    const color = light ? LIGHT_SQUARE_COLOR : DARK_SQUARE_COLOR;
                    context.fillStyle = color;
                    context.fillRect(x * 64, y * 64, 64, 64);
                    light = !light;
                }
                light = !light;
            }

            this.highlightSquares(context)
            this.drawPieces(context)   
        },
        
        drawPieces(context) {
            for (const key in this.piecePositions) {
                context.drawImage(this.images[this.piecePositions[key]], key[0] * 64, key[1] * 64, 64, 64);
            }
        },

        highlightSquares(context) {
            // highlight selected square
            if (!this.selectedSquare) 
                return;
            const color = this.selectedSquare[0] % 2 == this.selectedSquare[1] % 2 ? LIGHT_SQUARE_HIGHLIGHT_COLOR : DARK_SQUARE_HIGHLIGHT_COLOR
            this.drawCircle(context, 0, 0, this.selectedSquare, color)

            // highlight possible moves
            if (!this.possibleMoves) 
                return;
            this.possibleMoves.forEach(square => {
                this.drawCircle(context, 12, 18, square, POSSIBLE_MOVES_HIGHLIGHT_COLOR)
            });
            
        },

        drawCircle(context, offset, cornerRadius, square, color){
            const x = parseInt(square[0]) * 64 + offset / 2; 
            const y = parseInt(square[1]) * 64 + offset / 2;

            context.fillStyle = color
            context.beginPath();
            context.moveTo(x + cornerRadius, y);
            context.arcTo(x + 64 - offset, y, x + 64 - offset, y + cornerRadius, cornerRadius);
            context.arcTo(x + 64 - offset, y + 64 - offset, x + 64 - cornerRadius, y + 64 - offset, cornerRadius);
            context.arcTo(x, y + 64 - offset, x, y + 64 - cornerRadius, cornerRadius);
            context.arcTo(x, y, x + cornerRadius, y, cornerRadius);
            context.closePath();
            context.fill();
        },


        /*
         * API METHODS
         */
        async fetchStartPosition() {
            try {
                const response = await fetch(`/get-start-position`);
                this.piecePositions = await response.json();
            } catch (error) {
                console.error('Error fetching piece positions:', error);
            }
        },
        async fetchPossibleMoves(square) {
            try {
                const response = await fetch(`/get-possible-moves?square=${square}`);
                this.possibleMoves = await response.json();
            } catch (error) {
                console.error('Error fetching piece positions:', error);
            }
        },
        async movePiece(pieceToMovePosition, destinationPosition) {
            try {
                const response = await fetch(`/move?start=${pieceToMovePosition}&destination=${destinationPosition}`);
                const data = await response.json();
                this.piecePositions = data.piecePositions;
                this.pawnCanPromote = data.pawnCanPromote;
                this.gameState = data.gameState;
            } catch (error) {
                console.error('Error fetching piece positions:', error);
            }
        },
        async promotePawn(pawnLocation, promoteTo) {
            try {
                const response = await fetch(`/promote-pawn?pawnLocation=${pawnLocation}&promoteTo=${promoteTo}`);
                this.piecePositions = await response.json();
            } catch (error) {
                console.error('Error fetching piece positions:', error);
            }
        },


        /*
         * UTILITY METHODS
         */
        async loadImages() {
            const imageSources = {
                "WhitePawn": '/static/images/WhitePawn.png',
                "WhiteKnight": '/static/images/WhiteKnight.png',
                "WhiteBishop": '/static/images/WhiteBishop.png',
                "WhiteRook": '/static/images/WhiteRook.png',
                "WhiteQueen": '/static/images/WhiteQueen.png',
                "WhiteKing": '/static/images/WhiteKing.png',
                "BlackPawn": '/static/images/BlackPawn.png',
                "BlackKnight": '/static/images/BlackKnight.png',
                "BlackBishop": '/static/images/BlackBishop.png',
                "BlackRook": '/static/images/BlackRook.png',
                "BlackQueen": '/static/images/BlackQueen.png',
                "BlackKing": '/static/images/BlackKing.png',
            };

            await Promise.all(Object.keys(imageSources).map(async (key) => {
                const img = new Image();
                img.src = imageSources[key];
                await img.decode(); // Wait for image to be fully loaded
                this.images[key] = img;
            }));
        },
        async loadSounds() {
            const soundSources = {
                "move": '/static/sounds/moveSound.wav',
                "check": '/static/sounds/checkSound.wav',
            };
        
            await Promise.all(Object.keys(soundSources).map(async (key) => {
                const audio = new Audio();
                audio.src = soundSources[key];
                await new Promise((resolve, reject) => {
                    audio.oncanplaythrough = resolve;
                    audio.onerror = reject;
                });
                this.sounds[key] = audio;
            }));
        }
    }
});

new Vue({
    el: '#app'
});

