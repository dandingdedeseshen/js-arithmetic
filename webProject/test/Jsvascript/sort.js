// 二分查找
function binary_find(arr, goal) {
    let left = 0
    let right = arr.length - 1
    let i = 0
    while (i < arr.length) {
        i++
        let mid = parseInt((right + left) / 2)
        let num = arr[mid]
        if (goal === num) {
            return mid
        } else if (goal > num) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}

// 冒泡排序 arrLength:10000 time:281 - 293
function bubble_sort(arr) {
    let isSort
    for (let i = 0; i < arr.length - 1; i++) {
        isSort = true //冒泡优化 如果内部循环没有执行过交换则证明该数组有序直接返回即可
        for (let j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
                isSort = false
            }
        }
        if (isSort) {
            break
        }
    }
}
// 选择排序 arrLength:10000 time:74 - 79
function select_sort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let minIndex = i
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j
            }
        }
        [arr[minIndex], arr[i]] = [arr[i], arr[minIndex]]
    }
}
// 插入排序 arrLength:10000 time:35 - 40
function insert_sort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let j = i - 1
        const tmp = arr [i]
        while (j >= 0 && arr[j] < tmp ){
            arr[j + 1] = arr[j]
            j = j - 1
        } 
        arr[j + 1] = tmp 
    }
}

//快速排序 arrLength:10000 time:4 - 8
function fast_sort(arr, left, right,flag) {
    if (left>=0&&left < right&&right<arr.length) {
        let mid = homing(arr, left, right)
        fast_sort(arr, mid + 1, right,'right')
        fast_sort(arr, left, mid - 1,'left')
    }
   
}
// 归位函数
function homing(arr, left, right) {
    let homingVal = arr[left]
    // 大循环遍历一次数组
    while (left < right) {
        // 当右边指向的数字小于或等于归位数时向左移动
        while (left < right && homingVal <= arr[right]) {
            right--
        }
        arr[left] = arr[right]
        // 左边小于等于右移动
        while (left < right && homingVal >= arr[left]) {
            left++
        }
        arr[right] = arr[left]
    }
    arr[left] = homingVal
    return left
}
// 封装下快速排序函数
function fast_sort_run(arr){
    fast_sort(arr, 0, arr.length - 1)
}

// 堆排序 arrLength:10000 time:8 - 13
function heap_sort(arr){
    let j = arr.length - 1
    let i = Math.ceil(j / 2) - 1
    // 生成大根堆
    while(i >= 0){
        sift(arr,i,j)
        i--
    }
    // 挨个出数
    while(j > 0){
        [arr[0],arr[j]] = [arr[j],arr[0]]
        sift(arr,0,j - 1)
        j --
    }
}
// 堆的向下调整函数
function sift(arr,topIndex,lastIndex){
    let i = topIndex;
    let j = i * 2 + 1
    while(j <= lastIndex){
        if(arr[j] < arr[j+1] && j+1 <= lastIndex){
            j = j + 1
        }
        if(arr[i] < arr[j]){
            [arr[i],arr[j]] = [arr[j],arr[i]]
            i = j
            j = i * 2 + 1
        }else{
            break
        }
    }
}
// 生成一个堆的视图最多31个元素
function creatHeap(arr){
    for(let i = 0; i < arr.length;i++){
        $('span').eq(i).text(arr[i])
    }
}

// 归并排序 arrLength:10000 time:6 - 10
function merge_sort(arr,left,right,flag){
    if(left < right){
        let mid =  parseInt((left + right) / 2)
        merge_sort(arr,left,mid,'left')
        merge_sort(arr,mid + 1,right,'right')
        merge(arr,left,mid,right)
    }
}
// 一次归并
function merge(arr,left,mid,right){
    let arrCopy = []
    let i = left;
    let j = mid + 1
    while(j<=right&&i<=mid){
        if(arr[j] < arr[i]){
            arrCopy.push(arr[j])
            j++
        }else{
            arrCopy.push(arr[i])
            i++
        }
    }
    while(j<=right){
        arrCopy.push(arr[j])
        j++
    }
    while(i<=mid){
        arrCopy.push(arr[i])
        i++
    }
    let x = 0
    for(let i = left;i <= right;i++){
        arr[i] = arrCopy[x]
        x++
    }
}
function merge_sort_main(arr){
    merge_sort(arr,0,arr.length - 1)
}

// 希尔排序 arrLength:10000 time:32 - 36 比插入慢！？
function hill_sort(arr){
    let step = parseInt(arr.length / 2)
    while(step >= 1){
        hill(arr,step)
        step = parseInt(step / 2)
    }
}
// 希尔插入排序
function hill(arr,step){
    for(let i = step;i < arr.length;i += step){
        let j = i - step
        const tmp = arr [i]
        while (j >= 0 && arr[j] < tmp){
            arr[j + step] = arr[j]
            j = j - step
        } 
        arr[j + step] = tmp
    }
}

// 计数排序 arrLength:10000 time:7- 12
function number_sort(arr){
    let finallArr = []
    for(let item of arr){
        if(finallArr[item]){
            finallArr[item]++
        }else{
            finallArr[item] = 1
        }
    }
    console.log(finallArr)
    arr.length = 0
    for(let i = 0;i < finallArr.length;i++){
        for(let j = 1;j <= finallArr[i];j++){
            arr.push(i)
        }
    }
}

// 桶排序 arrLength:10000 time:16- 20
function bocket_sort(arr1){
    let finallArr = []
    for(let item of arr1){
        let i = parseInt(item / 1000)
        if(finallArr[i]){
            let j = finallArr[i].length - 1
            while(j >= 0  && finallArr[i][j] > item){
                finallArr[i][j + 1] = finallArr[i][j]
                j --
            }
            finallArr[i][j + 1] = item
        }else{
            finallArr[i] = []
            finallArr[i].push(item)
        }
    }
    arr1.length = 0
    for(let item of finallArr){
        if(item&&item.length){
            for(let i = 0; i < item.length; i ++){
                arr1.push(item[i])
            }
        }
    }
}
// let arr = creatRandomArr(10)
// console.log(arr)
// bocket_sort(arr,1)
// console.log(arr)

// 测试排序10000长度的数组所需时间
function test(sortFun) {
    let arr = []
    const arrLength = 10000
    for (let i = 0; i < arrLength; i++) {
        arr.push(parseInt(Math.random() * 10000))
    }
    // let arr = creatRandomArr(10000)
    const beforeDate = new Date()
    sortFun(arr)
    const afterDate = new Date()

    console.log(arr)
    console.log(afterDate - beforeDate)
}
test(bocket_sort)
