<template>
<div v-show="!printing">
    <el-button @click="add">add</el-button>
    <el-button @click="addInner">addInner</el-button>
    <div ref="aaa">
        a:{{a}}
        b:{{b.a}}
        <br>
        c:{{c.a}}
        d:{{d}}
        <br>
        e:{{e}}
        f:{{f}}
    </div>
    <hr>
    <div :class="$style.a">mixin</div>
    <el-button @click="sayHello">sayHello</el-button>
</div>
<div v-show="printing">
    只想打印这个字符串！！
</div>
</template>

<script>
import combinationApiSetup from "./combinationApi";
import mixin from "./mixin";
import {useCssModule} from 'vue'

export default {
    name:'combinationApi',
    data(){
        return{
            sayFor:"world(father)",
            printing:false,
        }
    },
    created(){
        console.log(`mixin say hi ${this.sayFor} i'm created`)
    },
    setup(){
        let {a,b,c,d,e,f,addInner} = combinationApiSetup()
        let style = useCssModule()
        console.log(style);
        return{
            a,
            b,
            c,
            d,
            e,
            f,
            addInner
        }
    },
    watch:{
        d(){
            console.log(123); //任何状态都监听不到（addInner和 add）
        },
        e(){
            console.log("e发生了变化"); 
        }
    },
    mixins:[mixin],
    methods: {
        add(){
            this.a ++ 
            this.d ++  //监听的到
            this.b.a += 2
            this.printing = true
            this.$nextTick(() => {
                window.print()
            })
            let that = this
            window.onafterprint = () => { //打印完成跳回原页面
                that.printing = false
            }
        },
        sayHello(){
            console.log(`mixin say hello ${this.sayFor}`)
        }
    },
}
</script>

<style module>
.a{
    background:red
}
</style>