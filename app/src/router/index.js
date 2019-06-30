import Vue from 'vue'
import VueRouter from 'vue-router'

// Pages
import UberMock from '@/pages/UberMock'
import Favorites from '@/pages/Favorites'
import Riders from '@/pages/Riders'
import DriverProfile from '@/pages/DriverProfile'
import Destination from '@/pages/Destination'

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

    // { path: '*', redirect: '/login' }
  ]
})

export default router