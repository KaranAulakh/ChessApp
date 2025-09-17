<template>
  <div v-if="visible" class="popup-overlay">
    <div class="popup-container">
      <div class="popup-header">
        <h2>{{ popupContent.title }}</h2>
      </div>

      <div class="popup-content">
        <div class="game-result-icon">{{ popupContent.icon }}</div>
        <p class="result-message">{{ popupContent.message }}</p>
        <div v-if="winner" class="winner-info">
          <span>{{ winner }} wins!</span>
        </div>
      </div>

      <div class="popup-actions">
        <button class="btn btn-primary" @click="newGame">
          {{ buttonText }}
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
  computed: {
    buttonText() {
      return this.gameState === "welcome" ? "Start Game" : "New Game";
    },

    popupContent() {
      const content = {
        welcome: {
          title: "Welcome to Chess!",
          icon: "♟️",
          message: "Click Start Game to begin!",
        },
        checkmate: {
          title: "Checkmate!",
          icon: "🏆",
          message: "The king has been checkmated!",
        },
        stalemate: {
          title: "Draw!",
          icon: "🤝",
          message: "Draw due to stalemate",
        },
        "insufficient material": {
          title: "Draw!",
          icon: "⚖️",
          message: "Draw due to insufficient material",
        },
        "three-fold repetition": {
          title: "Draw!",
          icon: "🔄",
          message: "Draw due to three fold repetition",
        },
        time_expired: {
          title: "Time's Up!",
          icon: "⏰",
          message: "Time has expired!",
        },
      };

      return (
        content[this.gameState] || {
          title: "Game Over!",
          icon: "⚖️",
          message: "The game has ended!",
        }
      );
    },
  },
  methods: {
    newGame() {
      this.$emit("new-game");
    },
  },
};
</script>

<style scoped>
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

.winner-info {
  background: #22313f;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 16px;
}

.popup-container {
  background: #2c3e50;
  border-radius: 12px;
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
  padding: 24px;
  max-width: 320px;
  width: 85%;
  text-align: center;
  animation: popup-appear 0.3s ease-out;
}

.game-result-icon {
  font-size: 36px;
  margin-bottom: 12px;
}
</style>
