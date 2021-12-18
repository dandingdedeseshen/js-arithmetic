<template>
  <el-dialog
    width="30%"
    :title="dialogTitle"
    :visible.sync="show"
    :before-close="handleClose"
  >
    <div>
      <el-form ref="form" :model="formData" label-width="80px">
        <el-form-item label="种类名称">
          <el-input
            v-model="formData.type"
            :disabled="dialogTitle == EDITTEXT"
          ></el-input>
        </el-form-item>

        <el-form-item label="原有数量" v-show="dialogTitle == EDITTEXT">
          <el-input v-model="formData.beforeNum" disabled>
          </el-input>
        </el-form-item>

        <el-form-item label="增加/减少" v-show="dialogTitle == EDITTEXT">
          <el-select v-model="formData.isAdd" placeholder="请选择" style="width:100%">
            <el-option
              label="增加"
              value=true
            >
            </el-option>
            <el-option
              label="减少"
              value=false
            >
            </el-option>
          </el-select>
        </el-form-item>

        <el-form-item :label="dialogTitle == ADDTEXT?'数量':'变化数量'">
          <el-input v-model="formData.changeNum"></el-input>
        </el-form-item>
      </el-form>
    </div>

    <span slot="footer" class="dialog-footer">
      <el-button @click="handleClose">取 消</el-button>
      <el-button type="primary" @click="submit">确 定</el-button>
    </span>
  </el-dialog>
</template>

<script>
import { edit } from "@/api/api";

export default {
  data() {
    return {
      formData: {}, //表单数据
    };
  },
  props: {
    show: Boolean,
    kindItem: Object,
    dialogTitle: String,
    EDITTEXT:String,
    ADDTEXT:String,
  },
  methods: {
    handleClose(flag) {
      this.formData = {}
      this.$emit("closeDialog",flag);
    },
    async submit() {
        this.formData.id = this.kindItem.id?this.kindItem.id:''
        let beforeNum = parseInt(this.formData.beforeNum)
        let changeNum = parseInt(this.formData.changeNum)
        if(this.dialogTitle == '编辑'){
            this.formData.num = this.formData.isAdd === 'true'?(beforeNum + changeNum):(beforeNum - changeNum)
        }else{
            this.formData.num = this.formData.changeNum
        }
        let res = await edit(this.formData)
        if(res.data !== 'fail'){
            this.$message({
                message: '添加成功',
                type: 'success'
            });
            this.handleClose(true)
        }else{
            this.$message({
                message: '添加失败',
                type: 'error'
            });
        }
    },
  },
};
</script>