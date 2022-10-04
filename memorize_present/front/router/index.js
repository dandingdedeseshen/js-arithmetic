import { createRouter, createWebHistory } from 'vue-router'
import arr2022 from './2022'

const routes = [
  {
    path: '/',
    name: 'menu',
    component: () => import('@/components/menu')
  },
]

const router = createRouter({
  base:'./dist',
  history: createWebHistory(process.env.BASE_URL),
  routes : [...routes,...arr2022]
})

export default router
