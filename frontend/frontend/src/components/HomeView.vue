<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import { apiServiceGET } from "@/utils/apiService";

export default {
  name: "homeView",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    async getResponse() {
      const path = "/";
      const res = await apiServiceGET(path);
      if (res.success) {
        this.msg = res.data;
      } else {
        this.msg = res.errorMsg;
      }
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
