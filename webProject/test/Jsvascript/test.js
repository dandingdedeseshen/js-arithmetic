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

// JSON.stringify的其他用法术
// let obj = {
//     a:1,
//     b:2
// }
// // - 第二个参数可以是数组，添加后会返回数组中包含的属性
// // - 第二个参数也可以是函数，接受两个参数 key 和 value 可以对处理结果进行简单的过滤
// // - 第三个参数可以是字符串或者数字表示不同的缩进形式
// let str = JSON.stringify(obj,null,4)
// console.log(str);

// 赋值语句的返回值
let i = 0, j = 1
console.log(i = j)