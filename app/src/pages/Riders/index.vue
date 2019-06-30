<template>
  <div class="home" v-loading='loading'>
    <v-layout class="mx-4 mt-4" wrap style="align-items: center; text-align: left;">
      <v-flex xs6 lg2 md2>
        <v-icon size="32" @click="$router.back()">arrow_back</v-icon>
      </v-flex>

      <v-flex></v-flex>

      <v-flex xs6 lg1 md1 style="text-align: right;">
        <img src="@/assets/logo.png" height="26" width="auto" />
      </v-flex>
    </v-layout> 

    <div> 
      <div class="title-pattern">
        Todas corridas
      </div>

      <div class="last-ride" v-if='lastRide'>
        <div class="last-ride-avatar">
          <img :src="lastRide.foto" />
        </div>
        <div>
          <div class="last-ride-name">
            {{ lastRide.name }}
          </div>
          <div class="last-ride-date">
            {{ formatDate(lastRide.createdAt) }}
          </div>
          <v-btn @click="favorite(lastRide)" class="px-3" flat color="#fff" style="background: #000;">
            <v-icon color="yellow" class="mr-2">star</v-icon>
            Favoritar
          </v-btn>
        </div>
      </div>
    </div>

  </div>
</template>
<script type="text/javascript">
import Axios from 'axios'
import _ from 'lodash'
import ErrorMessage from '@/helpers/ErrorMessage'
import GoogleMaps from '@/services/GoogleMaps'
import moment from 'moment'
moment.locale('pt-BR')

export default {
  name: 'Riders',

  data() {
    return {
      loading: false,
      lastRide: {
        foto: 'https://ait.bypronto.com/wp-content/uploads/sites/2404/2018/01/img-people-harsha-s-abeykoon.png',
        name: 'Valdir Ferreira de Bassos',
        createdAt: new Date()
      },
      favorites: [
        { nome: 'Valdir FASAF fas fsafa', foto: 'https://ait.bypronto.com/wp-content/uploads/sites/2404/2018/01/img-people-harsha-s-abeykoon.png', empresa: 'Uber', motorista_empresa_id: '12345678' },
        { nome: 'Valdir', foto: 'https://ait.bypronto.com/wp-content/uploads/sites/2404/2018/01/img-people-harsha-s-abeykoon.png', empresa: 'Uber', motorista_empresa_id: '12345678' },
      ],

    }
  },

  created() {

  },

  watch: {

  },

  computed: {

  },

  methods: {

    async fetchLastRide() {
      this.loading = true

      try {
        let res = await Axios.get('/riders')

        this.loading = false
      } catch(err) {
        this.loading = false
        this.$message({
          type: 'error',
          message: ErrorMessage(err),
        }) 
      }
    },

    async favorite(driver) {
      this.loading = true
      console.log(driver)
      try {
        let res = await Axios.post('/favorites', driver)
        
        this.$message({
          type: 'success',
          message: 'Motorista favoritado com successo!'
        })
        this.fetchLastRide()
      } catch(err) {
        this.loading = false
        this.$message({
          type: 'error',
          message: ErrorMessage(err),
        }) 
      }
    },

    formatDate(date, format = 'DD/MM/YYYY') {
      return moment(date).format(format)
    },
  }
}
</script>

<style scoped>
.title-pattern {
  height: 40px;
  background: #000;
  text-transform: uppercase;
  color: #fff;
  line-height: 40px;
  font-size: 18px;
  margin-left: 12px;
  margin-right: 12px;
  margin-top: 32px;
}
.last-ride-avatar {
  width: 98px;
  height: 98px;
  border-radius: 50%;
  overflow: hidden;
  border: 1px solid #707070;
  flex: none;
}
.last-ride {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 36px;
  margin-left: 36px;
  margin-right: 36px;
}
.last-ride-name {
  font-size: 24px;
  color: #000;
  margin-left: 24px;
  text-align: left;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
}
.last-ride-date {
  margin-left: 24px;
  text-align: left;
  color: rgba(0, 0, 0, 0.4);
}
.favorites {
  display: flex;
  margin-top: 16px;
  margin-left: 16px;
}
.favorite {
  margin-right: 24px;
  width: 84px;
}
.favorite-avatar {
  width: 84px;
  height: 84px;
  border-radius: 50%;
  overflow: hidden;
  border: 1px solid #1dff8d;
}
.favorite-name {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
}
</style>
