import axios from "axios";
const BASE_URL = process.env.VUE_APP_BASE_URL

function login(data) {
  return axios({
    url: BASE_URL + "/login",
    data: JSON.stringify(data),
    method: "POST",
  });
}

function uploadFile(data) {
  return axios({
    url: BASE_URL + "/saveFile",
    data: data,
    extraData:{noUser:true},
    method: "POST",
  });
}

function findFile(data, extraData) {
  return axios({
    url: BASE_URL + "/findFile",
    data: JSON.stringify(data) || '{}',
    method: "POST",
  });
}

function getFile(data) {
  return axios({
    url: BASE_URL + "/getFile",
    data: JSON.stringify(data) || '{}',
    responseType:'blob',
    method: "POST",
  });
}



export default { login, uploadFile, findFile, getFile };
