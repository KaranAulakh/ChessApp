<template>
  <div class="sidebar">
    <h1>Chess Lab</h1>
    <ul>
      <li @click="navigateTo('/')">
        <icon-images name="home"></icon-images>
        Home
      </li>
      <li @click="navigateTo('/play')">
        <icon-images name="play"></icon-images>
        Play
      </li>
    </ul>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
import IconImages from "../assets/IconImages.vue";

export default {
  name: "SideBar",
  components: {
    IconImages,
  },
  setup() {
    const router = useRouter();

    const navigateTo = (route) => {
      router.push(route);
    };

    return {
      navigateTo,
    };
  },
};
</script>

<style scoped>
.sidebar {
  width: 200px;
  background-color: #22313f;
  color: #908f8f;
  min-height: 100vh;
  margin: 0;
  li {
    color: #908f8f;
    text-align: left;
    padding-bottom: 10px;
    padding-top: 10px;
    padding-left: 20px;
    cursor: pointer;
  }
  ul {
    list-style-type: none;
    width: 100%;
    padding: 0px;
  }
  li:hover {
    background-color: #2c3e50;
    width: 100%;
  }
  a {
    color: #908f8f;
    width: 100%;
    text-decoration: none;
    padding: 10px;
    flex-grow: 1;
  }
}
</style>
