import { getFromFlask } from "@/utils/apiService";

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
      const res = await getFromFlask(path, ...params);
      if (res.success) {
        this.data = res.data;
      } else {
        console.error("Error fetching piece positions");
      }
    },
    async fetchPiecePositions(move) {
      try {
        const response =
          move === "start"
            ? await this.getResponse("/get-start-positions")
            : await this.getResponse(`/get-piece-positions?move=${move}`);
        this.position = await response.json();
      } catch (error) {
        console.error("Error fetching piece positions:", error);
      }
    },
    async fetchPossibleMoves(square) {
      try {
        const response = await fetch(`/get-possible-moves?square=${square}`);
        this.possibleMoves = await response.json();
      } catch (error) {
        console.error("Error fetching possible moves:", error);
      }
    },
  },
};
