<template>
  <div class="app-container">
    <p>Welcome to Chess</p>
    <ChessBoard />
  </div>
</template>

<script>
import ChessBoard from "./Chessboard.vue";

export default {
  name: "PlayChess",
  components: {
    ChessBoard,
  },
};
</script>
