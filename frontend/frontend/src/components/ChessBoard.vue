<template>
  <div ref="chessboard" class="chessboard"></div>
</template>

<script>
import { gameLogic } from "@/utils/gameLogic.js";

const BLACK_SQUARE_COLOR = "#948979";
const WHITE_SQUARE_COLOR = "#DFD0B8";
const POSSIBLE_MOVES_HIGHLIGHT_COLOR = "rgba(21, 52, 72, 0.15)";
const WHITE_SQUARE_HIGHLIGHT_COLOR = "#E6E6FA";
const BLACK_SQUARE_HIGHLIGHT_COLOR = "#A7D4CD";

export default {
  name: "ChessBoard",
  mixins: [gameLogic],
  data() {
    return {
      images: {},
    };
  },
  async mounted() {
    await this.loadImages();
    await this.fetchPiecePositions("start");
    this.createChessboard();

    window.addEventListener("resize", this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    /*
     * EVENT HANDLING METHODS
     */
    async handleClick(event) {
      const squareElement = event.target;
      const x = squareElement.dataset.x;
      const y = squareElement.dataset.y;
      const square = this.position[x + y];

      // If the clicked square has a piece that belongs to the team who's turn it is, then show options
      if (!!square && square.includes(this.whiteToMove ? "White" : "Black")) {
        await this.fetchPossibleMoves(x + y);
        this.selectedSquare = x + y;
      } else {
        this.possibleMoves = [];
        this.selectedSquare = null;
      }

      this.updateChessboard();
    },

    handleResize() {
      // Re-render the chessboard in case of resize
      this.updateChessboard();
    },

    /*
     * GRAPHIC RENDERING METHODS
     */
    // This Method Creates an 8 by 8 grid using divs for each and a preset pixel size for now
    createChessboard() {
      const chessboard = this.$refs.chessboard;
      chessboard.innerHTML = "";
      chessboard.style.display = "grid";
      chessboard.style.gridTemplateColumns = "repeat(8, 64px)";
      chessboard.style.gridTemplateRows = "repeat(8, 64px)";

      let light = true;
      for (let y = 0; y < 8; y++) {
        for (let x = 0; x < 8; x++) {
          const square = document.createElement("div");
          square.dataset.x = x;
          square.dataset.y = y;
          square.classList.add("chess-square");
          square.style.backgroundColor = light
            ? WHITE_SQUARE_COLOR
            : BLACK_SQUARE_COLOR;
          square.style.width = "64px";
          square.style.height = "64px";
          square.addEventListener("click", this.handleClick);
          chessboard.appendChild(square);
          light = !light;
        }
        light = !light;
      }
      this.updateChessboard();
    },

    updateChessboard() {
      const chessboard = this.$refs.chessboard;
      for (let y = 0; y < 8; y++) {
        for (let x = 0; x < 8; x++) {
          // The dom returns a 1 dimensional grid, so we need to multiply by 8 to get to the right row
          const square = chessboard.children[y * 8 + x];
          const piece = this.position[x.toString() + y.toString()];

          square.innerHTML = ""; // Clear previous pieces
          if (piece) {
            const pieceImg = document.createElement("img");
            pieceImg.src = this.images[piece].src;
            pieceImg.style.width = "100%";
            pieceImg.style.height = "100%";
            square.appendChild(pieceImg);
          }

          // Apply highlights
          if (this.selectedSquare === x.toString() + y.toString()) {
            square.style.backgroundColor =
              x % 2 === y % 2
                ? WHITE_SQUARE_HIGHLIGHT_COLOR
                : BLACK_SQUARE_HIGHLIGHT_COLOR;
          } else if (
            this.possibleMoves &&
            this.possibleMoves.includes(x.toString() + y.toString())
          ) {
            square.style.backgroundColor = POSSIBLE_MOVES_HIGHLIGHT_COLOR;
          } else {
            square.style.backgroundColor =
              x % 2 === y % 2 ? WHITE_SQUARE_COLOR : BLACK_SQUARE_COLOR;
          }
        }
      }
    },

    /*
     * LOAD METHODS
     */
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
}
</style>
