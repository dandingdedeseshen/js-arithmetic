<template>
  <div id="fileItem_2023" @click="getFileRes">
    <span :class="['iconfont', fileIco(devName)]" />
    <p class="text">{{ fileName }}</p>
  </div>
</template>

<script setup>
import  api  from "@/api/index";
let { getFile } = api

let prop = defineProps({
  fileName: {
    type: String,
    default: "xxx.jpg",
  },
});

// 根据问价类型获取文件图标
const fileIco = (type) => {
  switch(type){
    case 'jpg':
    case 'png':
    case 'webp':
    case 'bmp':
    case 'gif':
    case 'jpeg':
      return 'icon-tupian'
    case 'rar':
    case 'zip':
    case 'jar':
      return 'icon-yasuobao'
    default:
      return 'icon-wenjianjia'
  }
}

let devName = prop.fileName.match(/[a-z]+$/g) ? prop.fileName.match(/[a-z]+$/g)[0].toLowerCase() : ''

const getFileRes = async () => {
  let res = await getFile({fileName : prop.fileName})
  const url = window.URL.createObjectURL(res)
  const link = document.createElement('a')
  link.style.display = 'none'
  link.href = url
  link.setAttribute('download', prop.fileName)
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}
</script>

<style lang="less">
#fileItem_2023 {
  width: 80px;
  display: inline-block;
  border-radius: 10px;
  padding: 0 10px;
  margin-top: 10px;
  margin-left: 10px;
  border-right: 1px solid rgba(128, 128, 128, 0.327);
  border-bottom: 1px solid rgba(128, 128, 128, 0.327);
  .iconfont{
    display: inline-block;
    font-size: 60px;
    margin: 10px 10px 0 10px;
  }
  .text{
    font-size: 12px;
    width: 100%;
    text-align: center;
    padding-bottom: 10px;
    word-break: break-all;
  }
}
</style>
