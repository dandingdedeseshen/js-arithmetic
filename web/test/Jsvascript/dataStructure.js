// 队列
class Queue{
    constructor(length){
        this.length = length||100
        this.left = 0
        this.right = 0
        this.arr = []
    }
    isEmpty(){
        return this.left % this.length === this.right % this.length
    }
    isFull(){
        return this.right - this.left === this.length - 1
    }
    push(e){
        if(this.isFull()){
            console.error('Queue is Full!')
            return
        }  
        this.arr[this.right % this.length] = e
        this.right ++
    }
    pop(){
        if(this.isEmpty()){
            console.error('Queue is Empty!')
            return null
        }
        let e = this.arr[this.left % this.length]
        this.left ++ 
        return e
    }
}

// 双链表
class Chain{
    constructor(val){
        if(Array.isArray(val)){
            const obj = this.createNode(val[0])
            this.headNode = obj   
            this.tailNode = obj    //代码赋值不用浅拷贝，利用传值赋值的特性可以更新根节点
            for(let i = 1;i < val.length;i++){
                this.push_tail(val[i]) 
            }
        }else{
            const obj = this.createNode(val)
            this.headNode = obj 
            this.tailNode = obj
        }
    }
    // 创建一个新节点
    createNode(val){
        return{
            parent:null,
            next:null,
            val:val || null,
        }
    }
    // 头插(默认插入头结点之前)
    push_per(val,node){
        const obj = this.createNode(val)
        if(node && node.parent){
            obj.next = node
            obj.parent = node.parent
            node.parent.next = obj  //不要忘记将父节点的指针指向新的node
            node.parent = obj
        }else{
            obj.next = this.headNode
            this.headNode.parent = obj //在这里因为传址所以根节点的parent跟随着一起更新了
            this.headNode = obj
        }
    }
    // 尾插
    push_tail(val,node){
        const obj = this.createNode(val)
        if(node && node.next){
            obj.parent = node
            obj.next = node.next
            node.next.parent = obj
            node.next = obj  
        }else{
            obj.parent = this.tailNode
            this.tailNode.next = obj
            this.tailNode = obj
        }
    }
    // 查找(返回一个新的实例无法改变当前查询的链)
    find(val){
        let node = this.headNode
        while (node.next){
            node = {...node.next}
            if(node.val === val){
                return node
            }
        }
    }
    // 删除
    del(node_p){
        let node = node_p.parent
        if(!node.next.next){ //删除的是尾结点
            node.next = null
            this.tailNode = node
        }else{
            node.next.next.parent = node
            node.next = node.next.next
        }
        
    }
    // 遍历
    forEach(){
        let node = this.headNode
        while (node.next){
            console.log(node.val)
            node = {...node.next}
        }
        // 循环进入尾巴节点直接跳出所以单独打印一下
        console.log(node.val)
    }
}

// 哈希表
class HashList{
    constructor(){
        this.arr = Array(10)
        // 循环单独写入链表 直接使用fill会导致所元素公用一个链表
        for(let i = 0;i < this.arr.length; i++){
            this.arr[i] = new Chain('开始元素')
        }
    }
    // 哈希函数
    hash(num){
        return parseInt(num % 10) || 0
    }
    // 插入
    insert(key,val){
        let index = this.hash(key)
        this.arr[index].push_tail(val)
    }
    // 查找
    find(key){
        return this.arr[this.hash(key)]
    }
}

// 二叉搜索树(左小右大)
    //不支持插入同样的元素
class Tree{
    constructor(val){
        if(Array.isArray(val)){
            let obj = this.creadNode(val[0])
            this.headNode = obj
            for(let i = 1;i < val.length;i++){
                this.insert_loop(val[i]) 
            }
        }else{
            let obj = this.creadNode(val)
            this.headNode = obj
        }
    }
    // 创建节点
    creadNode(val){
        return{
            val:val||null,
            left:null,
            right:null,
            // parent:null
        }
    }
    // 插入（递归版）
    insert(val,node = this.headNode){
        let obj = this.creadNode(val)
        if(val < node.val){
            node.left?this.insert(val,node.left):node.left = obj
        }else{
            node.right?this.insert(val,node.right):node.right = obj
        }
    }
    // 插入（循环）
    insert_loop(val){
        let obj = this.creadNode(val)
        let node = this.headNode
        while(true){
            if(val < node.val){
                if(node.left){
                    node = node.left
                    continue
                }else{
                    node.left = obj
                    break
                }
            }else{
                if(node.right){
                    node = node.right
                    continue
                }else{
                    node.right = obj
                    break
                }
            }
        }
    }
    // 查找(递归)
    find(val,node = this.headNode){
        if(val < node.val){
            if(node.left){
               return this.find(val,node.left)
            }else{
                return null
            }
        }else if(val > node.val){
            if(node.right){
                return this.find(val,node.right)
            }else{
                return null
            }
        }else{
            return node
        }
    }
    // 查找(循环)
    find_loop(val){
        let node = this.headNode
        while(true){
            if(val < node.val){
                if(node.left){
                    node = node.left
                    continue
                }else{
                    return null
                }
            }else if(val > node.val){
                if(node.right){
                    node = node.right
                    continue
                }else{
                    return null
                }
            }else{
                return node
            }
        }
    }
    // 删除
    del(){

    }
    // 先序遍历
    foreach_pre(node = this.headNode){
        if(node){
            console.log(node.val)
            this.foreach_pre(node.left)
            this.foreach_pre(node.right)
        }
    }
    // 中序遍历
    forEach_mid(node = this.headNode){
        if(node){
            this.forEach_mid(node.left) //遍历只是改变递归顺序但是这里用了三个函数名称 所以复制完要改名！！！
            console.log(node.val)
            this.forEach_mid(node.right)
        }
        
    }
    // 后序遍历
    forEach_next(node = this.headNode){
        if(node){
            this.forEach_next(node.left)
            this.forEach_next(node.right)
            console.log(node.val)
        }
    }
}

let tree = new Tree([2,4,5,6,3,1,8,9,7])
// tree.foreach_pre()
// console.log('**********')
tree.forEach_mid()
// console.log('**********')
// tree.forEach_next()