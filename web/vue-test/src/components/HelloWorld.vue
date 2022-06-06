<template>
  <!-- 属性继承 -->
  <div :style="{'color': 'black'}">11</div>
  <div :style="[$attrs.style,obj]">22</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data(){
    return{
      obj:{
        'color':'tomato'
      }
    }
  },
  props: {
    msg: String
  }
}
</script>

<style scoped lang="scss">
。出咯的{
  是的发送到发生111
}
</style>
