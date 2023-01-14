// 冒泡排序实现topk
function bubble_topk(arr,top){
    top = top||arr.length
    for(let i = 0;i < top;i++){
        for(let j = 0;j < arr.length - i;j++){
            if(arr[j] > arr[j + 1]){
                [arr[j],arr[j + 1]] = [arr[ j + 1],arr[j]]
            }
        }
    }
}

// 堆排序实现topk
function heap_topk(arr,top){
    top = top||arr.length
    let finallArr = arr.slice(0,top)
    let i = parseInt((finallArr.length - 1) / 2)
    // 建立堆
    while(i >= 0){
        sift(finallArr,i,finallArr.length )
        i --
    }
    // 遍历组其他元素小于堆顶的元素替换掉并且向下调整一次
    for(let i = top;i < arr.length;i++){
        if(arr[i] > finallArr[0]){
            finallArr[0] = arr [i]
            sift(finallArr,0,finallArr.length )
        }
    }
    // 出数
    for(let i = finallArr.length - 1;i >= 0; i--){
        [finallArr[0],finallArr[i]] = [finallArr[i],finallArr[0]]
        sift(finallArr,0,i)
    }
    return finallArr
}
function sift(arr,low,height){
    let i = low;
    let j = i * 2 + 1
    while(j < height){
        if(j + 1 < height&&arr[j] > arr[j + 1]){
            j = j + 1
        }
        if(arr[j] < arr[i]){
            [arr[j],arr[i]] = [arr[i],arr[j]]
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
        $('span').eq(i).text( arr[i])
    }
}
let arr = creatRandomArr(1000)
let finall = heap_topk(arr,30)
console.log(finall)


