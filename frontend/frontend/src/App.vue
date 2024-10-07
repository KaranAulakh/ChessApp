<template>
  <div class="flex">
    <SideBar />
    <router-view class="app-container" />
  </div>
</template>

<script>
import SideBar from "./components/SideBar.vue";

export default {
  name: "App",
  components: {
    SideBar,
  },
};
</script>
