<template>
  <div>
    <el-form ref="form" :model="formData" label-width="80px">
      <el-form-item label="种类名称">
        <el-input v-model="formData.type"></el-input>
      </el-form-item>
    </el-form>
    <el-button type="primary" round @click="getTableData">查找</el-button>

    <div style="padding:10px">
        <h2>库存详情</h2>
        <el-button type="success" @click="add" style="float: left;margin: 0 0 10px 0;">添加种类</el-button>
        <el-table :data="tableData" style="width: 100%" border>
            <el-table-column prop="type" label="种类名称"> </el-table-column>
            <el-table-column prop="num" label="剩余数量"> </el-table-column>
            <el-table-column label="库存提示">
                <template slot-scope="scope">
                    <div style="color:red" v-if="scope.row.num <= 30">不足</div>
                    <div style="color:orange" v-if="scope.row.num > 30&&scope.row.num <= 50">马上不足</div>
                    <div style="color:green" v-if="scope.row.num > 50">充足</div>
                </template>
            </el-table-column>
            <el-table-column label="库存提示">
                <template slot-scope="scope">
                     <el-button type="primary" icon="el-icon-edit" circle @click="edit(scope.row)"></el-button>
                     <el-button type="danger" icon="el-icon-delete" circle @click="deleteData(scope.row)"></el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
    <edit ref="edit" :show='editShow' :kindItem=kindItem :dialogTitle="dialogTitle" :ADDTEXT='ADDTEXT' :EDITTEXT='EDITTEXT' @closeDialog='closeDialog'></edit>
  </div>
</template>

<script>
import { search,deleteData } from "@/api/api";
import edit from "./edit&add"

export default {
  components:{
    edit
  },  
  data() {
    return {
      ADDTEXT : "新增", //新增页面标题
      EDITTEXT : "编辑",
      tableData: [],    //表格数据
      formData: {},     //表单元素
      editShow:false,   //显隐弹窗
      kindItem:{},      //编辑种类
      dialogTitle:this.ADDTEXT//弹窗标题
    };
  },
  created() {
    this.getTableData();
  },
  methods: {
    async getTableData() {
      if(this.formData.length){
          this.formData.type = ''
      }
      let res = await search(this.formData);
      this.tableData = res.data
    },
    edit(data){
      this.editShow = true
      this.$refs.edit.formData = {
        type:data.type?data.type:'',
        beforeNum:data.num?data.num:'',
      }
      this.kindItem = data
      this.dialogTitle = this.EDITTEXT
    },
    add(){
      this.editShow = true
      this.kindItem = {}
      this.dialogTitle = this.ADDTEXT
    },
    async deleteData(data){
      let res = await deleteData(data)
      if(res.data !== 'fail'){
        this.$message({
            message: '删除成功',
            type: 'success'
        });
        this.getTableData()
      }else{
        this.$message({
            message: '删除失败',
            type: 'error'
        });
      }
    },
    closeDialog(flag){
      this.editShow = false
      if(flag){
        this.getTableData()
      }
    }
  },
};
</script>