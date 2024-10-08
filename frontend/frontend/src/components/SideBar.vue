<template>
  <div class="sidebar">
    <h1>Échecs</h1>
    <ul>
      <li>
        <icon-images name="home"></icon-images
        ><router-link to="/">Home</router-link>
      </li>
      <li>
        <icon-images name="play"></icon-images>
        <router-link to="/play">Play</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import IconImages from "../assets/IconImages.vue";

export default {
  name: "SideBar",
  components: {
    IconImages,
  },
};
</script>

<style scoped>
.sidebar {
  width: 150px;
  background-color: #22313f;
  color: #908f8f;
  min-height: 100vh;
  margin: 0;
}

/* Sidebar heading and link styles */
.sidebar h1 {
  color: #908f8f;
  text-align: center;
}

.sidebar ul,
.sidebar li {
  color: #908f8f;
  text-align: left;
  padding-bottom: 10px;
  padding-top: 10px;
  padding-left: 20px;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
}

.sidebar li:hover {
  background-color: #2c3e50;
  width: 100%;
}

.sidebar a {
  color: #908f8f;
  width: 100%;
  text-decoration: none; /* to remove the underline */
  padding: 10px;
  flex-grow: 1;
}
</style>
