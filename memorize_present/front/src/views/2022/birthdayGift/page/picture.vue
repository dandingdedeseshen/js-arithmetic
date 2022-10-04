<template>
  <div class="btn_wrap">
    <el-button round @click="$emit('goBack')">返回</el-button>
    <div>
      <el-button round @click="photoChange">切换图片</el-button>
      <el-switch v-model="isAutoRotate" inactive-text="自动旋转" />
    </div>
  </div>
  <div
    id="birthdayPictureWrap"
    @mousemove="rotateWrapEvent"
    @mousedown="openRotate"
    @mouseup="closeRotate"
  >
      <div class="img_wrap" ref="imgWrap" @click="clcikImgWrap">
        <div class="front side">
            <img :src="require('../assets/img/01.jpg')" alt="0" :class="{opacity:photoGroupIndex != 0}"/>
            <img :src="require('../assets/img/07.jpg')" alt="0" style="transform: rotatez(-90deg)" :class="{opacity:photoGroupIndex != 1}"/>
        </div>
        <div class="back side">
          <img src="../assets/img/02.jpg" class="reservey" alt="1" :class="{opacity:photoGroupIndex != 0}"/>
          <img src="../assets/img/08.jpg" class="reservey" alt="1" :class="{opacity:photoGroupIndex != 1}"/>
        </div>
        <div class="left side">
          <img src="../assets/img/03.jpg" class="reservey" alt="2" :class="{opacity:photoGroupIndex != 0}"/>
          <img src="../assets/img/09.jpg" class="reservey" alt="2" :class="{opacity:photoGroupIndex != 1}"/>
        </div>
        <div class="right side">
          <img
            src="../assets/img/04.jpg"
            style="transform: rotatez(-90deg)"
            alt="3"
            :class="{opacity:photoGroupIndex != 0}"
          />
          <img
            src="../assets/img/10.jpg"
            alt="3"
            :class="{opacity:photoGroupIndex != 1}"
          />
        </div>
        <div class="top side">
          <img
            src="../assets/img/05.jpg"
            style="transform: rotatez(180deg)"
            alt="4"
            :class="{opacity:photoGroupIndex != 0}"
          />
          <img
            src="../assets/img/11.jpg"
            style="transform: rotatez(180deg)"
            alt="4"
            :class="{opacity:photoGroupIndex != 1}"
          />
        </div>
        <div class="bottom side">
          <img src="../assets/img/06.jpg" class="reservex" alt="5" :class="{opacity:photoGroupIndex != 0}"/>
          <img src="../assets/img/12.jpg" class="reservex" alt="5" :class="{opacity:photoGroupIndex != 1}"/>
        </div>
      </div>
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      screenX: 0,
      screenY: 0,
      xdeg: 45,
      ydeg: 45,
      rotateFlag: false,
      timer: null,
      isAutoRotate: false,
      photoGroupIndex: 0,
    };
  },
  destroyed() {
    clearInterval(this.timer);
  },
  watch: {
    isAutoRotate(val) {
      val ? this.autoRotate() : clearInterval(this.timer);
    },
  },
  emits:['goBack'],
  methods: {
    // 开启拖动状态
    openRotate(e) {
      this.rotateFlag = e.button === 0;
    },
    // 关闭拖动状态
    closeRotate(e) {
      this.rotateFlag = e.button !== 0;
    },
    // 鼠标移动事件
    rotateWrapEvent(e) {
      if (!this.rotateFlag) return;
      this.rotateWrap(e.screenX, e.screenY);
    },
    // 根据鼠标坐标转动盒子
    rotateWrap(screenX, screenY) {
      const sensibility = 0;
      const sensibilityRotate = 0.5;
      let imgWrap = this.$refs.imgWrap;
      if (screenX - this.screenX > sensibility) {
        this.ydeg += sensibilityRotate;
      } else if (screenX - this.screenX < 0 - sensibility) {
        this.ydeg -= sensibilityRotate;
      }
      if (screenY - this.screenY > sensibility) {
        this.xdeg -= sensibilityRotate;
      } else if (screenY - this.screenY < 0 - sensibility) {
        this.xdeg += sensibilityRotate;
      }
      imgWrap.style.transform = `rotateX(${this.xdeg}deg) rotateY(${this.ydeg}deg)`;
      this.screenX = screenX;
      this.screenY = screenY;
    },
    // 自动旋转
    autoRotate() {
      this.timer = setInterval(() => {
        const rate = 0.5;
        let imgWrap = this.$refs.imgWrap;
        if (!imgWrap) {
          clearInterval(this.timer);
        }
        this.xdeg -= rate;
        this.ydeg -= rate;
        imgWrap.style.transform = `rotateX(${this.xdeg}deg) rotateY(${this.ydeg}deg)`;
      }, 30);
    },
    // 点击盒子
    clcikImgWrap(e) {
      let index = e.target.alt;
      let imgWrap = this.$refs.imgWrap;
      const arr = [
        [0, 0],
        [0, 180],
        [0, 90],
        [0, -90],
        [-90, 0],
        [90, 0],
      ];
      this.isAutoRotate = false;
      this.xdeg = arr[index][0];
      this.ydeg = arr[index][1];
      imgWrap.style.transition = `transform .3s linear`;
      imgWrap.style.transform = `rotateX(${this.xdeg}deg) rotateY(${this.ydeg}deg)`;
      let timer = setTimeout(() => {
        clearTimeout(timer);
        imgWrap.style.transition = `none`;
      }, 300);
    },
    // 切换图片
    photoChange(e) {
      this.photoGroupIndex =
        (this.photoGroupIndex == 1) ? 0 : this.photoGroupIndex + 1;
    },
  },
};
</script>

<style lang="less">
@side_width: 40vw;
.btn_wrap {
  height: 30px;
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
#birthdayPictureWrap {
  width: 100%;
  height: calc(100vh - 50px);
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  overflow: hidden;
  background-image: url('../assets/img/sky.jpg');
  background-size: cover;
  .img_wrap {
    width: @side_width;
    height: @side_width;
    position: relative;
    transform-style: preserve-3d;
    transform-origin: 20vw 20vw -20vw;
    transform: rotateX(45deg) rotateY(45deg);
    .side {
      width: @side_width;
      height: @side_width;
      opacity: 0.9;
      position: absolute;
      top: 0;
      left: 0;
      img {
        width: 100%;
        height: 100%;
        transition: opacity .3s linear;
        position: absolute;
      }
      .opacity{
        opacity: 0;
      }
      &:hover {
        opacity: 1;
      }
    }
    .back {
      transform: translateZ(-@side_width);
    }
    .left {
      transform-origin: 0 0;
      transform: rotateY(90deg);
    }
    .right {
      transform-origin: @side_width;
      transform: rotateY(-90deg);
    }
    .top {
      transform-origin: 0 0;
      transform: rotateX(-90deg);
    }
    .bottom {
      transform-origin: 0 @side_width;
      transform: rotateX(90deg);
    }
    .reservex {
      transform: rotateX(180deg);
    }
    .reservey {
      transform: rotateY(180deg);
    }
  }
}
</style>
