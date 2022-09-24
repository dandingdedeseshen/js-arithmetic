import { createApp } from 'vue'
import App from './App.vue'
import router from '../router'
import store from './store'
import ElementPlus from 'element-plus'

// CSS
import "./assets/index.css";         // 公共样式
import './assets/font/iconfont.css'  // 字体
import 'element-plus/dist/index.css' // element样式

createApp(App).use(store).use(router).use(ElementPlus).mount('#app')
