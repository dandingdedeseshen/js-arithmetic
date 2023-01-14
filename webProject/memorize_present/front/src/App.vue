<template>
  <div id="app">
    <router-view v-slot="{ Component, route }">
      <transition :enter-active-class="'animated ' + (route.meta.transition || 'fadeIn')">
        <keep-alive>
          <component
            :is="Component"
            :key="route.meta.usePathKey ? route.path : undefined"
          />
        </keep-alive>
      </transition>
    </router-view>
  </div>
</template>
