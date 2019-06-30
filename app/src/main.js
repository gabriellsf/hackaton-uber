import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from '@/router'
import Axios from 'axios'
import Environment from '@/environment'


import 'vuetify/dist/vuetify.min.css'
import 'element-ui/lib/theme-chalk/index.css'
import '@/styles/General.css'
import '@/styles/Vuetify.css'

import Vuetify from 'vuetify'
Vue.use(Vuetify)

import Element from 'element-ui'
Vue.use(Element)

Vue.config.productionTip = false

Axios.interceptors.request.use(function (config) {
  let isBase = config.baseURL == Environment.API_URL
  if (isBase && config.url.startsWith('http')) {
    return config;
  }

  config.headers['Authorization'] = 'Bearer ' + process.env.VUE_APP_UBER_TOKEN

  return config;
})

Axios.defaults.baseURL = Environment.API_URL

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
