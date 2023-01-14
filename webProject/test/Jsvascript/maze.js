let maze = [
    [0,0,0,0,0,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,1,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,1,1,0,1,0,1,1,1,1],
    [1,0,1,0,0,0,0,1,0,1,1,1,1,1],
    [0,0,1,0,0,0,1,1,1,1,1,1,1,1],
    [0,1,0,0,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
]

// 栈-深度优先寻找路径
function findPath_stack(maze,x1,y1,x2,y2){
    maze[x1][y1] = 3
    maze[x2][y2] = 4
    let arr = []
    let currentDot = [x1,y1]
    arr.push(currentDot)
    // 寻路的四个方向
    let driectionArr = [
        [1,0],
        [0,1],
        [-1,0],
        [0,-1],
    ]
    // 间隔一段时间寻一次路
    let timer = setInterval(() => {
        if(arr.length <= 0){
            clearInterval(timer)
            console.log("无路径")
        }
        drawMaze(maze)
        let flag = false
        for(let item of driectionArr){
            let nextDot = [currentDot[0] + item[0],currentDot[1] + item[1]]
            if(nextDot[0] < 0 || nextDot[1] < 0 || nextDot[0] > 8 || nextDot[1] > 13){
                continue
            }
            if(nextDot[0] === x2 && nextDot[1] === y2){
                clearInterval(timer)
                console.log(arr)
            }
            if(maze[nextDot[0]][nextDot[1]] === 0){
                maze[nextDot[0]][nextDot[1]] = 2
                arr.push(nextDot)
                currentDot = nextDot
                flag = true
                break
            }
        }
        if(!flag){
            currentDot = arr.pop()
        }
    }, 30);
}
// 队列-广度优先寻找路径
function findPath_Queue(maze,x1,y1,x2,y2){
    maze[x1][y1] = 3
    maze[x2][y2] = 4
    // 寻路的四个方向
    const driectionArr = [
        [1,0],
        [0,1],
        [-1,0],
        [0,-1],
    ]
    // 将其点记录并放入队中
    let pathArr = [[-1,x1,y1]]
    let queue = new Queue()
    queue.push([x1,y1])
    let currentPath = []
    let pathIndex = 0
    // 寻路
    let timer = setInterval(() => {
        drawMaze(maze)
        if(queue.isEmpty()){
            clearInterval(timer)
            console.log('无路径')
        }
        currentPath = queue.pop()
        for(let item of driectionArr){
            let nextPath = [currentPath[0] + item[0],currentPath[1] + item[1]]
            if(nextPath[0] === x2 && nextPath[1] === y2){
                clearInterval(timer)
                let arr = []
                let item = pathArr[pathArr.length - 1]
                while(item[0] >= 0){
                    arr.push([item[1],item[2]])
                    maze[item[1]][item[2]] = 4
                    item = pathArr[item[0]]
                }
                console.log(maze)
                drawMaze(maze)
                console.log(arr)
                console.log('找到了')
            }
            if(maze[nextPath[0]] && maze[nextPath[0]][nextPath[1]] == 0){
                maze[nextPath[0]][nextPath[1]] = 2
                pathArr.push([pathIndex,currentPath[0] + item[0],currentPath[1] + item[1]])
                queue.push(nextPath)
            }
        }
        pathIndex ++
    }, 30);
     
}

findPath_Queue(maze,0,0,8,13)