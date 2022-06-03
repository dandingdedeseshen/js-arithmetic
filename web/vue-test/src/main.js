import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import renderFun from '@/components/renderFun'

import 'element-plus/dist/index.css'

// App.mixins = [
//     {
//         msg: 'mixin',
//     }
// ]
const app = createApp(App)
// 自定义mixin合并策略
// const app = createApp({
//     msg: 'Vue',
//     mixins: [
//       {
//         msg: 'mixin ',
//       }
//     ],
//   })
// app.config.optionMergeStrategies.msg = (toVal, fromVal) => {
//     console.log(toVal,fromVal)
//     return fromVal || toVal
// }
app.config.globalProperties.$router = router
app.use(router).use(ElementPlus).use(renderFun).mount('#app')
