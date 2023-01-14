<template>
	<view class="content hzl">
		<uni-popup ref="popup" type="dialog" :closeDuration="1000">
		    <uni-popup-message :type="message.type" :message="message.text" ></uni-popup-message>
		</uni-popup>
		<view class="pop">
			<text class="font text1">HELLO</text>
			<text class="font text2">{{$t('welcome')}}</text>
			<view class="loginPop">
				<input type="text" v-model="loginName" />
				<input type="password" v-model="passWord" />
				<button @click="logonEvent">Login</button>
			</view>
		</view>
	</view>
</template>

<script>
	import {encode64,Cookies} from "@/common/util.js"
	export default {
		data() {
			return {
				loginName:'',
				passWord:'',
				message:{
					type:'',
					text:''
				}
			}
		},
		onLoad() {

		},
		methods: {
			async logonEvent(){
				uni.navigateTo({
				    url: '/pages/salesPlan/index'
				});
				// let passWord = this.passWord?encode64(this.passWord):''
				// let res = await this.$request.noHeaderGet(this.$request.url.sys.login,{loginName:this.loginName,password:passWord})
				// res = res.data
				// if(res.message === "登录成功"){
				// 	this.message.type = 'success'
				// 	this.message.text = res.message
				// 	this.$refs.popup.open()
				// 	Cookies.set('crm-token',res['crm-token'],{ expires: 1 })
				// 	uni.setStorageSync('backendToken',res['crm-token'])
				// 	uni.navigateTo({
				// 	    url: '/pages/salesPlan/index'
				// 	});
				// }else{
				// 	this.message.type = 'error'
				// 	this.message.text = res.message  || 'error'
				// 	this.$refs.popup.open()
				// 	uni.removeStorageSync('backendToken')
				// }
			},
		}
	}
</script>

<style scoped lang="scss">
.content{
	box-sizing: border-box;
	width: 100vw;
	height: 100vh;
	background:url(@/static/sys/login.jpg) bottom no-repeat;
	background-size: cover;
	padding: 21vh 0 0 0;
	.pop{
		margin: 0 auto;
		width: 90%;
		background:url(@/static/sys/xc.png) bottom no-repeat;
		background-size: cover;
		box-sizing: border-box;
		padding: 20px 5%  5%;
		.text1{
			display: block;
			color: rgb(7, 129, 172);
			font-size: 60rpx;
		}
		.text2{
			display: block;
			font-size: 38rpx;
			margin-top: 30rpx;
			color: rgb(7, 129, 172);
		}
		.loginPop{
			margin: 20rpx auto;
			padding-top: 30rpx;
			padding-bottom: 50rpx;
			width: 100%;
			border-radius: 20rpx;
			background-color: $uni-bg-color;
			image{
				margin: 0 auto 30rpx auto;
				display: block;
				width: 366rpx;
				height: 104rpx;
			}
			input{
				margin: 20rpx auto;
				width: 90%;
			}
			button{
				width: 90%;
				height: 80rpx;
				line-height: 80rpx;
				background: linear-gradient(to left,#0b4aa7,#1ab3fa);
				color: $uni-bg-color;
				&::after{
					display: none;
				}
			}
		}
	}
}
</style>
