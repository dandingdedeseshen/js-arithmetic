<template>
  <div class="loginWrap">
    <div class="card">
      <el-input v-model="userName" clearable />
      <el-input v-model="password" type="password" clearable />
      <el-button @click="loginEvent">登录</el-button>
    </div>
  </div>
</template>
<script setup>
import { ElMessage } from 'element-plus'
import api from "@/api/index";
import { ref,getCurrentInstance } from 'vue'

let { login } = api
let { proxy } = getCurrentInstance()
let userName = ref('')
let password = ref('')

// 必填校验
const isVerify = () => {
  if(!userName.value){
    ElMessage({
      showClose: true,
      message: '请输入用户名!',
      type: 'error',
      'custom-class':'login-close'
    })
    return false
  }
  if(!password.value){
    ElMessage({
      showClose: true,
      message: '请输入密码!',
      type: 'error',
      'custom-class':'login-close'
    })
    return false
  }
  return true
}

// 登录成功
const loginSuccess = (data) => {
  // 登录信息存入localhost
  localStorage.setItem('userData',JSON.stringify(data))
  // 跳转页面
  proxy.router.push('/menu')
}

// 登录方法
const loginEvent = async () =>{
  if(!isVerify()){
    return
  }
  let data = {
    userName:userName.value,
    password:password.value
  }
  // TODO 加密传送
  let res = await login(data)
  res = res[0]
  if(res && res.Password == password.value){
    loginSuccess(res)
  }else{
    ElMessage({
      showClose: true,
      message: '用户名或密码错误!',
      type: 'error',
      'custom-class':'login-close'
    })
  }
}
</script>

<style lang="less">
.loginWrap{
  background-image: url('./back.jpg');
  background-size: cover;
  box-sizing: border-box;
  overflow: hidden;
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  .card{
    height: 150px;
    display: flex;
    justify-content: center;
    align-content: center;
    flex-wrap: wrap;
    padding: 10px;
    margin: 0 20vw;
    background: linear-gradient(to bottom; var(--theme-color3) 0%, var(--theme-color4) 70%);
    backdrop-filter: blur(5px);
    border-radius: 5px;
    &>div{
      margin-bottom: 12px;
    }
    &>button{
      width: 100%;
      background: linear-gradient(to left; var(--theme-color3) 0%, var(--theme-color4) 70%);
      color: white;
    }
  }
}
.login-close{
  width: 80vw;
}
</style>