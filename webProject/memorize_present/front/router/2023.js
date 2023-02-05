
const routes = [
  {
    path: '/2023',
    name: '2023',
    children: [
      {
        path: 'updateFile',
        name: 'updateFile',
        component: () => import('@/views/2023/updateFile'),
        meta: {
          transition : 'bounceIn'
        }
      }
    ]
  },
]

export default routes