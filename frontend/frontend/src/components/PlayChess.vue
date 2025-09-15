<template>
  <div class="app-container">
    <div class="game-container">
      <!-- Black Timer -->
      <div class="timer-section top">
        <ChessTimer
          ref="blackTimer"
          playerName=""
          :initialTime="600"
          :isActive="!gameState.whiteToMove"
          @timer-expired="handleTimerExpired"
        />
      </div>

      <!-- Chess Board -->
      <ChessBoard @game-state-updated="handleGameStateUpdate" />

      <!-- White Timer -->
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
/* Override the global app-container spacing */
.app-container {
  justify-content: center !important;
  align-items: center !important;
  gap: 0;
  padding: 20px;
}

.game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
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
  margin: 0;
}
</style>
