import Vue from 'vue';
import Router from 'vue-router';


Vue.use(Router);

import index from '@/page/index';
import warehouse from '@/page/warehouse/warehouse';


// 解决ElementUI导航栏中的vue-router在3.0版本以上重复点菜单报错问题
const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index,
    },
    {
      path:'/warehouse',
      name:'warehouse',
      component: warehouse,
    }
  ],
});
