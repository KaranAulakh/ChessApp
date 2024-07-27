<template>
  <div>
    <p>{{ board }}</p>
  </div>
</template>

<script>
import { getFromFlask } from "@/services/apiService";

export default {
  name: "homeView",
  data() {
    return {
      board: "",
    };
  },
  methods: {
    getResponse() {
      const path = "/play";
      getFromFlask(path)
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
