<template>
  <div v-show="!printing">
    <el-button @click="print">PrintPage</el-button>
  </div>
  <div v-show="printing">只想打印这个字符串！！</div>
</template>

<script>
export default {
  name: "printPage",
  data() {
    return {
      printing: false,
    };
  },
  methods: {
    print() {
      this.printing = true;
      this.$nextTick(() => {
        window.print();
      });
      let that = this;
      window.onafterprint = () => {
        //打印完成跳回原页面
        that.printing = false;
      };
    },
  },
};
</script>

<style lang="sass"></style>
