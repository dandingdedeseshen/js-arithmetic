import { setTransitionHooks } from "vue";

class FireWork {
  FIRE_NUM = 1   // 烟花数量

  canvas = document.querySelector(".canvans"); //获取画板
  ctx = this.canvas.getContext("2d"); //获取画笔
  width = window.innerWidth     //canvas宽度
  height = window.innerHeight   //canvas高度
  fireArr = []  // 烟花数组
  boomArr = [] // 爆炸碎屑数组
  textArr = [] // 爆炸碎屑数组
  contentArr = ['♍愿 每一岁都走在热爱中!','( • ̀ω•́ )✧下凡周年快乐!','不仅生日快乐还要天天快乐!','Happy Birthday!','叮!按时长大!(oﾟ▽ﾟ)o  ','永远18岁!(｡◕ˇ∀ˇ◕)']
  timer = null // 动画计时器

  constructor() {
    // 设置画板高度
    this.canvasResize()
    // 窗口变化 
    // window.onresize = this.canvasResize  尺寸变化时获取不到this.camvas
    // 触发画板动画
    this.init()
  }
  // 生成烟花
  createFire(){
    let fire = {
      x : this.#random(this.width - 10,10),
      y : this.height,
      w : 3,
      h : this.#random(20 ,9),
      r : this.#random(10 ,5),
      c1 : this.#randomColor(255,55),
      c2 : this.#randomColor(255,55,0),
      boomHeight : this.#random(300 ,100),
      textFlag : this.#random(1,2) < 1.4
    } 
    return fire
  }
  // 添加烟花
  addFire(){
    this.FIRE_NUM += 1
    this.fireArr.push(this.createFire())
  }
  // 生成爆炸碎屑
  createBoom(x,y){
    const random = Math.random
    for(let i = 1; i < 12; i++){
      for(let r = 20; r < 120; r += 25){
        const posionX = r * Math.cos((r - 30) * i * Math.PI / 180) 
        const posionY = r * Math.sin((r - 30) * i * Math.PI / 180)
        this.boomArr.push({
          x : x - posionX,
          y : y + posionY,
          a : random() * .5,
          cr : this.#random(255,55,true),
          cg : this.#random(255,55,true),
          cb : this.#random(255,55,true),
          ca : 1,
          yr : 0,
          xr : random() * 3 - 1.5
        })
        this.boomArr.push({
          x : x + posionX,
          y : y - posionY,
          a : random() * .5,
          cr : this.#random(255,55,true),
          cg : this.#random(255,55,true),
          cb : this.#random(255,55,true),
          ca : 1,
          yr : 0,
          xr : random() * 3 - 1.5
        })
      }
    }
  }
  // 生成爆炸文本
  createText(x,y){
    const obj = {
      x : x,
      y : y,
      r : this.#random(3,5),
      s : 0,
      text : this.contentArr[this.#random(0,5,true)],
    }
    this.textArr.push(obj)
  }
  // 绘制烟花
  drawFire(){
    const ctx = this.ctx
    let i = 0
    for(let item of this.fireArr){
      ctx.beginPath()
      item.y -= item.r
      const gra = this.ctx.createLinearGradient(item.x,item.y,item.x,item.y + item.h);
      gra.addColorStop(0,item.c1);
      gra.addColorStop(0.5,item.c2);
      gra.addColorStop(1,item.c2);
      ctx.shadowColor = gra
      ctx.shadowBlur = 10
      ctx.fillStyle = gra
      ctx.fillRect(item.x,item.y,item.w,item.h)
      if(item.boomHeight > item.y){
        this.fireArr.splice(i , 1)
        this.fireArr.push(this.createFire())
        item.textFlag ? this.createText(item.x,item.y) : this.createBoom(item.x,item.y)
      }
      i ++
    }
  }
  // 绘制爆炸碎屑
  drawBoom(){
    const ctx = this.ctx
    let i = 0

    for(let item of this.boomArr){
      ctx.beginPath()
      ctx.shadowColor = `rgba(${item.cr},${item.cg},${item.cb},1)`
      ctx.shadowBlur = 10
      ctx.fillStyle = `rgba(${item.cr},${item.cg},${item.cb},${item.ca})`
      item.ca -= .05
      item.yr += item.a
      item.y += item.yr
      item.x += item.xr
      ctx.arc(item.x,item.y,2,0,2 * Math.PI)
      ctx.fill()
      if(item.y > this.height - 300){
        this.boomArr.splice(i,1)
      }
      i++
    }
  }
  // 绘制爆炸文本
  drawText(){
    const ctx = this.ctx
    let i = 0

    for(let item of this.textArr){
      ctx.beginPath()
      const x = item.x + parseInt(30 * item.text.length)
      const gra = ctx.createLinearGradient(item.x,item.y,x,item.y);
      gra.addColorStop("0","magenta");
      gra.addColorStop("0.5","blue");
      gra.addColorStop("1.0","red");
      ctx.fillStyle = gra
      ctx.shadowColor = gra
      ctx.shadowBlur = 10
      item.y += item.r
      item.s < 20 ? item.s ++ : ''
      ctx.font = `${item.s}px Verdana`;
      ctx.fillText(item.text,item.x,item.y);
      if(item.y > this.height){
        this.textArr.splice(i,1)
      }
      i++
    }
  }
  // 重置画板宽高
  canvasResize(){
    this.width = window.innerWidth
    this.height = window.innerHeight
    this.canvas.width = this.width
    this.canvas.height = this.height - 5
  }
  // 随机数
  #random(max,min,isParseInt = false){
    let num = Math.random() * (max - min) + min
    num = isParseInt ? parseInt(num) : num
    return num
  }
  // 随机颜色
  #randomColor(max = 255,min = 0,a = 1){
    max = max > 255 ? 255 : max
    min = min < 0 ? 0 : min
    return `rgba(${this.#random(max,min,true)},${this.#random(max,min,true)},${this.#random(max,min,true)},${a})`
  }
  // 初始化画板内容
  init(){
    // 先生成5个烟花
    for(let i = 0; i < this.FIRE_NUM;i++){
      this.fireArr.push(this.createFire())
    }
    if(this.timer) clearInterval(this.timer)
    this.timer = setInterval(() => {
      this.ctx.clearRect(0,0,this.width,this.height)
      this.drawFire()
      this.drawBoom()
      this.drawText()
    }, 30);
    let timer1 = setTimeout(() => {
      clearTimeout(timer1)
      this.destroyed()
      this.init()
    }, 60000);
  }
  // 销毁实例释放内存
  destroyed() {
    clearInterval(this.timer)
    this.fireArr = []  // 烟花数组
    this.boomArr = [] // 爆炸碎屑数组
    console.log(this.timer);
    console.log(this.fireArr);
  }
}


export { FireWork }