import App from './App'
import Vue from 'vue'
import messages from './locale/index'
import VueI18n from 'vue-i18n'
import request from '@/api/index.js';

// 配置vue全局变量
Vue.prototype.$request = request

// 获取国际化实例
let i18nConfig = {
  locale: uni.getLocale(),
  messages
}
Vue.use(VueI18n)
const i18n = new VueI18n(i18nConfig)
// 配置vue实例
Vue.config.productionTip = false
App.mpType = 'app'
const app = new Vue({
	i18n,
    ...App
})
app.$mount()