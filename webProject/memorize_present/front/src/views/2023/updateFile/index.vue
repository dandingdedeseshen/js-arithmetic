<template>
  <div>
    <input type="file" id="file" @change="getFile">
  </div>
</template>

<script setup>
import { uploadFile } from "@/api/index";

const  getFile = async (e) => {
  let file = e.target.files[0]
  let data = new FormData()
  data.append('file', file)
  let res = await uploadFile(data)
  console.log(res)
}
</script>

<style lang="less">
</style>