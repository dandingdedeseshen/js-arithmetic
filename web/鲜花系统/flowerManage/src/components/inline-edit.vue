<template>
    <div class="table-Wrap" id="inline-edit">
        <el-table :data="tableListCopy" header-row-class-name="table-header-row" row-class-name="table-row-color" id="break-normal" class="inline-table">
            <!-- 自定义列 -->
            <slot name="columBefore"></slot>
            <el-table-column v-for="(option,index) in tableProps" :key="index" :prop="option.prop" :label="option.name" :width="option.width||'auto'">
                <template slot-scope="scope">
                    <b v-show="scope.row.isEditing&&option.isRequire" style="color:red">*</b>
                    <!-- 编辑状态 v-if控制种类 v-show控制显隐彼此独立-->
                    <!-- 时间选择 -->
                    <el-date-picker :disabled='option.disabled' v-model="scope.row[option.editStr]" v-if="option.type == 'date'" v-show="scope.row.isEditing" type="date" class="inputWrap"
                    value-format="yyyy-MM-dd" @change="change(scope.row,option)"/>
                    <!-- 下拉框 -->
                    <el-select :disabled='option.disabled' v-model="scope.row[option.editStr]" v-else-if="option.type == 'selected'" v-show="scope.row.isEditing"  class="inputWrap"
                    @change="selectChange(scope.row,option,scope.row[option.editStr])">
                        <el-option v-for="(item,index) in option.options" :key="index" :label="item.label" :value="item.value"></el-option>
                    </el-select>
                    <!-- 文本域 -->
                    <el-input :disabled='option.disabled' v-model="scope.row[option.editStr]"  v-else-if="option.type == 'textarea'" v-show="scope.row.isEditing" type="textarea"
                    :rows="2" @change="change(scope.row,option)" class="inputWrap"/>
                    <!-- 输入框 -->
                    <el-input :disabled='option.disabled' v-model="scope.row[option.editStr]" v-else v-show="scope.row.isEditing" type="text"
                    @change="change(scope.row,option)" class="inputWrap"/>
                    <!-- 显示状态 -->
                    <span v-show="!scope.row.isEditing" v-html="scope.row[option.viewStr]"></span>
                </template>
            </el-table-column>
            <!-- 自定义列 -->
            <slot name="columAfter"></slot>
            <slot name="operate">
                <el-table-column label="Operate">
                    <template slot-scope="scope">
                        <div v-show="!scope.row.isEditing">
                            <i class="el-icon-edit-outline pointer" :disabled='isview' @click="doEdit(scope.row)"/>
                            <span class="delete"><i class="el-icon-delete pointer" :disabled='isview' @click="doDelete(scope.$index)"/></span>
                        </div>
                        <div v-show="scope.row.isEditing">
                            <i class="iconfont icon-baocun pointer" :disabled='isview' @click="doSave(scope.row,scope.$index)"/>
                            <i class="iconfont icon-cancelRequest pointer" :disabled='isview' @click="doCancel(scope.$index,scope.row)"/>
                        </div>
                    </template>
                </el-table-column>
            </slot>
        </el-table>
        <el-button @click="doAdd" v-if="showAdd" class="float-right" style="margin-top:10px" :disabled='isview'>
            {{$t('common.add')}}
        </el-button>
        <div style="clear:both"></div>
    </div>
</template>

<script>
import {formateDateUS,formateDateCN} from 'utils/main.js'

export default{
    created() {
        this.tableListCopy = JSON.parse(JSON.stringify(this.tableList))
    },
    data(){
        return{
            // 正在编辑状态
            isEditing:false,
            // 正在编辑状态的数据(编辑之前的值)
            isEditingObj:{},
            // 列表数据
            tableListCopy:[],
        }
    },
    props:{
        // 对象数组，设置每一列的属性
        tableProps:{
            // [{
            //     name:'', 该列表头的名称
            //     [type]:'text', 该列编辑状态中表单的格式        非必须默认取text
            //     editStr:'', 该列编辑状态中展示的值
            //     viewStr:'', 该列查看状态中展示的值
            //     [options]:'', 该列下拉框的数据
            //     [change]:'', 该列编辑状态的表单的数据改变事件 参数:row该列数据，that组件中的this,obj选中的对象
            //     [isRequire]:'',该字段是否必填
            //     [disabled]:'',该字段是否必填
            // }],
            default:[],
            type:Array
        },
        // 对象数组,列表数据
        tableList:{
            default:[],
            type:Array
        },
        // 对象数组,列表数据
        showAdd:{
            default:true,
            type:Boolean
        },
        // 是否是查看状态
        isview:{
            default:false,
            type:Boolean
        },
        // 默认值
        defaultObj:{
            default:() => ({}),
            type:Object
        },
        // 保存之前的校验功能，返回false为禁止保存
        saveCheck:{
            default:() => {return true},
            type:Function
        }
    },
    methods:{
        // 下拉组件数据更改时默认执行的事件
        selectChange(row,option,value){
            let obj = option.options.find((item)=>{
                return item.value === row[option.editStr];
            });
            this.$set(row,option.viewStr,obj?obj.label:'')
            if(option.change){
                option.change(row,this,obj)
            }
        },
        change(row,option){
            if(option.type == 'date'){
                row[option.viewStr] = formateDateUS(row[option.editStr])
            }
            if(option.change){
                option.change(row,this)
            }
        },
        // 添加数据
        doAdd(){
            if(this.isEditing){
                this.$message.error(this.$t('common.isEditIng'))
                return
            }
            let obj = {...this.defaultObj}||{}
            obj.isEditing = true
            this.$set(this.tableListCopy,this.tableListCopy.length,obj)
            this.isEditing = true
            this.isEditingObj = 'new Data'
        },
        // 编辑事件
        doEdit(e){
            if(this.isview){
                return
            }
            if(this.isEditing){
                this.$message.error(this.$t('common.isEditIng'))
                return
            }
            this.isEditing = true
            this.$set(e,'isEditing',true)
            this.isEditingObj = {...e}
        },
        // 删除事件
        doDelete(e){
            if(this.isview){
                return
            }
            this.tableListCopy.splice(e,1)
        },
        // 保存事件
        doSave(e,index){
            // 必填校验
            for(let item of this.tableProps){
                if(item.isRequire&&!e[item.editStr]){
                    this.$message.error(item.name + " " + this.$t('common.require'))
                    return
                }
            }
            // 自定义保存校验
            if(!this.saveCheck(e,index,this.tableListCopy)){
                return
            }
            if(JSON.stringify({...this.defaultObj}) !== '{}'){
                let obj = this.tableListCopy.find((item) => { return item.isEditing})
                for(let item of this.tableProps){
                    if(item.type === 'selected'){
                        this.selectChange(obj,item)
                    }
                }
            }
            this.$set(e,'isEditing',false)
            this.isEditing = false
            this.isEditingObj = {}
        },
        // 取消事件
        doCancel(index){
            if(this.isEditingObj === 'new Data'){
                this.tableListCopy.splice(this.tableListCopy.length - 1,1)
            }else{
                this.isEditingObj.isEditing = false
                this.$set(this.tableListCopy,index,this.isEditingObj)
            }
            this.isEditing = false
            this.isEditingObj = {}
        },
    },
    watch:{
        tableList:{
            handler(val){
                this.tableListCopy = JSON.parse(JSON.stringify(val))
            },
            deep:true
        },
    }
}
</script>

<style>
.inline-table .inputWrap{
    width: 90% !important;
}
#inline-edit .el-table td, 
#inline-edit .el-table th,
#inline-edit .el-table__header thead tr th{
    padding: 6px;
}

</style>
