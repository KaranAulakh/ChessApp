<template>
  <div class="app-container">
    <h1>Welcome to Chess</h1>

    <!-- Black Timer (Top) -->
    <div class="timer-section top">
      <ChessTimer
        ref="blackTimer"
        playerName=""
        :initialTime="600"
        :isActive="!gameState.whiteToMove"
        @timer-expired="handleTimerExpired"
      />
    </div>

    <ChessBoard @game-state-updated="handleGameStateUpdate" />

    <!-- White Timer (Bottom) -->
    <div class="timer-section bottom">
      <ChessTimer
        ref="whiteTimer"
        playerName=""
        :initialTime="600"
        :isActive="gameState.whiteToMove"
        @timer-expired="handleTimerExpired"
      />
    </div>
  </div>
</template>

<script>
import ChessBoard from "./ChessBoard.vue";
import ChessTimer from "./Timer.vue";

export default {
  name: "PlayChess",
  components: {
    ChessBoard,
    ChessTimer,
  },
  data() {
    return {
      gameState: {
        whiteToMove: true,
      },
    };
  },
  methods: {
    handleGameStateUpdate(newGameState) {
      this.gameState = { ...newGameState };
    },
    handleTimerExpired(playerName) {
      console.log(`${playerName}'s time is up!`);
      // Handle game end due to time expiry
      // You can emit an event or call an API here
    },
  },
};
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

h1 {
  margin-bottom: 20px;
  color: #333;
  font-family: "Arial", sans-serif;
}

.timer-section {
  display: flex;
  justify-content: flex-end;
  width: 512px; /* Same width as chessboard (8 * 64px) */
  padding-right: 0;
}

.timer-section.top {
  margin-bottom: 5px;
}

.timer-section.bottom {
  margin-top: 5px;
}
</style>
