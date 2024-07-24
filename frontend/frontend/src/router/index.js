import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/components/HomeView.vue";
import Chessboard from "@/components/Chessboard.vue";

const routes = [
  {
    path: "/",
    name: "homeView",
    component: HomeView,
  },
  {
    path: "/play",
    name: "chessBoard",
    component: Chessboard,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
