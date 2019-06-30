<template>
  <div class="" v-if='!confirmed'>
    <GoogleMapLoader
      style='height: 60vh'
      :mapConfig="mapConfig"
      :apiKey="MAPS_KEY"
    >
    </GoogleMapLoader>

    <div class="pricing">
      <div class="rides-count">
        {{ ridesCount }} corridas
      </div>

      <div class="estimate-price">
        R$ 404,55/mês
      </div>
    </div>

    <div class="mt-4 px-3">
      <v-btn @click="confirm()" class="px-3 mb-3" flat color="#fff" style="background: #000; width: 100%; margin: 0;">
        Confirmar
      </v-btn>
      <v-btn @click="$router.back()" class="px-3" flat color="#707070" outline style="width: 100%; margin: 0;">
        Voltar
      </v-btn>
    </div>

  </div>

  <div style="height: 100%; display: flex; align-items: center; justify-content: center; flex-direction: column;" v-else>
    <img src="@/assets/success.jpg" />
    <h2>Em breve seu favorito chegará 😉</h2>

    Obrigado por confiar nele e em nós 💚
  </div>
</template>
<script type="text/javascript">
const MAPS_KEY = process.env.VUE_APP_MAPS_KEY
import GoogleMapLoader from '@/components/GoogleMapLoader'
import GoogleMapMarker from "@/components/GoogleMapMarker";
import GoogleMapLine from "@/components/GoogleMapLine";

import { mapSettings } from "@/constants/mapSettings";
import Vue from 'vue'
import _ from 'lodash'

export default {
  name: 'EstimatePrice',

  data() {
    return {
      google: null,
      map: null,
      MAPS_KEY: MAPS_KEY,
      confirmed: false,
    }
  },

  components: {
    GoogleMapLoader,
    GoogleMapMarker,
    GoogleMapLine
  },

  computed: {

    ridesCount() {
      return (this.daysSelected && this.daysSelected.length || 0) * 4
    },

    mapConfig() {
      return {
        ...mapSettings,
        center: this.mapCenter
      };
    },

    mapCenter() {
      return { lat: -22.907364, lng: -43.1775717 }
    },
  },

  props: {
    driver: {
      type: Object
    },

    initialPlace: {
      type: Object
    },

    finalPlace: {
      type: Object
    },

    daysSelected: {
      type: Array
    }
  },

  methods: {
    confirm(){
      this.confirmed = true
    }
  }
}
</script>

<style type="text/css">
.pricing {
  height: 58px;
  display: flex;
  align-items: center;
  margin-left: 28px;
  margin-right: 28px;
  margin-top: 28px;
  box-shadow: 0 3px 6pt rgba(0,0,0,0.16);
}
.rides-count {
  text-transform: uppercase;
  text-align: left;
  flex: 1 1 auto;
  margin-left: 12px;
}
.estimate-price {
  font-size: 20px;
  margin-right: 12px;
  color: #000;
}
</style>