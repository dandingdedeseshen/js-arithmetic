import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:5000'
// const BASE_URL = 'http://43.143.165.98:5000'

function login(data){
  return axios({
    url:BASE_URL + '/login',
    data:JSON.stringify(data),
    method:'POST',
  })
}

function uploadFile(data){
  return axios({
    url:BASE_URL + '/saveFile',
    data:data,
    method:'POST',
  })
}

export {
  login,
  uploadFile
}