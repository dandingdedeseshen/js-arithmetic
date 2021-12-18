import axios from 'axios'

function search(data){
    return axios({
        url:'http://127.0.0.1:5000/search',
        data:JSON.stringify(data),
        method:'POST',
    })
}

function edit(data){
    return axios({
        url:'http://127.0.0.1:5000/update',
        data:JSON.stringify(data),
        method:'POST',
    })
}
function deleteData(data){
    return axios({
        url:'http://127.0.0.1:5000/delete',
        data:JSON.stringify(data),
        method:'POST',
    })
}

export {
    search,
    edit,
    deleteData
}