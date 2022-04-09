import url from "./url.js"

const BASE_URL = ''

const request = {
	url,
	post(url,data){
		const TOKEN = uni.getStorageSync('backendToken')
		return Promise((resolve,reject) => {
			uni.request({
				url:BASE_URL + url,
				data,
				method:"POST",
				header:{
					Authorization: "Authorization-crm",
					'Authorization-crm':TOKEN
				},
				success(res){
					resolve(res)
				},
				fail(res){
					reject(res)
				}
			})
		})
	},
	get(url,data){
		const TOKEN = uni.getStorageSync('backendToken')
		return new Promise((resolve,reject) => {
			uni.request({
				url:BASE_URL + url,
				data,
				header:{
					Authorization: "Authorization-crm",
					'Authorization-crm':TOKEN
				},
				method:"GET",
				success(res){
					resolve(res)
				},
				fail(res){
					reject(res)
				}
			})
		})
	},
	noHeaderGet(url,data){
		return new Promise((resolve) => {
			uni.request({
				url:BASE_URL + url,
				data,
				method:"GET",
				success(res){
					resolve(res)
				}
			})
		})
	}
}

export default request

