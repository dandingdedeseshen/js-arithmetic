import { createApp } from 'vue'
import App from './App.vue'
import router from '../router'
import store from './store'
import ElementPlus from 'element-plus'

// CSS
import "./assets/index.css";         // 公共样式
import './assets/font/iconfont.css'  // 字体
import 'element-plus/dist/index.css' // element样式
import 'animate.css'                 // 动画库
import 'amfe-flexible'               // 移动端适配

let vue = createApp(App)
// 设置全局变量
vue.config.globalProperties.router = router

vue.use(store).use(router).use(ElementPlus).mount('#app')