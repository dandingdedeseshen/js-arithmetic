<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			// 如果登录了直接进入首页
			if(uni.getStorageSync('backendToken')){
				uni.navigateTo({
				    url: '/pages/salesPlan/index'
				});
			}
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
@import '@/common/index.css'
	/*每个页面公共css */
</style>
