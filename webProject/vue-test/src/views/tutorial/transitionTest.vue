<template>
  <div class="home" id="transitionView">
    <button @click="addNum">改变</button>
    <transition-group tag='h1' name="list">
      <div v-for="item of arr" :key="item" class="list-item">
        {{ item }}
      </div>
    </transition-group>
  </div>
</template>

<script>

export default {
  name: "transitionTest",
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
  
};
</script>

<style>
#transitionView .list-item {
  transition: transform 1s ease, opacity 1s ease;
  display: inline-block;
  margin-right: 10px;
}
#transitionView .list-enter-from,
#transitionView .list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}
#transitionView .list-leave-active {
  position: absolute;
}
</style>
