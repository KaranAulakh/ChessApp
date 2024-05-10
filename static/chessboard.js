Vue.component('chess-board', {
    template: `<canvas ref='canvas' width='512' height='512'></canvas>`,

    data() {
        return {
            images: {},
            position: {},
            highlightedSquares: [],
            whiteToMove: true,
        };
    },
    async mounted() {
        await this.loadImages();
        await this.fetchPiecePositions("start");
        this.$refs.canvas.addEventListener('click', this.handleClick);
        window.addEventListener('resize', this.handleResize); // Listen for window resize events
        this.handleResize(); // Call handleResize initially to ensure proper scaling
    },
    beforeDestroy() {
        this.$refs.canvas.removeEventListener('click', this.handleClick);
        window.removeEventListener('resize', this.handleResize); // Remove event listener on component destroy
    },
    methods: {
        async loadImages() {
            const imageSources = {
                "LightPawn": '/static/images/LightPawn.png',
                "LightKnight": '/static/images/LightKnight.png',
                "LightBishop": '/static/images/LightBishop.png',
                "LightRook": '/static/images/LightRook.png',
                "LightQueen": '/static/images/LightQueen.png',
                "LightKing": '/static/images/LightKing.png',
                "DarkPawn": '/static/images/DarkPawn.png',
                "DarkKnight": '/static/images/DarkKnight.png',
                "DarkBishop": '/static/images/DarkBishop.png',
                "DarkRook": '/static/images/DarkRook.png',
                "DarkQueen": '/static/images/DarkQueen.png',
                "DarkKing": '/static/images/DarkKing.png',
            };

            await Promise.all(Object.keys(imageSources).map(async (key) => {
                const img = new Image();
                img.src = imageSources[key];
                await img.decode(); // Wait for image to be fully loaded
                this.images[key] = img;
            }));
        },
        async fetchPiecePositions(move) {
            try {
                const response = await fetch(`/get-piece-positions?move=${move}`);
                this.position = await response.json();
                // Once positions are fetched, draw the chessboard
                this.drawChessboard();
            } catch (error) {
                console.error('Error fetching piece positions:', error);
            }
        },
        async drawChessboard() {
            const canvas = this.$refs.canvas;
            const context = canvas.getContext('2d');
            const LIGHT_COLOR = "#DFD0B8";
            const DARK_COLOR = "#948979";

            // draw chess board
            let light = true;
            for (let x = 0; x < 8; x++) {
                for (let y = 0; y < 8; y++) {
                    const color = light ? LIGHT_COLOR : DARK_COLOR;
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
            for (const key in this.position) {
                context.drawImage(this.images[this.position[key].imageName], key[0] * 64, key[1] * 64, 64, 64);
            }
        },
        highlightSquares(context) {
            const HIGHLIGHT_COLOR = "rgba(21, 52, 72, 0.15)";
            const cornerRadius = 18;
            const offset = 8;
            
            this.highlightedSquares.forEach(square => {
                const x = parseInt(square.charAt(0)) * 64 + offset / 2; 
                const y = parseInt(square.charAt(1)) * 64 + offset / 2;
            
                context.fillStyle = HIGHLIGHT_COLOR;
                context.beginPath();
                context.moveTo(x + cornerRadius, y);
                context.arcTo(x + 64 - offset, y, x + 64 - offset, y + cornerRadius, cornerRadius);
                context.arcTo(x + 64 - offset, y + 64 - offset, x + 64 - cornerRadius, y + 64 - offset, cornerRadius);
                context.arcTo(x, y + 64 - offset, x, y + 64 - cornerRadius, cornerRadius);
                context.arcTo(x, y, x + cornerRadius, y, cornerRadius);
                context.closePath();
                context.fill();
            });

            /* highlight squares with circle

            this.highlightedSquares.forEach(square => {
                // find center of circle
                const x = (parseInt(square.charAt(0)) + 0.5) * 64;
                const y = (parseInt(square.charAt(1)) + 0.5) * 64;
                const radius = 30; 
                context.fillStyle = HIGHLIGHT_COLOR;
                context.beginPath();
                // start angle = 0 and end angle is 2PI radians (or 360 degrees)
                context.arc(x, y, radius, 0, 2 * Math.PI);
                context.fill();
            });
            */
        },
        handleClick(event) {
            const canvas = this.$refs.canvas;
            const rect = canvas.getBoundingClientRect();
            const x = Math.floor((event.clientX - rect.left) / 64);
            const y = Math.floor((event.clientY - rect.top) / 64);
            /* How in the world do I format this to not look like shit? */
            if 
            (this.whiteToMove && 
             this.position[x.toString() + y.toString()] !== undefined && 
             this.position[x.toString() + y.toString()].isWhite)
                this.highlightedSquares = [x.toString() + y.toString()]

            else if 
            (!this.whiteToMove && 
             this.position[x.toString() + y.toString()] !== undefined && 
             !this.position[x.toString() + y.toString()].isWhite)
                this.highlightedSquares = [x.toString() + y.toString()]
                
            else
                this.highlightedSquares = [];
            this.drawChessboard()
            
        },
        handleResize() {
            // Redraw the chessboard, will probably need to seen in new dimensions
            this.drawChessboard();
        },
    }
});

new Vue({
    el: '#app'
});
