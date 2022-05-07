<template>
  <div>
      第二个页面
  </div>
</template>

<script>

  export default {
    data() {
      return {
        title: '第二个页面：Hello World!'
      }
    },
    head() {
      return {
        title: this.$obj.b, 
        meta: [
          {
            hid: 'description',
            name: 'description',
            content: this.$obj.b
          }
        ]
      }
    }
  }
</script>
