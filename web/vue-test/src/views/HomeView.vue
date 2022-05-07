<template>
  <div class="home" id="homeView">
    <HelloWorld :style="{ 'font-size': '100px' }" />
    <button @click="addNum">改变</button>
    <transition-group tag='h1' name="list">
      <div v-for="item of arr" :key="item" class="list-item">
        {{ item }}
      </div>
    </transition-group>
  </div>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  data() {
    return {
      num: 1,
      arr : [3,6,9]
    };
  },
  methods: {
    addNum() {
      this.num++;
      this.num = (this.num > 2)?0 : this.num
      let arr = []
      for(let item of [1,2,3,4,5,6,7,8,9,10]){
        if(item % 3 === this.num) arr.push(item)
      }
      this.arr = arr
      console.log(this.num);      
    },
  },
  components: {
    HelloWorld,
  },
};
</script>

<style>
#homeView .list-item {
  transition: transform 1s ease, opacity 1s ease;
  display: inline-block;
  margin-right: 10px;
}
#homeView .list-enter-from,
#homeView .list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}
</style>
