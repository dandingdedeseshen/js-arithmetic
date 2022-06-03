<script>
// import FirstDemo from "@/components/tutorial/firstDemo.vue";
import  { 
  h,
  // resolveComponent 
} from 'vue'

export default {
  name: "renderFun",
  data() {
    return {};
  },
  render() {
    // 渲染普通元素
    return h('div',{style:{ 'font-size': '30px' }},[1,h('div',null,2)])
    // 渲染组件
    // const slotObj = {default:'hello! i am created by renderFun to default',hasName:'hello! i am created by renderFun to hasName'}
    // return h(FirstDemo,{style:{ 'font-size': '100px' },msg:'66777'},slotObj)
    // 渲染全局注册的组件
    // return h(resolveComponent('el-button'),{style:{ 'font-size': '12px' },msg:'66777'},'确认')
    // 渲染字符串
    // return (<div>hello! i am created by template</div>)
  },
  install(app){
    app.component('RenderFun',this)
  }
};
</script>

<style></style>
