<template>
  <div class="chessboard-container">
    <div class="chessboard">
      <div v-for="row in 8" :key="row" class="row">
        <div
          v-for="col in 8"
          :key="col"
          :class="['cell', getColor(row, col)]"
        ></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChessBoard",
  methods: {
    getColor(row, col) {
      return (row + col) % 2 === 0 ? "white" : "black";
    },
  },
};
</script>

<style>
.chessboard-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.chessboard {
  display: grid;
  grid-template-rows: repeat(8, 50px);
  grid-template-columns: repeat(8, 50px);
  border: 2px solid #000;
}

.row {
  display: contents;
}

.cell {
  width: 50px;
  height: 50px;
}

.cell.white {
  background-color: #dfd0b8;
}

.cell.black {
  background-color: #948979;
}
</style>
