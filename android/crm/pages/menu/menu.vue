<template>
	<view class="content">
		<uni-nav-bar left-icon="back" left-text="·µ»Ø" title="²Ëµ¥" @clickLeft='clickLeft'></uni-nav-bar>
		<view class="locale-item" @click="gotoMap">
			<text class="text">{{$t('map')}}</text>
		</view>
		<view class="locale-item" v-for="(item, index) in locales" :key="index" @click="onLocaleChange(item)">
			<text class="text">{{item.text}}</text>
			<text class="icon-check" v-if="item.code == applicationLocale"></text>
		</view>
		<button type="default" @click="loginOut">{{$t('loginOut')}}</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				applicationLocale:''
			}
		},
		mounted(){
			this.applicationLocale = uni.getLocale();
		},
		computed:{
		  locales() {
		    return [{
		        text: this.$t('locale.auto'),
		        code: 'auto'
		      }, {
		        text: this.$t('locale.en'),
		        code: 'en'
		      },
		      {
		        text: this.$t('locale.zh-hans'),
		        code: 'zh-Hans'
		      }
		    ]
		  }
		},
		methods: {
			onLocaleChange(e) {
			  if (this.isAndroid) {
			    uni.showModal({
			      content: this.$t('index.language-change-confirm'),
			      success: (res) => {
			        if (res.confirm) {
					  this.applicationLocale = e.code
			          uni.setLocale(e.code);
			        }
			      }
			    })
			  } else {
				this.applicationLocale = e.code
			    uni.setLocale(e.code);
			    this.$i18n.locale = e.code;
			  }
			},
			loginOut(){
				uni.removeStorageSync('backendToken')
				uni.navigateTo({
				    url: '/pages/index/index'
				});
			},
			clickLeft(){
				uni.navigateBack()
			},
			gotoMap(){
				uni.navigateTo({
				    url: '/pages/map/map'
				});
			},
		}
	}
</script>

<style scoped lang="scss">
.locale-item {
  display: flex;
  flex-direction: row;
  padding: 10px 0;
}

.locale-item .text {
  flex: 1;
}

.icon-check {
  margin-right: 5px;
  border: 2px solid #007aff;
  border-left: 0;
  border-top: 0;
  height: 12px;
  width: 6px;
  transform-origin: center;
  transform: rotate(45deg);
}
</style>
