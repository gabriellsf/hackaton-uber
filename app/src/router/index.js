import Vue from 'vue'
import VueRouter from 'vue-router'

// Pages
import UberMock from '@/pages/UberMock'
import Favorites from '@/pages/Favorites'
import Riders from '@/pages/Riders'
import DriverProfile from '@/pages/DriverProfile'
import Destination from '@/pages/Destination'
import Schedules from '@/pages/Schedules'
import EstimatePrice from '@/pages/EstimatePrice'

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
      name: 'favorites',
      path: '/favorites',
      component: Favorites,
      meta: {
        title: 'Meus favoritos',
      },
    },

    {
      name: 'riders',
      path: '/riders',
      component: Riders,
      meta: {
        title: 'Todas corridas',
      },
    },

    {
      name: 'driver-profile',
      path: '/driver-profile',
      component: DriverProfile,
      meta: {
        title: 'Meu Favorito',
      },
      props: true
    },

    {
      name: 'destination',
      path: '/destination',
      component: Destination,
      meta: {
        title: 'Defina o destino',
      },
      props: true
    },

    {
      name: 'schedules',
      path: '/schedules',
      component: Schedules,
      meta: {
        title: 'Defina a sua rotina',
      },
      props: true
    },

    {
      name: 'estimate-price',
      path: '/estimate-price',
      component: EstimatePrice,
      meta: {
        title: 'Descubra o valor',
      },
      props: true
    },
    // { path: '*', redirect: '/login' }
  ]
})

export default router