<template>
  <div class="loginWrap">
    <div class="card">
      <el-input v-model="userName" />
      <el-input v-model="password" />
      <el-button @click="loginEvent">登录</el-button>
    </div>
  </div>
</template>

<script>
import { login } from "@/api/index";
export default {
  data(){
    return ({
      userName : '',
      password : ''
    })
  },
  methods:{
    async loginEvent(){
      let data = {
        userName:this.userName
      }
      let res = await login(data)
      console.log(res.data)
    }
  }
}
</script>

<style lang="less">
.loginWrap{
  background: linear-gradient(to right; var(--theme-color1) 0%, var(--theme-color2) 70%);
  height: 60vh;
  width: 100vw;
  padding-top: 40vh;
  .card{
    height: 150px;
    display: flex;
    justify-content: center;
    align-content: space-between;
    flex-wrap: wrap;
    padding: 10px;
    margin: 0 30vw;
    backdrop-filter: blur(100px);
    border-radius: 5px;
  }
}
  
</style>