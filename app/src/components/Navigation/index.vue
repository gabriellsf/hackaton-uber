<template>
  <v-app 
    style="font-family: Roboto, Ubuntu, Helvetica Neue,Helvetica,PingFang SC,Hiragino Sans GB,Microsoft YaHei,SimSun,sans-serif;">



<!--     <v-toolbar color="white" class="toolbar" app dark flat>
      <v-toolbar-side-icon class="primary--text hidden-lg-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-layout row flex class="title riemann-grey--text hidden-md-and-down">
        {{ currentRoute.meta.title }}
      </v-layout>
      <v-layout row align-center justify-center class="flex hidden-lg-and-up">
        <img src="@/assets/logo_riemann.png" height="32" />
      </v-layout>

    </v-toolbar>
 -->
    <!-- Main Content -->
    <v-content style="transition: initial !important;">
      <!-- Content with default slot -->
      <slot></slot>
    </v-content>

  </v-app>
</template>

<script>
export default {
  name: 'Navigation',
}
</script>
<style>
.v-toolbar.toolbar {
  box-shadow: 0 2px 2px rgba(0,0,0,.03), 0 1px 0 rgba(0,0,0,.03)!important;
}
.v-toolbar--fixed.toolbar {
  z-index: 4;
}
.logo-minified {
  display: flex;
  justify-content: center;
  align-items: center;
}
.riemann-navigation.v-navigation-drawer--mini-variant .v-list__tile{
  padding: 0 20px;
}
</style>