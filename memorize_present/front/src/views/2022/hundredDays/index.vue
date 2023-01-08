<template>
  <div>
    <div>back</div>
    <div class="first_wrap" v-show="flag == 1">
      <div class="back_wrap"></div>
      <div class="text">
        <div class="animated fadeInDown">小曹老师</div>
        <div class="animated fadeInRight" style="--delay:1s">2022年7月19号21点29分</div>
        <div class="animated fadeInDown" style="--delay:2s">小刘迎来了您的第一声打招呼</div>

        <div class="animated fadeInDown" style="--delay:4s;margin-top:20px">眨眼已经过去</div>
        <div class="animated fadeInLeft positionWrap" style="--delay:5s">{{ yy }}年{{ dd }}天{{ hh }}小时{{ mm }}分
          <transition enter-active-class="animated flipInX" mode="out-in">
            <span v-show="(ss % 2) == 0">{{ ss }}</span> 
          </transition>
          <transition enter-active-class="animated flipInX" mode="out-in">
            <span v-show="(ss % 2) != 0">{{ ss }}</span> 
          </transition>
          <div style="display:inline-block;width:1.5em"></div>
        秒</div>

        <div class="animated fadeInDown" style="--delay:7s;margin-top:20px">总计</div>
        <div class="animated fadeInUp positionWrap" style="--delay:8s">
          <div>{{ y }}年</div>
          <div>{{ d }}天</div>
          <div>{{ h }}小时</div>
          <div>{{ m }}分</div>
          <div></div>
          <transition enter-active-class="animated flipInX" mode="out-in">
            <span v-show="(s % 2) == 0">{{ s }}</span> 
          </transition>
          <transition enter-active-class="animated flipInX" mode="out-in">
            <span v-show="(s % 2) != 0">{{ s }}</span> 
          </transition>
          <div style="display:inline-block;width:4.5em"></div>
        秒</div>

        <div class="animated fadeInUp" style="--delay:10s;margin-top:20px">
          慢慢的经历，磕磕绊绊，甜甜蜜蜜，
          <div class="animated fadeIn" style="--delay:12s;display:inline">但最重要的是小曹不嫌弃，</div> 
          <div class="animated fadeIn" style="--delay:13s;display:inline">小刘一直在(๑*◡*๑)。</div> 
        </div>
      </div>
      <div class="animated fadeInUp btn">
        <div class="memorizeBtn" @click="() => {flag = 2}">一起回忆一下吧</div>
      </div>
    </div>
    <transition enter-active-class="animated fadeIn">
      <div  class="second_wrap" v-show="flag == 2">
        <div class="back_wrap"></div>
        <div class="text">
          <div class="animated fadeInDown">首先看到的是</div>
          <div class="animated fadeInDown" style="--delay:1s">小曹老师的送给小刘的第一个礼物</div>
          <div class="animated fadeInLeft" style="--delay:3s;margin-top:20px">叮咚~一声</div>
          <div class="animated fadeInDown" style="--delay:4s">一件礼物等待查收</div>
          <div class="animated fadeInDown" style="--delay:5s">拆开礼物</div>
          <div class="animated fadeInDown" style="--delay:6s">开心到小刘同学做梦都是甜的</div>
          <div class="animated fadeInDown" style="--delay:8s;margin-top:20px">承蒙问候</div>
          <div class="animated fadeInDown" style="--delay:9s">走进了我这二十几年无人问津的心</div>
          <div class="animated fadeInDown" style="--delay:10s">(✪ω✪)</div>
          <div class="animated fadeInUp btn" style="--delay:11s">
            <div class="memorizeBtn" @click="() => {flag = 3}">继续前进</div>
          </div>
        </div>
      </div>
    </transition>
    <transition enter-active-class="animated fadeIn">
      <div  class="thrid_wrap" v-show="flag == 3">
        <div v-for="i of 7" :class="activeClass(i) + ' transparent'" :key="i">
          <img :src="imgArr[i + 2]">
          <div :class="'message text' + i % 2">{{message[i - 1]}}</div>
          <div class="animated fadeInUp btn" style="--delay:1s" v-show=" activeImgIndex == 6">
            <div class="memorizeBtn" @click="() => {flag = 4}">继续前进</div>
          </div>
        </div>
        <div class="change-box" style="left:0" @click="activeImgIndex--" v-show="activeImgIndex > 1">
          <span class="iconfont icon-jiantouzuo-copy"></span>
        </div>
        <div class="change-box" style="right:0" @click="activeImgIndex++" v-show="activeImgIndex < 6">
          <span class="iconfont icon-jiantouyou"></span>
        </div>
      </div>
    </transition>
    <transition enter-active-class="animated fadeIn">
      <div  class="fort_wrap" v-show="flag == 4"></div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from "vue";
import dayjs from "dayjs";

