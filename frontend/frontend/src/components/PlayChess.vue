<template>
  <div class="app-container">
    <div class="game-container">
      <!-- Black Timer -->
      <div class="timer-section top">
        <ChessTimer
          ref="blackTimer"
          playerName=""
          :initialTime="600"
          :isActive="!gameState.whiteToMove && gameInProgress"
          @timer-expired="handleTimerExpired"
        />
      </div>

      <!-- Chess Board with Popup Container -->
      <div class="board-container">
        <ChessBoard @game-state-updated="handleGameStateUpdate" />

        <!-- Game End Popup positioned over chess board -->
        <GameEndPopup
          :visible="showPopup"
          :gameState="gameEndState"
          :winner="winner"
          @new-game="startNewGame"
        />
      </div>

      <!-- White Timer -->
      <div class="timer-section bottom">
        <ChessTimer
          ref="whiteTimer"
          playerName=""
          :initialTime="600"
          :isActive="gameState.whiteToMove && gameInProgress"
          @timer-expired="handleTimerExpired"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ChessBoard from "./ChessBoard.vue";
import ChessTimer from "./Timer.vue";
import GameEndPopup from "./GameEndPopup.vue";

export default {
  name: "PlayChess",
  components: {
    ChessBoard,
    ChessTimer,
    GameEndPopup,
  },
  data() {
    return {
      gameState: {
        whiteToMove: true,
      },
      gameEndState: "welcome", // "welcome" | null (playing) | "checkmate" | "stalemate" etc.
      winner: null,
    };
  },
  computed: {
    showPopup() {
      return this.gameEndState !== null; // Show popup when not actively playing
    },
    gameInProgress() {
      return this.gameEndState === null;
    },
    gameStarted() {
      return this.gameEndState !== "welcome";
    },
  },
  methods: {
    handleGameStateUpdate(newGameState) {
      this.gameState = { ...newGameState };

      // Show popup when game ends (only if game has started)
      if (
        this.gameStarted &&
        newGameState.gameEnded &&
        newGameState.gameState
      ) {
        this.gameEndState = newGameState.gameState;
        this.setWinner(newGameState.gameState, newGameState.whiteToMove);
      }
    },

    handleTimerExpired(playerName) {
      console.log(`${playerName}'s time is up!`);
      this.gameEndState = "time_expired";
      this.setWinner("time_expired", null, playerName);
    },

    startNewGame() {
      if (this.gameEndState === "welcome") {
        // Start the game
        this.gameEndState = null;
      } else {
        // Restart game
        window.location.reload();
      }
    },

    setWinner(gameEndState, whiteToMove, timerExpiredPlayer = null) {
      if (gameEndState === "checkmate") {
        this.winner = whiteToMove ? "Black" : "White";
      } else if (gameEndState === "time_expired" && timerExpiredPlayer) {
        this.winner = timerExpiredPlayer === "White" ? "Black" : "White";
      } else {
        this.winner = null; // Draw cases
      }
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

.board-container {
  position: relative;
  display: inline-block;
}

.timer-section {
  display: flex;
  justify-content: flex-end;
  width: 512px; /* Same width as chessboard (8 * 64px) */
  padding-right: 0;
  margin: 0;
}
</style>
