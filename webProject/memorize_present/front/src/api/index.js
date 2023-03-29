import axios from "axios";
import api_2023 from "./2023.js";
import { ElMessageBox } from 'element-plus'

// 添加请求拦截器
axios.interceptors.request.use(
  function (config) {
    // 在发送请求之前做些什么
    let user = JSON.parse(localStorage.getItem('userData'))
    let flag = config.extraData ? !config.extraData.noUser : true
    if(user && user.User_name && flag ){
      config.data = JSON.parse(config.data)
      config.data.user = {
        userName : user.User_name,
        identity : user.Is_baby == 1
      }
      config.data = JSON.stringify(config.data)
    }
    return config;
  },
  function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

// 添加响应拦截器
axios.interceptors.response.use(
  function (response) {
    // 对响应数据做点什么
    if(response.config.extraData){
      // 携带了额外的数据之后做点什么
    }
    return response.data;
  },
  function (error) {
    // 对响应错误做点什么
    ElMessageBox.alert(error.response.data.result, '出错了')
    return Promise.reject(error);
  }
);

export default { ...api_2023 };
