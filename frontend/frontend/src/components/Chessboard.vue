<template>
  <div>
    <p>{{ board }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "homeView",
  data() {
    return {
      board: "",
    };
  },
  methods: {
    getResponse() {
      const path = "http::localhost:5000/play";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.board = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