// 页面变量
let flag = ref(1)   //页面标记
let activeImgIndex = ref(1) // 轮播图激活图片
let activeClass = (i) => {
  switch(activeImgIndex.value){
    case i - 1 :
      return 'back_wrap-left'
    case i :
      return 'back_wrap'
    case i + 1 :
      return 'back_wrap-right'
    default:
      return 'none'
  }
}
// 12617  5136 211.71
const message = ['在我们认识的这段时间里','微信聊天成了日常','我们聊天使用最频繁的词是"哈哈哈"（确实欢乐）','当然重头还是通话',
'小曹你知道吗,咱们目前总共打电话211.71小时','也就是说这段时间里咱们促膝长谈了9天,想想就幸福，嘿嘿嘿ヾ(✿ﾟ▽ﾟ)ノ']
// 逻辑变量
let imgArr = []
const date = dayjs("2022-07-19 21:29:00");
let ss = ref(0),
  mm = ref(0),
  hh = ref(0),
  dd = ref(0),
  yy = ref(0);
let s = ref(0),
  m = ref(0),
  h = ref(0),
  d = ref(0),
  y = ref(0);

for(let i = 1; i < 10; i++){
  imgArr.push(require(`./asset/back (${i}).jpg`))
}

let computeTime = () => {
  let now = dayjs();
  yy.value = now.diff(date, "year");
  now = now.subtract(yy.value, "year");
  dd.value = now.diff(date, "day");
  now = now.subtract(dd.value, "day");
  hh.value = now.diff(date, "hour");
  now = now.subtract(hh.value, "hour");
  mm.value = now.diff(date, "minute");
  now = now.subtract(mm.value, "minute");
  ss.value = now.diff(date, "second");
};
let computeAllTime = () => {
  let now = dayjs();
  y.value = now.diff(date, "year", true).toFixed(2);
  d.value = now.diff(date, "day", true).toFixed(2);
  h.value = now.diff(date, "hour");
  m.value = now.diff(date, "minute");
  s.value = now.diff(date, "second");
};

computeTime();
computeAllTime();
const timer = setInterval(() => {
  computeTime();
  computeAllTime();
}, 1000);

</script>

<style lang="less">
.back_wrap{
  width: 46vh;
  height: 100vh;
  position: absolute;
  top: 0;
  z-index: -1;
}
.text {
  min-width: 100vw;
  height: 100vh;
  box-sizing: border-box;
  padding: 20px;
  background: rgba(255, 255, 255, 0.7);
  font-weight: 600;
}
.btn{
  width: 100%;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  bottom: 10vh;
  --delay:13s;
  .memorizeBtn{
    width: 200px;
    height: 60px;
    font-size: 13px;
    text-align: center;
    line-height: 60px;
    color: white;
    background-image: linear-gradient(135deg, var(--theme-color2), var(--theme-color1));
    border-radius: 5px;
  }
}
div.animated{
  animation-delay: var(--delay,0s);
} 
.first_wrap {
  position: relative;
  .back_wrap{
    right: 0;
    background: url('./asset/back (1).jpg');
    background-size: 100% 100%;
  }
  .text {
    color: var(--theme-color1);
  }
  .positionWrap{
    position: relative;
    span{
      position: absolute;
    }
  }
}
.second_wrap{
  position: relative;
  .back_wrap{
    left  : 0;
    background: url('./asset/back (2).jpg');
    background-size: 100% 100%;
  }
  .text {
    text-align: right;
    color: var(--theme-color2);
    background: rgba(255, 255, 255, 0.2);
  }
}
.thrid_wrap{
  position: relative;
  .transparent{
    transition: all 2s ease;
    transform: rotateY(180);
  }
  .back_wrap-left{
    position: absolute;
    left : 0;
    z-index: 1;
    transform:scaleY(.9);
    opacity: .5;
  }
  .back_wrap{
    left : calc((100vw - 46vh) / 2);
    right : calc((100vw - 46vh) / 2);
    z-index: 2;
    box-shadow: 0 8px 16px var(--theme-color1);
    opacity: 1;
  }
  .back_wrap-right{
    position: absolute;
    right : 0;
    z-index: 1;
    transform:scaleY(.9);
    opacity: .5;
  }
  .none{
    display: none;
  }
  img{
    width: 46vh;
    height: 100vh;
  }
  .change-box{
    position: absolute;
    height: 30px;
    width: 30px;
    opacity: .7;
    top: 40vh;
    z-index: 3;
    font-weight: 800;
    .iconfont{
      font-size: 20px !important;
    } 
  }
  .message{
    text-align: center;
    position: inherit;
    top: 10px;
    width: 46vh;
    border-radius: 8px;
    background: white;
    opacity: .9;
  }
  .memorizeBtn{
    position: inherit;
    bottom: 30px;
  }
  .text0 {
    color: var(--theme-color2);
  }
  .text1 {
    color: var(--theme-color1);
  }
}
.fort_wrap{
  width: 100vw;
  height: 100vh;
  background: url('./asset/img.jpg');
  background-size: 100vw 100vw;
  background-repeat: no-repeat;
  background-position-y: 50%;
}
</style>
