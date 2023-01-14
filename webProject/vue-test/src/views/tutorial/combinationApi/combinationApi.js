import { ref,reactive,readonly,inject } from 'vue'

export default function combinationApiSetup(){
    let a = ref(0)
    let d = 0
    let e = inject("e",0)
    let f = inject("f",0)
    let b = reactive({a:0})
    let c = readonly({a:0})
    

    function addInner(){
        a.value += 10
        d += 30  //监听不到
        e -= 1   //监听不到
        f.value -= 1  
        b.a += 20
        c.a ++
    }

    return {
        a,
        b,
        c,
        d,
        e,
        f,
        addInner
    }
}