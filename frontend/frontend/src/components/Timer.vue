<template>
  <div class="timer-base" :class="isActive ? 'timer-active' : 'timer-inactive'">
    <div v-if="playerName" class="player-label">{{ playerName }}</div>
    <div
      class="timer-display monospace-display"
      :class="{ 'pulse-glow': isActive }"
    >
      {{ formattedTime }}
    </div>
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
    this.intervalId = setInterval(() => {
      if (this.isActive && this.timeRemaining > 0) {
        this.timeRemaining--;
        if (this.timeRemaining === 0) {
          this.$emit("timer-expired", this.playerName);
        }
      }
    }, 1000);
  },
  beforeUnmount() {
    if (this.intervalId) clearInterval(this.intervalId);
  },
};
</script>

<style scoped>
.player-label {
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.timer-display {
  font-size: 24px;
  margin-bottom: 4px;
}

.pulse-glow {
  animation: pulse-glow 2s infinite;
}

@keyframes pulse-glow {
  0%, 100% { text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1); }
  50% { text-shadow: 0 0 10px rgba(255, 255, 255, 0.5); }
}
</style>
