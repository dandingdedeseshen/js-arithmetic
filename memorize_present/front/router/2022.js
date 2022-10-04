
const routes = [
  {
    path: '/2022',
    name: '2022',
    children: [
      {
        path: 'birthday',
        name: 'birthday',
        component: () => import('@/views/2022/birthdayGift')
      },
      {
        path: 'hundredDays',
        name: 'hundredDays',
        component: () => import('@/views/2022/hundredDays')
      }
    ]
  },
]

export default routes