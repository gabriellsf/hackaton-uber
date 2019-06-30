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
        Última corrida
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

      <el-button @click="$router.push({ name: 'riders' })" class="pa-0" type="text" style="width: 100%; text-align: left; margin-top: 12px; margin-left: 36px;">Ver todas as corridas</el-button>

      <div class="title-pattern" style="margin-top: 20px!important">
        Meus favoritos
      </div>

      <div class="favorites">
        <div class="favorite" v-for='favorite in favorites' @click="options = favorite.foto">
          <div class="favorite-avatar" v-ripple><img :src="favorite.foto" /></div>
          <div class="favorite-name">{{ favorite.nome }}</div>
        </div>
      </div>
    </div>

    <v-bottom-sheet v-model="options">
      <v-list>
        <v-subheader>Ações</v-subheader>
        <v-list-tile @click="removeFromFavorites(options)">
          <v-list-tile-title>
            <v-icon class="mr-2">close</v-icon>
            Remover dos favoritos
          </v-list-tile-title>
        </v-list-tile>

        <v-list-tile @click="scheduleFavorite(options)">
          <v-list-tile-title>
            <v-icon class="mr-2">event</v-icon>
            Agendar horários
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-bottom-sheet>
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
  name: 'Favorites',

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

      options: false 
    }
  },

  created() {

  },

  watch: {

  },

  computed: {
    entries() {
      return ([]).concat(this.places)
    },
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

      try {
        let res = await Axios.post('/favorites', driver)
        
        this.$message({
          type: 'success',
          message: 'Motorista favoritado com successo!'
        })
        this.fetchLastRide()
      } catch(err) {
        this.$router.push({ name: 'driver-profile', params: {
          driver: driver
        }})

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
