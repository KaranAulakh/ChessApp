<template>
  <div class="chessboard">
    <div
      v-for="square in boardSquares"
      :key="square.id"
      :class="getSquareClasses(square)"
      @click="handleSquareClick(square)"
    >
      <img
        v-if="square.piece"
        :src="images[square.piece]?.src"
        class="piece-image"
        :alt="square.piece"
      />
    </div>
  </div>
</template>

<script>
import { gameLogic } from "@/utils/gameLogic.js";

export default {
  name: "ChessBoard",
  mixins: [gameLogic],
  data() {
    return {
      images: {},
    };
  },
  computed: {
    // Reactive computed property that automatically updates when position changes
    boardSquares() {
      const squares = [];
      for (let y = 0; y < 8; y++) {
        for (let x = 0; x < 8; x++) {
          const id = `${x}${y}`;
          squares.push({
            id,
            x,
            y,
            piece: this.position[id] || null,
            isLight: (x + y) % 2 === 0,
          });
        }
      }
      return squares;
    },
  },
  async mounted() {
    await this.loadImages();
    await this.fetchPiecePositions("start");
    this.emitGameState();
    window.addEventListener("resize", this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    // Get CSS classes for each square based on its state
    getSquareClasses(square) {
      const classes = ["chess-square"];

      // Add base color class
      if (square.isLight) {
        classes.push("light-square");
      } else {
        classes.push("dark-square");
      }

      // Add selection highlight
      if (this.selectedSquare === square.id) {
        classes.push("selected");
      }

      // Add possible move highlight
      if (this.possibleMoves && this.possibleMoves.includes(square.id)) {
        // Check if there's an enemy piece on this square
        const hasEnemyPiece =
          square.piece &&
          !square.piece.includes(this.whiteToMove ? "White" : "Black");

        classes.push(hasEnemyPiece ? "possible-capture" : "possible-move");
      }

      return classes;
    },

    // Handle square clicks
    async handleSquareClick(square) {
      const clickedSquare = square.id;
      const pieceAtSquare = this.position[clickedSquare];

      // Make a move ff we have a piece selected and click on a valid move
      if (this.selectedSquare && this.possibleMoves.includes(clickedSquare)) {
        const moveResult = await this.makeMove(
          this.selectedSquare,
          clickedSquare
        );
        if (moveResult) {
          this.possibleMoves = [];
          this.selectedSquare = null;
          this.emitGameState();
        }
      }
      // Show possible moves if the clicked square has a piece that belongs to the team whose turn it is
      else if (
        !!pieceAtSquare &&
        pieceAtSquare.includes(this.whiteToMove ? "White" : "Black")
      ) {
        await this.fetchPossibleMoves(clickedSquare);
        this.selectedSquare = clickedSquare;
      }
      // Clear the selection ff this is not a valid spot to click
      else {
        this.possibleMoves = [];
        this.selectedSquare = null;
      }
    },

    async loadImages() {
      const imageSources = {
        WhitePawn: require("@/assets/pieces/wP.svg"),
        WhiteKnight: require("@/assets/pieces/wN.svg"),
        WhiteBishop: require("@/assets/pieces/wB.svg"),
        WhiteRook: require("@/assets/pieces/wR.svg"),
        WhiteQueen: require("@/assets/pieces/wQ.svg"),
        WhiteKing: require("@/assets/pieces/wK.svg"),
        BlackPawn: require("@/assets/pieces/bP.svg"),
        BlackKnight: require("@/assets/pieces/bN.svg"),
        BlackBishop: require("@/assets/pieces/bB.svg"),
        BlackRook: require("@/assets/pieces/bR.svg"),
        BlackQueen: require("@/assets/pieces/bQ.svg"),
        BlackKing: require("@/assets/pieces/bK.svg"),
      };

      await Promise.all(
        Object.keys(imageSources).map(async (key) => {
          const img = new Image();
          img.src = imageSources[key];
          await img.decode();
          this.images[key] = img;
        })
      );
    },

    // Emit game state information to parent component
    emitGameState() {
      this.$emit("game-state-updated", {
        whiteToMove: this.whiteToMove,
        gameState: this.gameState,
        gameEnded: this.gameEnded,
      });
    },
  },
};
</script>

<style scoped>
.chessboard {
  display: grid;
  grid-template-columns: repeat(8, 64px);
  grid-template-rows: repeat(8, 64px);
}

.chess-square {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 64px;
  height: 64px;
  cursor: pointer;
}

/* Base square colors */
.light-square {
  background-color: #dfd0b8;
}

.dark-square {
  background-color: #948979;
}

/* Selection highlight */
.chess-square.selected.light-square {
  background-color: #e6e6fa;
}

.chess-square.selected.dark-square {
  background-color: #a7d4cd;
}

/* Possible move highlight */
.chess-square.possible-move {
  position: relative;
}
.chess-square.possible-move::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 20px;
  background-color: rgba(21, 52, 72, 0.4);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 1;
}

.chess-square.possible-capture::before {
  content: "✕";
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 24px;
  font-weight: bold;
  color: rgba(220, 53, 69, 0.8);
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 1;
}

/* Piece image styling */
.piece-image {
  width: 100%;
  height: 100%;
  pointer-events: none; /* Prevent image from interfering with square clicks */
}
</style>
