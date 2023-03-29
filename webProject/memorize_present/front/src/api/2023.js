import axios from "axios";
import { BASE_URL } from "../../const.js";

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
