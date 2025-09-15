<template>
  <div
    class="timer-container"
    :class="{ 'active-timer': isActive, 'paused-timer': !isActive }"
  >
    <div class="player-label" v-if="playerName">{{ playerName }}</div>
    <div class="timer-display">{{ formattedTime }}</div>
  </div>
</template>

<script>
export default {
  name: "ChessTimer",
  props: {
    playerName: {
      type: String,
      required: true,
    },
    initialTime: {
      type: Number,
      default: 600,
    },
    isActive: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      timeRemaining: this.initialTime,
      intervalId: null,
    };
  },
  computed: {
    formattedTime() {
      const minutes = Math.floor(this.timeRemaining / 60);
      const seconds = this.timeRemaining % 60;
      return `${minutes.toString().padStart(2, "0")}:${seconds
        .toString()
        .padStart(2, "0")}`;
    },
  },
  mounted() {
    // Set up interval once and let it run continuously
    this.intervalId = setInterval(() => {
      // Only countdown if this timer is active and has time remaining
      if (this.isActive && this.timeRemaining > 0) {
        this.timeRemaining--;
        if (this.timeRemaining === 0) {
          this.$emit("timer-expired", this.playerName);
        }
      }
    }, 1000);
  },
  methods: {},
  beforeUnmount() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  },
};
</script>

<style scoped>
.timer-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px 16px;
  margin: 0;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  min-width: 120px;
}

.active-timer {
  background: linear-gradient(135deg, #4caf50, #45a049);
  color: white;
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(76, 175, 80, 0.3);
}

.paused-timer {
  background: linear-gradient(135deg, #f5f5f5, #e0e0e0);
  color: #333;
}

.player-label {
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.timer-display {
  font-size: 24px;
  font-family: "Courier New", monospace;
  font-weight: bold;
  margin-bottom: 4px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.active-timer .timer-display {
  animation: pulse-glow 2s infinite;
}

@keyframes pulse-glow {
  0%,
  100% {
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
  }
  50% {
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
  }
}
</style>
