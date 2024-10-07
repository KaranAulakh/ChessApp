<template>
  <div class="flex">
    <SideBar />
    <div class="flex-1 flex justify-center">
      <router-view />
    </div>
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
