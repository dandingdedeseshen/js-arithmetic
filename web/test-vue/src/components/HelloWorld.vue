<template>
  <div :style="{'color': 'red'}">11</div>
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
</style>
