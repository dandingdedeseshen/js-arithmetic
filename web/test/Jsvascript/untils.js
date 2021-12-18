// 随机生成一个不重复的sum长度的数组
function creatRandomArr(sum){
    let arr = []
    for(let i = 0; i < sum;i++){
        arr.push(i)
    }
    arr.sort(() => {
        return Math.random() - 0.5
    })
    return arr
}