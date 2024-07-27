<template>
  <div class="app-container">
    <h1>Welcome to Chess</h1>
    <ChessBoard />
  </div>
</template>

<script>
import ChessBoard from "./ChessBoard.vue";

export default {
  name: "PlayChess",
  components: {
    ChessBoard,
  },
};
</script>

<style scoped>
body,
html {
  background-color: #153448;
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.app-container {
  text-align: center;
  color: white;
}
</style>
