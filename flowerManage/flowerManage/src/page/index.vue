<template>
    <div>
        <el-button type="primary" plain @click="goto('/warehouse')">仓储管理</el-button>
    </div>
</template>

<script>
export default {
    methods: {
        goto(url){
            this.$router.push({path: url})
        }
    }
}
</script>