<template>
  <div class="btn_wrap">
    <el-button round @click="goBack">返回</el-button>
    <div>
      <!-- <el-button round @click="photoChange">切换图片</el-button> -->
      <!-- <el-switch v-model="isAutoRotate" inactive-text="自动旋转" /> -->
    </div>
  </div>
  <canvas class="canvans" @click="addFire"/>
</template>

<script>
import {FireWork} from '../assets/fireWork.js'
let fireWork = null

export default {
  data() {
    return {
    };
  },
  mounted() {
   fireWork = new FireWork()
  },
  destroyed(){
    fireWork.destroyed()
  },
  emits: ["goBack"],
  methods:{
    goBack(){
      fireWork.destroyed()
      this.$emit('goBack')
    },
    addFire(){
      fireWork.addFire()
    }
  }
};
</script>

<style lang="less" scoped>
.btn_wrap {
  position: fixed;
  height: 30px;
  width: 100vw;
  background: skyblue;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  color: white;
  span {
    color: white !important;
  }
  .el-button {
    margin-right: 10px;
    span {
      color: skyblue !important;
    }
  }
}
.canvans {
  padding: 0;
  margin: 0;
  background-image: url('../assets/img/fireWork.jpg');
  // background: black;
  background-size: cover;
}
</style>
