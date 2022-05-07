<template>
  <div>
      第一个页面
      <nuxt-link to="second">走你</nuxt-link>
      <div v-if="flag">
        sfdasdfsadfsafasfsafasfsfd
      </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        flag:false,
        title: 'Hello World!'
      }
    },
    asyncData({isDev, route, store, env, params, query, req, res, redirect, error}) {
      
    },
    mounted(){
      let data = window.navigator
      this.flag = data ? true : false
    },
    head() {
      return {
        title: this.title,
        meta: [
          {
            hid: 'description',
            name: 'description',
            content: 'My custom description'
          }
        ]
      }
    }
  }
</script>
