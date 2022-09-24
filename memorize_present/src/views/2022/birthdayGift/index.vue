<template>
  <div>
    <transition name="el-fade-in-linear">
      <div class="two_wrap" v-if="pageFlag === 0">
        <div class="left_wrap" @click="pageFlag = 1">
          <span class="iconfont icon-gift font1"></span>
          <span class="iconfont icon-si-glyph-birthday-cake font2"></span>
        </div>
        <div class="right_wrap" @click="pageFlag = 2">
          <span class="iconfont icon-gift font1"></span>
          <span class="iconfont icon-si-glyph-birthday-cake font2"></span>
        </div>
      </div>
    </transition>
    <transition name="el-fade-in-linear">
      <Picture v-if="pageFlag === 1" @goBack='pageFlag = 0'></Picture>
    </transition>
    <transition name="el-fade-in-linear">
      <Fireworks v-if="pageFlag === 2" @goBack='pageFlag = 0'></Fireworks>
    </transition>
  </div>
</template>

<script>
import Picture from "./page/picture.vue";
import Fireworks from "./page/fireworks.vue";

export default {
  data() {
    return {
      pageFlag:0,
    };
  },
  components: {
    Picture,
    Fireworks
  },
};
</script>

<style lang="less">
.two_wrap {
  width: 100vw;
  height: 100vh;
  display: flex;
  div{
    width: 50vw;
    height: 100vh;
    opacity: 0.9;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .left_wrap {
    background-color: var(--theme-color1);
    position: relative;
    .iconfont{
      color: var(--theme-color2);
      position: absolute;
    }
    .font1{
      opacity: 0;
      transition: opacity .3s linear;
    }
    &:hover{
      .font2{
        opacity: 0;
      }
      .font1{
        display: inline-block;
        opacity: 1;
      }
    }
  }
  .right_wrap {
    background-color: var(--theme-color2);
    position: relative;
    .iconfont{
      color: var(--theme-color1);
      position: absolute;
    }
    .font2{
      opacity: 0;
      transition: opacity .3s linear;
    }
    &:hover{
      .font1{
        opacity: 0;
      }
      .font2{
        display: inline-block;
        opacity: 1;
      }
    }
  }
  .iconfont{
    font-size: 100px;
  }
}
</style>
