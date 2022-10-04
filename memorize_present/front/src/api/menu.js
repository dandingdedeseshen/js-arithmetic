import {res1,res2} from "./mock/menu/MB13401"

export function MB13401(parm){
    return new Promise((resolve,reject) => {
        if(parm.id == 1){
            resolve(res1)
        }else{
            resolve(res2)
        }
    })
}