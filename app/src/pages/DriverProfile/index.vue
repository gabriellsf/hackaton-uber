<template>
  <div>
    <v-layout class="mx-4 mt-4" wrap style="align-items: center; text-align: left;">
      <v-flex xs6 lg2 md2>
        <v-icon size="32" @click="$router.back()">arrow_back</v-icon>
      </v-flex>

      <v-flex></v-flex>

      <v-flex xs6 lg1 md1 style="text-align: right;">
        <img src="@/assets/logo.png" height="26" width="auto" />
      </v-flex>
    </v-layout> 

    <div class="driver" v-if='driver'>
      <div class="driver-avatar">
        <img :src="driver.foto" />
      </div>
      <div class="driver-name">
        {{ driver.name }}
      </div>
    </div>

    <div class="">
      <v-btn @click="setDestination()" class="px-3" flat color="#fff" style="background: #000; width: 250px;">
        AGENDAR HORÁRIOS
      </v-btn>
      <br />
      <v-btn @click="$router.back()" class="px-3" flat color="#707070" outline style="width: 250px;">
        Voltar
      </v-btn>
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
  name: 'DriverProfile',

  data() {
    return {

    }
  },

  props: {
    driver: {
      type: Object
    }
  },

  created() {

  },

  methods: {
    setDestination() {
      this.$router.push({ name: 'destination'})
    }
  }
}
</script>

<style scoped>
.driver-avatar {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  overflow: hidden;
  border: 1px solid #1dff8d;
  display: flex;
}
.driver-name {
  font-size: 24px;
  color: #000;
  text-align: center;
}
.driver {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 24px;
  margin-bottom: 24px;
}
</style>
