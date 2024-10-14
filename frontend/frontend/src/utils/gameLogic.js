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
      const response = await fetch(`/get-possible-moves?square=${square}`);
      this.possibleMoves = await response.json();
    },
  },
};
