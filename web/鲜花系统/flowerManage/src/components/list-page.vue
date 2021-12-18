<template>
    <div id="list-page" class="table-Wrap" v-loading='listLoading'>
        <header id="serachWrap">
            <h4>{{title}}</h4>
            <slot name="header">
                <span class="searchBy">{{$t('common.searchBy')}} &nbsp;&nbsp;</span>
                <el-input v-model="inputText" :placeholder="$t('common.placeholder')" class="serachInput"></el-input>
                <el-button @click="searchEvent">{{$t('common.go')}}</el-button>
            </slot>
            <slot name="btnGroup"></slot>
        </header>
        <slot name="status" class="statusWrap"></slot>
        <main class="padding-top-10">
            <el-table :data="tableList" header-row-class-name="table-header-row" row-class-name="table-row-color" id="break-normal"
                @sort-change="sortChange" @selection-change="handleSelectionChange" ref="listTable">
                <slot name="columBefore"></slot>
                <el-table-column v-for="(item,index) in tableProps" :key="index" :prop="item.prop" :label="item.name" :sortable='item.custom' :width="item.width"/>
                <slot name="columAfter"></slot>
                <slot name="operate">
                    <el-table-column :label="$t('common.operation')" width="100">
                        <template slot-scope="scope">
                            <div class="operate">
                                <i class="el-icon-delete pointer" @click="doDelete(scope.row)"></i>
                                <i class="el-icon-edit-outline pointer" @click="doEdit(scope.row)"></i>
                                <i class="el-icon-view pointer" @click="doView(scope.row)"></i>
                                <!-- <el-button type="info" size="mini" @click="doView(scope.row)">{{$t('common.view')}}</el-button>
                                <el-button type="primary" size="mini" @click="doEdit(scope.row)">{{$t('common.edit')}}</el-button>
                                <el-button type="danger" size="mini" @click="doDelete(scope.row)">{{$t('common.del')}}</el-button> -->
                            </div>
                        </template>
                    </el-table-column>
                </slot>
            </el-table>
        </main>
        <footer>
            <!-- layout="prev, pager, next, jumper,sizes,total" -->
            <el-pagination
            layout="prev, pager, next, jumper"
            background
            style="float:left;margin:10px 0 0 -11px;"
            :page-sizes="[10, 20, 50, 100, 500, 2000]"
            :current-page="pageData.pageNumber"
            :page-size="pageData.pageSize"
            :total="pageData.totalCount"
            @current-change="handleCurrentChange">
            </el-pagination>
        </footer>
    </div>
</template>

<script>
import {postLcsp} from 'api/commonApi'

export default{
    data(){
        return{
            // 分页数据
            pageData:{
                pageNumber:1,//当前页数
                pageSize:10,
                totalCount:0
            },
            // 输入框数据
            inputText:'',
            // 列表数据
            tableList:[],
            // 列表中选择的数据
            selecArr:[],
            // 查询条件的额外参数
            extraParm:{},
            // 加载动画
            listLoading:false,
            // 排序方式
            sortBy:'',
            // 排序字段
            sortOrder:'',
        }
    },
    created() {
        this.getData()
    },
    props:{
        // 对象数组，设置每一列的属性
        tableProps:{
            // [{
            //     prop:'callOffNo',  该列对应的字段名称
            //     name:this.$t('callOffNotes.callOffNumber'), 该列表头的名称
            //     custom:'custom', 该列是否需要排序
            //     width:'100px', 该列是否需要排序
            // }],
            default:[],
            type:Array
        },
        // 请求地址
        url:{
            default:'',
            type:String
        },
        //普通查询的关键字
        searchCode:{
            default:'',
            type:String
        },
        // 页面名
        title:{
            default:'',
            type:String
        },
        // 额外携带的参数与组件中的extraParm不同的是这个额外携带的参数是所有查询都会带并且会覆盖其他同名属性的数据
        extraData:{
            default:() => ({}),
            type:Object
        },
        // 处理接口返回数据的函数
        setList:{
            default:() => {},
            type:Function
        },
    },
    methods:{
        // 更改分页
        handleCurrentChange(e){
            this.pageData.pageNumber = e
            this.getData()
        },
        // 搜索事件
        searchEvent(){
            this.getData()
        },
        // 调用接口获取数据
        async getData(extraParm,sortBy,sortOrder){
            let data = {
                [this.searchCode]: typeof(this.inputText) === 'string'?this.inputText.trim():this.inputText,
                page: {SortBy: "", SortOrder: "", pageIndex: 0, pageSize: "11"},
                searchType: 0,
            }
            this.sortBy = sortBy||this.sortBy
            this.sortOrder = sortOrder||this.sortOrder
            data.page.pageSize = this.pageData.pageSize
            data.page.pageIndex = this.pageData.pageNumber - 1
            data.page.SortBy = this.sortBy
            data.page.SortOrder = this.sortOrder
            if(extraParm){
                this.extraParm = {...extraParm}
                for(let item in extraParm){
                    let str = typeof(extraParm[item]) === 'string'?extraParm[item].trim():extraParm[item]
                    data[item] = str
                }
            }
            if(this.extraData){
                for(let item in this.extraData){
                    let str = typeof(this.extraData[item]) === 'string'?this.extraData[item].trim():this.extraData[item]
                    data[item] = str
                }
            }
            this.listLoading = true
            let res = await postLcsp(data,this.url)
            if(!res){
                this.$message.error(this.$t('common.getFail'));
                return
            }
            this.listLoading = false
            if(res.totalCount === undefined){   //拦截一下错误的返回结果防止报错
                this.setPage('')
                this.tableList = []
                this.$message.error(this.$t('common.getFail'))
                return
            }
            if(res.totalCount === 0){
                this.setPage('')
                this.tableList = []
                this.$message.warning(this.$t('common.noData'))
                return
            }
            this.setPage(res)
            this.tableList = res.list
            this.setList(this.tableList)
        },
        // 排序
        async sortChange(e){
            let sortOrder = (e.order == "ascending")?'asc':'desc'
            this.getData(this.extraParm,e.prop,sortOrder)
        },
        // 设置分页信息
        setPage(res){
            this.pageData.pageNumber = (res.pageIndex + 1)||1
            this.pageData.pageSize = res.pageSize || 10
            this.pageData.totalCount = res.totalCount || 0
        },
        // 选择数据时触发
        handleSelectionChange(arr){
            this.selecArr = arr
        },
        // 查看
        doView(row){
            this.$emit('operate','view',row)
        },
        // 编辑
        doEdit(row){
            this.$emit('operate','edit',row)
        },
        // 删除
        doDelete(row){
            this.$emit('operate','del',row)
        }
    },
}
</script>

<style scoped>
#serachWrap{
    padding-top:5px;
    height: 45px;
    border-bottom: 1px solid #DFDFDF;
    text-align: right;
}
#serachWrap>h4{
    color: #0073cc;
    float: left;
    line-height: 40px;
    font-size: 20px;
}
#serachWrap>.searchBy{
    font-size: 14px;
    color: #0073cc;
}
.serachInput{
    width: 15%;
}
.operate>i{
    font-size: 15px;
    font-weight: bold;
    color: #0073cc;
}
</style>

<style>
#list-page tbody td,
#list-page thead th{
    padding: 0;
    height: 30px !important;
}
#list-page tbody tr:hover>td:nth-last-of-type(1) i,
#list-page tbody tr:hover>td:nth-of-type(1){
    color: red !important;
}
#list-page .cell{
    padding: 6px 0;
}
</style>
