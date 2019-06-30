import Vue from 'vue'
import VueRouter from 'vue-router'

// Pages
import UberMock from '@/pages/UberMock'
import LastRiders from '@/pages/LastRiders'
import Fail from '@/pages/Fail'
import CNAE from '@/pages/CNAE'

Vue.use(VueRouter)
const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      name: 'home',
      path: '/',
      component: UberMock,
      meta: {
        title: 'Uber',
      },
    },

    {
      name: 'last-riders',
      path: '/last-riders',
      component: LastRiders,
      meta: {
        title: 'Últimas corridas',
      },
    },

    {
      name: 'fail',
      path: '/error',
      component: Fail,
      meta: {
        title: 'Ops! Área não encontrada',
      },
      props: true
    },

    {
      name: 'cnae',
      path: '/cnae',
      component: CNAE,
      meta: {
        title: 'Defina o CNAEs',
      },
      props: true
    },
    // { path: '*', redirect: '/login' }
  ]
})



export default router