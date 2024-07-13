import { createRouter, createWebHistory } from 'vue-router'
import Chess from '@/components/Chess.vue'

const routes = [
  {
    path: '/chess',
    name: 'Chess',
    component: Chess,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
