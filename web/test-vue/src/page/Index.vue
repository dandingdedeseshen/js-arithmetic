<template>
    <div id="box">
        <Page1/>
    </div>
</template>

<script>
import Page1 from '@/components/Page1'
export default {
    components:{
        Page1
    }
}
</script>

<style>
    *{
        margin: 0;
        padding: 0;
    }
    #box{
        padding-top: 80px;
        margin: auto;
        width: 650px;
        height: 285px;
        background-color: tomato;
    }
</style>