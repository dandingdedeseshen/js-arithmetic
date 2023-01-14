import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/index'),
    children:[
      {
        path: '/tutorial/combinationApi',
        name: 'combinationApi',
        component: () => import('@/views/tutorial/combinationApi/combinationApi.vue'),
      },
      {
        path: '/tutorial/printPage',
        name: 'printPage',
        component: () => import('@/views/tutorial/printPage.vue'),
      },
      {
        path: '/tutorial/transitionTest',
        name: 'transitionTest',
        component: () => import('@/views/tutorial/transitionTest.vue'),
      },
      {
        path: '/tutorial/myAttribute',
        name: 'myAttribute',
        component: () => import('@/views/tutorial/myAttribute.vue'),
      },
    ]
  },
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
