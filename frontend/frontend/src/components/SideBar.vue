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
/* Sidebar styling */
.sidebar {
  width: 210px; /* Fixed width */
  background-color: #908f8f; /* Grey background (inverse of main content) */
  color: #2c3e50; /* Blue font color (inverse of main content) */
  min-height: 100vh; /* Ensure the sidebar takes the full height of the viewport */
  margin: 0; /* Remove any default margins */
}

/* Sidebar heading and link styles */
.sidebar h1,
.sidebar ul,
.sidebar li {
  color: #2c3e50; /* Sidebar font color */
  text-align: center;
}

.sidebar ul {
  list-style-type: none; /* Remove bullet points from the list */
  padding: 0; /* Remove default padding */
}

.sidebar li {
  margin-bottom: 10px; /* Add space between the links */
}

.sidebar a {
  color: #2c3e50; /* Ensure links use the sidebar's font color */
  text-decoration: none; /* Remove underline from links */
}

.sidebar a:hover {
  background-color: #b0afaf;
  padding: 5px;
  border-radius: 10px;
}
</style>
