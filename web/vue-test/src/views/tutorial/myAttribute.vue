<template>
    <!-- 自定义指令 -->
    <div id="myAttribute">
        <div v-a:data="num" @click="() => {num ++}">{{num}}</div>
        <el-button v-b @click="() => {num ++}">{{num}}</el-button>
        <div class="duplicateClass"></div>
        <div class="duplicateClass"></div>
    </div>
    <!-- Teleport -->
    <teleport to='el-button'>
        <div class="teleportWrap">teleport</div>
    </teleport>
</template>

<script>
export default {
    name:'myAttribute',
    data(){
        return{
            num:0,
        }
    },
    directives:{
        a(el,bind,vnode,revnode){
            console.log(el,bind,vnode,revnode);
        },
        b:{
            created(){
                console.log('created');
            },
            beforeMount(){
                console.log('beforeMount');
            },
            mounted(){
                console.log('mounted');
            },
            beforeUpdate(){
                console.log('beforeUpdate');
            },
            updated(){
                console.log('updated');
            },
            beforeUnmount(){
                console.log('beforeUnmount');
            },
            unmounted(){
                console.log('unmounted');
            },
        }
    },
}
</script>

<style>
.duplicateClass .teleportWrap{
    width: 100%;
    height: 30px;
    background-color: orange;
}
</style>