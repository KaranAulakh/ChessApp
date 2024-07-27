import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/components/HomeView.vue";
import PlayChess from "@/components/PlayChess.vue";

const routes = [
  {
    path: "/",
    name: "homeView",
    component: HomeView,
  },
  {
    path: "/play",
    name: "playChess",
    component: PlayChess,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
