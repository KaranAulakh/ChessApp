<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ChessBoard',
  data() {
    return {
      msg: '',
    }
  },
  methods: {
    getChessBoard() {
      const path = 'http://localhost:5000/chess'
      axios
        .get(path)
        .then((res) => {
          console.log(res.data)
          this.msg = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getChessBoard()
  },
}
</script>
