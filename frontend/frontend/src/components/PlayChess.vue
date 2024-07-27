<template>
  <div>
    <h1>Welcome to Chess</h1>
    <ChessBoard />
  </div>
</template>

<script>
import ChessBoard from "./ChessBoard.vue";

export default {
  name: "{PlayChess}",
  components: {
    ChessBoard,
  },
};
</script>
