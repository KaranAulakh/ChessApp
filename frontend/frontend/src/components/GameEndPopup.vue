<template>
  <div v-if="visible" class="popup-overlay" @click="close">
    <div class="popup-container" @click.stop>
      <div class="popup-header">
        <h2>{{ getTitle() }}</h2>
      </div>

      <div class="popup-content">
        <div class="game-result-icon">{{ getIcon() }}</div>
        <p class="result-message">{{ getMessage() }}</p>
        <div v-if="winner" class="winner-info">
          <span class="crown">👑</span>
          <span class="winner-text">{{ winner }} wins!</span>
        </div>
      </div>

      <div class="popup-actions">
        <button class="btn btn-primary" @click="newGame">
          {{ gameState === "welcome" ? "Start Game" : "New Game" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameEndPopup",
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
    gameState: {
      type: String,
      default: null,
    },
    winner: {
      type: String,
      default: null,
    },
  },
  methods: {
    getTitle() {
      switch (this.gameState) {
        case "welcome":
          return "Welcome to Chess!";
        case "checkmate":
          return "Checkmate!";
        case "stalemate":
          return "Stalemate!";
        case "insufficient material":
          return "Draw!";
        case "three-fold repetition":
          return "Draw!";
        case "time_expired":
          return "Time's Up!";
        default:
          return "Game Over!";
      }
    },

    getIcon() {
      switch (this.gameState) {
        case "welcome":
          return "♟️";
        case "checkmate":
          return "🏆";
        case "stalemate":
          return "🤝";
        case "time_expired":
          return "⏰";
        default:
          return "⚖️";
      }
    },

    getMessage() {
      switch (this.gameState) {
        case "welcome":
          return "Ready to play a game of chess? Click Start Game to begin!";
        case "checkmate":
          return "The king has been checkmated!";
        case "stalemate":
          return "No legal moves available!";
        case "insufficient material":
          return "Insufficient material to checkmate!";
        case "three-fold repetition":
          return "Position repeated three times!";
        case "time_expired":
          return "Time has expired!";
        default:
          return "The game has ended!";
      }
    },

    newGame() {
      this.$emit("new-game");
    },
  },
};
</script>

<style scoped>
.popup-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 512px; /* Same width as chessboard */
  height: 512px; /* Same height as chessboard */
  background-color: rgba(0, 0, 0, 0.75);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(3px);
  border-radius: 4px;
}

.popup-container {
  background: linear-gradient(135deg, #ffffff, #f8f9fa);
  border-radius: 12px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
  padding: 24px;
  max-width: 320px;
  width: 85%;
  text-align: center;
  animation: popup-appear 0.3s ease-out;
  border: 2px solid #e9ecef;
}

@keyframes popup-appear {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.popup-header h2 {
  margin: 0 0 16px 0;
  color: #2c3e50;
  font-family: "Copperplate", fantasy;
  font-size: 22px;
}

.game-result-icon {
  font-size: 36px;
  margin-bottom: 12px;
}

.result-message {
  font-size: 14px;
  color: #2c3e50;
  margin: 0 0 16px 0;
}

.winner-info {
  background: linear-gradient(135deg, #ffd700, #ffed4e);
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 16px;
}

.crown {
  font-size: 20px;
  margin-right: 6px;
}

.winner-text {
  font-size: 16px;
  font-weight: bold;
  color: #8b4513;
}

.popup-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #4caf50, #45a049);
  color: white;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #45a049, #3e8e41);
  transform: translateY(-2px);
}

.btn-secondary {
  background: linear-gradient(135deg, #6c757d, #5a6268);
  color: white;
}

.btn-secondary:hover {
  background: linear-gradient(135deg, #5a6268, #495057);
  transform: translateY(-2px);
}
</style>
