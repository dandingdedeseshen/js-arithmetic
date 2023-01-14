<template>
  <div class="mainWrap">
    <el-menu default-active="/" class="leftMenuWrap" router>
      <el-menu-item index="/">首页</el-menu-item>
      <el-sub-menu
        v-for="(item, index) in routeArr"
        :key="index"
        :index="index.toString()"
      >
        <template #title>
          <span>{{ item.name }}</span>
        </template>
        <el-menu-item
          v-for="(sonItem, index) in item.children"
          :key="index"
          :index="sonItem.path"
          >{{ sonItem.name }}</el-menu-item
        >
      </el-sub-menu>
    </el-menu>
    <!-- 组件示例 -->
    <div class="tabWrap" v-show="showDemo">
      <el-tabs v-model="activeName">
        <el-tab-pane label="基础教程" name="tutorial">
          <h4>可以继承属性的组件</h4>
          <first-demo :style="{ 'font-size': '100px' }"/>
          <hr />
          <h4>render函数渲染的组件</h4>
          <render-fun></render-fun>
          <hr />
        </el-tab-pane>
        <el-tab-pane label="User" name="first"> </el-tab-pane>
      </el-tabs>
    </div>
    <div class="viewWrap" v-show="!showDemo">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import FirstDemo from "@/components/tutorial/firstDemo.vue";

export default {
  name: "HomeView",
  data() {
    return {
      activeName: "tutorial",
      routeArr: [
        {
          name: "基础入门",
          children: [
            {
              name: "混合api-setup",
              path: "/tutorial/combinationApi",
            },
            {
              name: "window.print()",
              path: "/tutorial/printPage",
            },
            {
              name: "过渡-transition",
              path: "/tutorial/transitionTest",
            },
            {
              name: "自定义指令-directives",
              path: "/tutorial/myAttribute",
            }
          ],
        },
        {
          name: "API",
          path: "/tutorial",
        },
      ],
    };
  },
  computed: {
    showDemo() {
      return this.$route.fullPath === "/";
    },
  },
  methods: {
  },
  components: {
    FirstDemo,
  },
};
</script>

<style>
.mainWrap {
  width: 99vw;
  display: flex;
}
.mainWrap .leftMenuWrap {
  flex-basis: 300px;
  overflow: hidden;
}
.mainWrap .tabWrap {
  width: 100%;
  padding: 10px;
}
.mainWrap .viewWrap {
  width: 100%;
}
.mainWrap .el-sub-menu__title {
  font-size: 12px;
}
</style>
