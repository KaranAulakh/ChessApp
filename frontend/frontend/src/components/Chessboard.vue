<template>
  <canvas ref="canvas" width="512" height="512"></canvas>
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

    // handle events for click and window resize
    this.$refs.canvas.addEventListener("click", this.handleClick);
    window.addEventListener("resize", this.handleResize);
    this.drawChessboard();
  },
  beforeUnmount() {
    this.$refs.canvas.removeEventListener("click", this.handleClick);
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    /*
     * EVENT HANDLING METHODS
     */
    async handleClick(event) {
      const canvas = this.$refs.canvas;
      const rect = canvas.getBoundingClientRect();
      const x = Math.floor((event.clientX - rect.left) / 64);
      const y = Math.floor((event.clientY - rect.top) / 64);
      const square = this.position[x.toString() + y.toString()];

      // If the clicked square has a piece that belongs to the team who's turn it is, then show options
      if (!!square && square.includes(this.whiteToMove ? "White" : "Black")) {
        await this.fetchPossibleMoves(x.toString() + y.toString());
        this.selectedSquare = x.toString() + y.toString();
      } else {
        this.possibleMoves = [];
        this.selectedSquare = null;
      }

      this.drawChessboard();
    },
    handleResize() {
      // Redraw the chessboard, will probably need to send in new dimensions
      this.drawChessboard();
    },
    /*
     * GRAPHIC RENDERING METHODS
     */
    drawChessboard() {
      const canvas = this.$refs.canvas;
      const context = canvas.getContext("2d");

      // draw chess board
      let light = true;
      for (let x = 0; x < 8; x++) {
        for (let y = 0; y < 8; y++) {
          const color = light ? WHITE_SQUARE_COLOR : BLACK_SQUARE_COLOR;
          context.fillStyle = color;
          context.fillRect(x * 64, y * 64, 64, 64);
          light = !light;
        }
        light = !light;
      }

      this.highlightSquares(context);
      this.drawPieces(context);
    },

    drawPieces(context) {
      for (const key in this.position) {
        context.drawImage(
          this.images[this.position[key]],
          key[0] * 64,
          key[1] * 64,
          64,
          64
        );
      }
    },

    highlightSquares(context) {
      // highlight selected square
      if (!this.selectedSquare) return;
      const color =
        this.selectedSquare[0] % 2 == this.selectedSquare[1] % 2
          ? WHITE_SQUARE_HIGHLIGHT_COLOR
          : BLACK_SQUARE_HIGHLIGHT_COLOR;
      this.drawCircle(context, 0, 0, this.selectedSquare, color);

      // highlight possible moves
      if (!this.possibleMoves) return;
      this.possibleMoves.forEach((square) => {
        this.drawCircle(
          context,
          12,
          18,
          square,
          POSSIBLE_MOVES_HIGHLIGHT_COLOR
        );
      });
    },

    drawCircle(context, offset, cornerRadius, square, color) {
      const x = parseInt(square[0]) * 64 + offset / 2;
      const y = parseInt(square[1]) * 64 + offset / 2;

      context.fillStyle = color;
      context.beginPath();
      context.moveTo(x + cornerRadius, y);
      context.arcTo(
        x + 64 - offset,
        y,
        x + 64 - offset,
        y + cornerRadius,
        cornerRadius
      );
      context.arcTo(
        x + 64 - offset,
        y + 64 - offset,
        x + 64 - cornerRadius,
        y + 64 - offset,
        cornerRadius
      );
      context.arcTo(x, y + 64 - offset, x, y + 64 - cornerRadius, cornerRadius);
      context.arcTo(x, y, x + cornerRadius, y, cornerRadius);
      context.closePath();
      context.fill();
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
