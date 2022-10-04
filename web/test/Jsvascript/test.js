let aa = document.querySelector('.a')
let bb = document.querySelector('.b')
// 拖拽
// bb.ondragstart = (e) => {
//     console.log('ondragstart');
//     let obj = {a:1,b:2,c:3}
//     e.dataTransfer.setData('aaa',JSON.stringify(obj))
// }

// aa.ondragover = (e) => {
//     e.preventDefault()  //阻止默认事件 让a元素可以触发drop事件
// }
// aa.ondrop = (e) => {
//     console.log('ondrop-aa');
//     let str = e.dataTransfer.getData('aaa')
//     console.log(JSON.parse(str));
// }

// 影子DOM
// let bbShodow = bb.attachShadow({mode:'open'})  // 使用现有元素
// bbShodow.innerHTML = `<div class="b">
//                         <slot></slot>
//                     </div>`

// let cc = document.createElement('div')         // 重新创建元素
// cc.classList = 'c'
// let ccShodow = cc.attachShadow({mode:'open'})
// ccShodow.appendChild(aa)
// document.body.appendChild(cc)


let obj = {
    a:1,
    b:2
}

let str = JSON.stringify(obj,null,4)
console.log(JSON.parse(str));