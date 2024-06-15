import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/chess",
    name: "Chessboard",
    /*
     * Maybe I shouldn't lazy load everything
     */
    component: () => import("@/components/ChessBoard.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
