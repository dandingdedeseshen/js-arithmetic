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
    method: "POST",
  });
}

function findFile(data, extraData) {
  return axios({
    url: BASE_URL + "/findFile",
    data: data || {},
    method: "POST",
    extraData: extraData
  });
}

export default { login, uploadFile, findFile };
