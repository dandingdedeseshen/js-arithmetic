<template>
  <div id="menuWrap">
    <div class="back_wrap">
      <!-- 一级年份目录 -->
      <div class="menu_mid_wrap">
        <div
          v-for="index of 10"
          class="item"
          :key="index"
          @click="openMenu(index)"
        >
          <span class="text">{{ 2022 + index - 1 }}</span>
          <span
            :class="{ rotate: openIndex != index }"
            class="iconfont icon-jiantouyou"
          ></span>
        </div>
      </div>
      <!-- 二级事件目录 -->
      <transition mode="in-out">
        <div class="menu_mid_wrap" v-show="openIndex">
          <div
            v-for="item of sonMenu"
            class="item"
            :key="item.id"
            :class="{ disabled: item.disabled }"
            @click="gotoPage(item)"
          >
            <span class="text">{{ item.text }}</span>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import { MB13401 } from "@/api/menu";

export default {
  data() {
    return {
      openIndex: 0,
      sonMenu: [],
    };
  },
  methods: {
    async openMenu(index) {
      if(this.openIndex == index) return
      this.openIndex = 0;
      // menu1-todo 目前这里字面量写法，未来改成按年份调用接口
      let res = await MB13401({ id: index });
      this.sonMenu = res.data;
      let timer = setTimeout(() => {
        clearTimeout(timer)
        this.openIndex = index;
      },300)
    },
    gotoPage(item) {
      if(item.disabled) return
      this.$router.push(item.path);
    },
  },
};
</script>

<style lang="less">
@itemWidth : 390px;
#menuWrap {
  box-sizing: border-box;
  .back_wrap {
    padding-top: 5px;
    width: 800px;
    height: 99vh;
    margin: 0 auto;
    background-image: url("./assets/back.jpg");
    background-repeat: no-repeat;
    background-size: 800px;
    display: flex;
  }
  .menu_mid_wrap {
    width: @itemWidth;
    height: 98vh;
    margin-left: 5px;
    overflow: auto;
    background: white;
    opacity: 0.6;
    border-radius: 10px;
    &::-webkit-scrollbar {
      background: #96f3f3;
      opacity: 0.1;
    }
  }
  .item {
    width: 100%;
    height: 6vh;
    box-sizing: border-box;
    display: flex;
    padding: 0 10px;
    align-items: center;
    border-bottom: 1px solid var(--font-color);
    overflow: hidden;
    cursor: pointer;
    .text {
      width: 100%;
      text-align: center;
      font-size: 20px;
      font-weight: 600px;
    }
    .iconfont {
      transition: transform 0.3s linear;
      transform: rotate(0);
    }
    .rotate {
      transform: rotate(180deg);
    }
  }
  .v-enter-active {
    transition: all 0.3s ease-out;
    //animation: bounce-in 0.5s;
  }
  /* 可以为进入和离开动画设置不同的持续时间和动画函数 */
  .v-enter-from{
    transform: scaleX(0);
    transform-origin: left;
    opacity: 0;
  }
}
@media screen and (max-width: 430px) {
  @itemWidth : 48vw;
  #menuWrap {
    .back_wrap{
      width: 100vw;
      height: 99vh;
      background-size: 100vw;
    }
    .menu_mid_wrap {
      width: @itemWidth;
    }
  }
}
</style>
