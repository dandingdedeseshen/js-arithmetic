<template>
  <div class="home">
    <HelloWorld :style="{'font-size': '100px'}"/>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
