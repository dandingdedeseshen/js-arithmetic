<template>
  <div>
    <div id="page1Box">
      <div id="top">
        <img src="../assets/timg_03.png">
        <span>后台管理登录</span>
      </div>
      <div id="section">
        <div id="user">
          <p>用户名:</p>
          <input type="text" placeholder="139574566@">
        </div>
        <div id="pas">
          <p>密码:</p>
          <input type="password">
        </div>
        <div id="code">
          <p>验证码:</p>
          <input type="password">
        </div>
        <div id="but">
          <button :class='cla' @click.once="gain()">{{mess}}</button>
        </div>
      </div>
      <div id="footer">

      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return(
      {
        mess:'登录',
        a:9,
        cla:'yes'
      }
    )
  },
  methods: {
    gain(){
      this.cla = 'no'
      let time = setInterval(() => {
        this.mess = this.a
        this.a--
        if(this.a < 0){
          this.a = 9
          this.mess = '登录'
          clearInterval(time)
          this.cla = 'yes'
        }
      }, 1000);
    }
  },
}
</script>

<style>
  #page1Box{
    margin: auto;
    width: 180px;
    height: 245px;
    /* background-color: black */
  }
  #top>image{
    width: 45px;
    height: 20px;
  }
  #top>span{
    margin-left: 13px;
    padding-left: 13px;
    display: inline-block;
    border-left: 2px solid blue;
    width: 100px;
    height: 22px;
    vertical-align: top;
    line-height: 22px;
    color: white;
    font-weight: 600;
  }
  #section{
    margin-top: 25px;
    padding-top: 15px;
    width: 181px;
    height: 160px;
    border-radius: 10px;
    background-color: white;
  }
  #user,#pas,#code,#but{
    width: 153px;
    height: 25px;
    margin: auto;
    margin-bottom: 15px;
  }
  #user>p,#pas>p,#code>p{
    height: 8px;
    font-size: 10px;
    text-align: left;
  }
  #user>input,#pas>input,#code>input{
    outline: none;
    width: 153px;
    height: 15px;
    border-radius: 3px;
    border: 1px solid black;
    font-size: 10px;
    line-height: 15px;
    padding-left: 2px;
  }
  #but>.yes,#but>.no{
    width: 150px;
    height: 23px;
    outline: none;
    background-color: blue;
    border: 1px solid white;
    color: white;
    font-size: 10px;
    text-align: center;
    line-height: 23px;
  }
  #but>.no{
    background-color: gray;
  }
</style>