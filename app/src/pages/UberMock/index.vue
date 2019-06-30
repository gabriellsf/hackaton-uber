<template>
  <div class="">
    <div class="menu-uber">
      <v-icon color="black" size="36">menu</v-icon>
    </div>
    <div class="meu-favorito">
      <v-btn color="black" dark round class="py-0 px-3" style="height: 26px;">
        <img src="@/assets/uber-eats-logo.png" height="13" width="auto" />
      </v-btn><br />
      <v-btn @click="open()" color="black" dark round><img src="@/assets/meu-favorito-white.png" height="24" width="auto" /></v-btn>
    </div>
    <GoogleMapLoader
      style='height: 80vh'
      :mapConfig="mapConfig"
      :apiKey="MAPS_KEY"
    >
    </GoogleMapLoader>

    <div class="initial-message">
      Boa noite, Felipe
    </div>

    <div class="mx-4 mt-2">
      <div class="input-search">
        <div style="flex: 1 1 auto;">Para onde?</div>
        <div class="schedule-car">
          <v-icon>commute</v-icon>
        </div>
      </div>
    </div>
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
  name: 'UberMock',

  data() {
    return {
      google: null,
      map: null,
      MAPS_KEY: MAPS_KEY,
    }
  },

  components: {
    GoogleMapLoader,
    GoogleMapMarker,
    GoogleMapLine
  },

  computed: {
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

  methods: {
    open(){
      this.$router.push({ name: 'favorites' })
    }
  }
}
</script>

<style type="text/css">
.meu-favorito {
  position: absolute;
  z-index: 100;
  right: 10px;
  top: 10px;
  text-align: right;
}
.menu-uber {
  position: absolute;
  left: 10px;
  top: 10px;
  z-index: 100;
}
.initial-message {
  height: 46px;
  line-height: 46px;
  font-size: 15px;
  font-family: Roboto;
  color: #000;
  border-bottom: 2px solid #ccc;
}
.input-search {
  height: 42px;
  display: flex;
  align-items: center;
  background: #e9e8e8;
  padding-left: 12px;
  font-size: 16px;
  text-align: left;
}
.schedule-car {
  width: 36px;
  border-left: 1px solid #ccc;
  padding-left: 12px;
  margin-right: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>