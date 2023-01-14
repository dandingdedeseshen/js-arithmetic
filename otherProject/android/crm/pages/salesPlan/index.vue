<template>
	<view>
		<uni-nav-bar right-text="菜单" title="客户计划" @clickRight='clickRight'></uni-nav-bar>
		<view class="searchWrap padding-middle">
			<uni-combox :candidates="communicationTypeOption" placeholder="请选择沟通方式" v-model="communicationType" class="serchDiv"/>
			<uni-datetime-picker type="date" v-model="startTime" class="serchDiv"/>
			<uni-datetime-picker type="date" v-model="endTime" class="serchDiv"/>
			<button type="primary" @click="searchEvent">Search</button>
		</view>
		<view class="tableWrap padding-middle">
			<uni-table border stripe emptyText="暂无更多数据" >
				<!-- 表头行 -->
				<uni-tr>
					<uni-th align="left" width="100">{{$t('salesPaln.customer')}}</uni-th>
					<uni-th align="left">{{$t('salesPaln.communicationType')}}</uni-th>
					<uni-th align="left">{{$t('salesPaln.isNeedSupport')}}</uni-th>
					<uni-th align="left">{{$t('salesPaln.planTime')}}</uni-th>
					<uni-th align="left">{{$t('salesPaln.op')}}</uni-th>
				</uni-tr>
				<!-- 表格数据行 -->
				<uni-tr v-for="item in tableData" :key = 'item.id'>
					<uni-th align="center">{{item.customerName}}</uni-th>
					<uni-th align="center">{{item.communicationTypeName}}</uni-th>
					<uni-th align="center">{{item.isNeedSupport?'是':'否'}}</uni-th>
					<uni-th align="center">{{item.planTime.split(' ')[0]}}</uni-th>
					<uni-th align="center">无权限</uni-th>
				</uni-tr>
			</uni-table>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			tableData:[],
			communicationType:'',
			startTime:'',
			endTime:'',
			communicationTypeOption:[],
			communicationTypeArr:[]
		}
	},
	mounted(){
		this.getOption()
		this.searchEvent()
	},
	onLoad() {
	},
	methods: {
		async getOption(){
			let res = await this.$request.get(this.$request.url.selectOption.getCommunicationTypeList,null)
			this.communicationTypeArr = res.data.list
			this.communicationTypeOption = res.data.list.map((item) => {return item.name})
		},
		async searchEvent(){
			let communicationTypeId = this.communicationTypeArr.find((item) => {return item.name === this.communicationType})
			communicationTypeId = communicationTypeId?communicationTypeId.id:''
			let data = {
				customerName: '',
				customerShortName: '',
				communicationType: communicationTypeId,
				businessUser: '',
				isNeedSupport: '',
				startTime: this.startTime,
				endTime: this.endTime,
				pageSize: 10,
				currentPage: 1,
			}
			let res = await this.$request.get(this.$request.url.salesPlan.getCrmSalesPlanForPage,data)
			if(res.data.list){
				this.tableData = res.data.list
			}else{
				
			}
		},
		clickRight(){
			uni.navigateTo({
			    url: '/pages/menu/menu',
				animationType: 'pop-in',
				animationDuration: 2000
			});
		}
	}
}
</script>

<style scoped lang="scss">
.serchDiv{
	margin-bottom: 10rpx;
}
</style>
