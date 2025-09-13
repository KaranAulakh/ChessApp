import { apiServiceGET } from "@/utils/apiService";

export const gameLogic = {
  data() {
    return {
      position: {},
      selectedSquare: null,
      possibleMoves: [],
      whiteToMove: true,
    };
  },
  methods: {
    async getResponse(path, ...params) {
      const res = await apiServiceGET(path, ...params);
      if (!res?.success) {
        console.error(res.errorMsg);
      }
      return res;
    },
    async fetchPiecePositions(move) {
      const response =
        move === "start"
          ? await this.getResponse("/get-start-positions")
          : await this.getResponse(`/get-piece-positions?move=${move}`);
      if (response?.success) {
        this.position = response.data;
      }
    },
    async fetchPossibleMoves(square) {
      const response = await this.getResponse(`/get-possible-moves?square=${square}`);
      if (response?.success) {
        this.possibleMoves = response.data;
      } else {
        this.possibleMoves = [];
      }
    },
    async makeMove(startSquare, endSquare) {
      const response = await fetch(`${this.$apiBaseUrl || 'http://localhost:5001'}/make-move`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          start: startSquare,
          end: endSquare
        })
      });
      
      if (response.ok) {
        const result = await response.json();
        this.position = result.piecePositions;
        this.whiteToMove = !this.whiteToMove;
        return result;
      } else {
        console.error('Failed to make move');
        return null;
      }
    },
  },
};
