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

    <div class="topbar">
      <div class="">

      </div>

      <div class="">
        
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
  name: 'Destination',

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
}
</script>

<style scoped>
</style>
