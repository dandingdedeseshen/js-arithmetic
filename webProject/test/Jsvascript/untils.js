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

// 绘制迷宫
function drawMaze(arr){
    let wrap = $('#mazeWrap')
    const mazeWidth = 20
    wrap[0].style.width = (arr[0].length + 2) * mazeWidth + 'px'
    wrap.empty()
    let col = 0
    for(let item of arr){
        col ++
        let row = 0
        for(let son of item){
            row ++
            let divTemp = document.createElement('div')
            divTemp.style.width = mazeWidth + 'px'
            divTemp.style.height = mazeWidth + 'px'
            $(divTemp).data('col',col)
            $(divTemp).data('row',row)
            // todo 可以点击div改变迷宫路径
            // $(divTemp).on('click',changeVal($(divTemp),maze))
            switch(son){
                case 0:
                    divTemp.className = 'white'
                    break;
                case 1:
                    divTemp.className = 'black'
                    break;
                case 2:
                    divTemp.className = 'tomato'
                    break;
                case 3:
                    divTemp.className = 'orange'
                    break;
                default:
                    divTemp.className = 'skyblue'
                    break;
            }
            wrap.append(divTemp)
        }
    }
}

let l = console.log
