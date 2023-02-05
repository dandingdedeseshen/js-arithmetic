import { createRouter, createWebHistory } from 'vue-router'
import arr2022 from './2022'
import arr2023 from './2023'

const routes = [
  {
    path: '/menu',
    name: 'menu',
    component: () => import('@/components/menu')
  },
  {
    path: '/',
    name: 'login',
    component: () => import('@/components/login')
  },
]

const router = createRouter({
  base:'./dist',
  history: createWebHistory(process.env.BASE_URL),
  routes : [...routes, ...arr2022, ...arr2023]
})

// 全局前置守卫
router.beforeEach((to, from) => {
  let userData = JSON.parse(localStorage.getItem('userData'))
  if(to.path !== "/" && !userData){ // 未登录
    return '/'
  }
  if(to.path == "/" && userData){
    return '/menu'
  }
})

export default router
