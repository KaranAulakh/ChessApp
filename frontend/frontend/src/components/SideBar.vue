<template>
  <div class="sidebar">
    <h1>Sidebar</h1>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/play">Play Chess</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "SideBar",
};
</script>

<style scoped>
.sidebar {
  width: 210px;
  background-color: #908f8f;
  color: #2c3e50;
  min-height: 100vh;
  margin: 0;
}

/* Sidebar heading and link styles */
.sidebar h1,
.sidebar ul,
.sidebar li {
  color: #2c3e50;
  text-align: center;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
}

.sidebar li {
  margin-bottom: 10px;
}

.sidebar a {
  color: #2c3e50;
  width: 100%;
  text-decoration: none; /* to remove the underline */
  padding: 10px;
}

.sidebar a:hover {
  background-color: #b0afaf;
  border-radius: 10px;
  width: 100%;
}
</style>
