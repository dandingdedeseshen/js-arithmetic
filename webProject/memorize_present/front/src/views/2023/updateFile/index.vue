<template>
  <div id="updateFile_2023">
    <FileItem v-for="item of fileList" :key="item.id" :fileName='item.File_name' />
    <div class="upload_wrap" @click="uploadEvent">
      <p>+</p>
      <input type="file" id="file" @change="upload">
    </div>
  </div>
</template>

<script setup>
import api from "@/api/index";
import { FileItem } from "../components/index";
import { ref } from 'vue'

let { uploadFile, findFile } = api;
let fileList = ref([])

const upload = async (e) => {
  let file = e.target.files[0];
  let data = new FormData();
  data.append("file", file);
  await uploadFile(data);
  getFileList();
};

const getFileList = async (e) => {
  let res = await findFile({a:1}, {b:2});
  fileList.value = res
};

const uploadEvent = () => {
  document.getElementById('file').click()
}

getFileList();
</script>

<style lang="less">
#updateFile_2023 {
  padding: 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  .upload_wrap{
    display: inline-block;
    border: 1px solid rgba(128, 128, 128, 0.327);
    margin-top: 10px;
    margin-left: 10px;
    width: 100px;
    border-radius: 10px;
    p{
      font-size: 50px;
      line-height: 90px;
      text-align: center;
    }
    input{
      display: none;
    }
  }
  
}
</style>
