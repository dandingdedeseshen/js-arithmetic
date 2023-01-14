<template>
  <!-- 属性继承 -->
  <div :style="{'color': 'black'}">{{msg}}</div>
  <div :style="[$attrs.style,obj]">{{22}}{{33}}</div>
  <slot></slot>
  <br>
  <slot name="hasName"></slot>
</template>

<script>

export default {
  name: 'FirstDemo',
  data(){
    return{
      obj:null,
    }
  },
  created() {
    let res = {
      color:'tomato',
    }
    this.obj = {...res}
  },
  props: {
    msg: {
      type:String,
      default:'11222'
    },
    modelValue:{
      type:Number,
      default:1
    },
  },
}
</script>

<style scoped lang="scss">
</style>
