<template>
  <div style="position: relative; height: 100%;">
    <v-layout class="mx-4 pt-4" wrap style="align-items: center; text-align: left;">
      <v-flex xs6 lg2 md2>
        <v-icon size="32" @click="$router.back()">arrow_back</v-icon>
      </v-flex>

      <v-flex></v-flex>

      <v-flex xs6 lg1 md1 style="text-align: right;">
        <img src="@/assets/logo.png" height="26" width="auto" />
      </v-flex>
    </v-layout> 
    <div class="topbar">
      <div class="initial-address">
        <v-combobox
          solo
          v-model='initialAddress'
          :search-input.sync="searchInitial"
          :items="entries"
          :multiple="false"
          hide-details
          hide-no-data
          no-data-text="Nenhum resultado"
          item-text="name"
          placeholder="Digite o endereço inicial"
          class="pt-0 search-address list-addresses"
          return-object
          append-icon=""
          :no-filter="true"
        >
          <div class="prepend" slot="append">
            <v-progress-circular v-if='loadingSearchInitial' indeterminate color="primary" size="24" width="2"></v-progress-circular>
            <v-icon :size="$vuetify.breakpoint.xsOnly ? '22' : '32'" v-else>search</v-icon>
          </div>
          <template v-slot:selection="data">
            <div>
              {{ data.item && data.item.description }}
            </div>
          </template>
          <template v-slot:item="data">
            <div class="destination-name" style="text-align: left;">
              <v-icon class="mr-1" size="20" v-if='data.item && data.item.description'>
                place
              </v-icon>
              {{ data.item && data.item.description }}
            </div>
          </template>
        </v-combobox>
      </div>

      <div class="initial-address">
        <v-combobox
          solo
          v-model='finalAddress'
          :search-input.sync="searchFinal"
          :items="entries"
          :multiple="false"
          clearable
          hide-details
          hide-no-data
          no-data-text="Nenhum resultado"
          hide-selected
          item-text="name"
          placeholder="Para onde vai?"
          class="pt-0 search-address list-addresses"
          return-object
          append-icon=""
          :no-filter="true"
        >
          <div class="prepend" slot="append">
            <v-progress-circular v-if='loadingSearchFinal' indeterminate color="primary" size="24" width="2"></v-progress-circular>
             <v-icon :size="$vuetify.breakpoint.xsOnly ? '22' : '32'" v-else>search</v-icon>
          </div>
          <template v-slot:selection="data">
            <div>
              {{ data.item && data.item.description }}
            </div>
          </template>
          <template v-slot:item="data">
            <div class="destination-name" style="text-align: left;">
              <v-icon class="mr-1" size="20" v-if='data.item && data.item.description'>
                place
              </v-icon>
              {{ data.item && data.item.description }}
            </div>
          </template>
        </v-combobox>
      </div>
    </div>

    <GoogleMapLoader
      style='height: calc(100vh - 59px); position: absolute; top: 59px; left: 0px; width: 100%;'
      :mapConfig="mapConfig"
      :apiKey="MAPS_KEY"
    >
      <template slot-scope="{ google, map }">
        <GoogleMapMarker
          v-for="marker in markers"
          :key="marker.id"
          :marker="marker"
          :google="google"
          :map="map"
        />
      </template>
    </GoogleMapLoader>

    <div class="next-step">
      <v-btn v-if='!finalAddress' disabled class="px-3" flat style="background: #ccc; width: 100%; margin: 0;">
        Selecione o destino final
      </v-btn>
      <v-btn @click="next()" v-else class="px-3" flat color="#fff" style="background: #000; width: 100%; margin: 0;">
        Continuar
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
const MAPS_KEY = process.env.VUE_APP_MAPS_KEY
import { mapSettings } from "@/constants/mapSettings";
import GoogleMapLoader from '@/components/GoogleMapLoader'
import GoogleMapMarker from '@/components/GoogleMapMarker'

export default {
  name: 'Destination',

  data() {
    return {
      places: [],
      searchInitial: null,
      searchFinal: null,

      initialAddress:  {
         "description" : "WeWork - Avenida Almirante Barroso - Centro, RJ, Brasil",
         "id" : "01a9e6bcff0b19868dff379de2cbffcca9cba2a1",
         "matched_substrings" : [
            {
               "length" : 6,
               "offset" : 0
            },
            {
               "length" : 2,
               "offset" : 45
            }
         ],
         "place_id" : "ChIJAQCwCGB_mQARRHR4Fq67g9A",
         "reference" : "ChIJAQCwCGB_mQARRHR4Fq67g9A",
         "structured_formatting" : {
            "main_text" : "WeWork",
            "main_text_matched_substrings" : [
               {
                  "length" : 6,
                  "offset" : 0
               }
            ],
            "secondary_text" : "Avenida Almirante Barroso - Centro, RJ, Brasil",
            "secondary_text_matched_substrings" : [
               {
                  "length" : 2,
                  "offset" : 36
               }
            ]
         },
         "terms" : [
            {
               "offset" : 0,
               "value" : "WeWork"
            },
            {
               "offset" : 9,
               "value" : "Avenida Almirante Barroso"
            },
            {
               "offset" : 37,
               "value" : "Centro"
            },
            {
               "offset" : 45,
               "value" : "RJ"
            },
            {
               "offset" : 49,
               "value" : "Brasil"
            }
         ],
         "types" : [ "real_estate_agency", "establishment" ]
      },
      finalAddress: null,
      loadingSearchInitial: false,
      loadingSearchFinal: false,

      MAPS_KEY: MAPS_KEY,
      markers: [{ position: {
        lat: -22.907364,
        lng: -43.175383
      }, id: "0"}],
      google: null,
      map: null,
      initialPlace: {
        "address_components": [
          {
            "long_name": "81",
            "short_name": "81",
            "types": [
              "street_number"
            ]
          },
          {
            "long_name": "Avenida Almirante Barroso",
            "short_name": "Av. Alm. Barroso",
            "types": [
              "route"
            ]
          },
          {
            "long_name": "Centro",
            "short_name": "Centro",
            "types": [
              "sublocality_level_1",
              "sublocality",
              "political"
            ]
          },
          {
            "long_name": "Rio de Janeiro",
            "short_name": "Rio de Janeiro",
            "types": [
              "administrative_area_level_2",
              "political"
            ]
          },
          {
            "long_name": "Rio de Janeiro",
            "short_name": "RJ",
            "types": [
              "administrative_area_level_1",
              "political"
            ]
          },
          {
            "long_name": "Brasil",
            "short_name": "BR",
            "types": [
              "country",
              "political"
            ]
          },
          {
            "long_name": "20040-060",
            "short_name": "20040-060",
            "types": [
              "postal_code"
            ]
          }
        ],
        "adr_address": "<span class=\"street-address\">Av. Alm. Barroso, 81</span> - <span class=\"extended-address\">Centro</span>, <span class=\"locality\">Rio de Janeiro</span> - <span class=\"region\">RJ</span>, <span class=\"postal-code\">20040-060</span>, <span class=\"country-name\">Brasil</span>",
        "formatted_address": "Av. Alm. Barroso, 81 - Centro, Rio de Janeiro - RJ, 20040-060, Brasil",
        "formatted_phone_number": "(21) 3957-9296",
        "geometry": {
          "location": {
            "lat": -22.907364,
            "lng": -43.175383
          },
          "viewport": {
            "northeast": {
              "lat": -22.90610776970849,
              "lng": -43.1739020697085
            },
            "southwest": {
              "lat": -22.9088057302915,
              "lng": -43.1766000302915
            }
          }
        },
        "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png",
        "id": "01a9e6bcff0b19868dff379de2cbffcca9cba2a1",
        "international_phone_number": "+55 21 3957-9296",
        "name": "WeWork",
        "place_id": "ChIJAQCwCGB_mQARRHR4Fq67g9A",
        "plus_code": {
          "compound_code": "3RVF+3R Rio de Janeiro, RJ, Brasil",
          "global_code": "589R3RVF+3R"
        },
        "rating": 4.8,
        "reference": "ChIJAQCwCGB_mQARRHR4Fq67g9A",
        "scope": "GOOGLE",
        "types": [
          "real_estate_agency",
          "point_of_interest",
          "establishment"
        ],
        "url": "https://maps.google.com/?cid=15025059138213803076",
        "user_ratings_total": 421,
        "utc_offset": -180,
        "vicinity": "Avenida Almirante Barroso, 81, Rio de Janeiro",
        "website": "https://www.wework.com/buildings/almirante-barroso-81--rio-de-janeiro?utm_source=Google&utm_campaign=Organic&utm_medium=Listings"
      },
      finalPlace: null,
    } 
  },
  
  components: {
    GoogleMapLoader,
    GoogleMapMarker,
  },
  created() {

  },

  watch: {
    searchInitial(val) {
      this.loadingSearchInitial = true
      this.searchDebounced(val)
    },

    searchFinal(val) {
      this.loadingSearchFinal = true
      this.searchDebounced(val)
    },

    initialAddress(val, newVal) {
      if(val && val.place_id) {
        this.getInfo(val.place_id, true)
      }
    },

    finalAddress(val, newVal) {
      if(val && val.place_id) {
        this.getInfo(val.place_id)
      }
    }
  },

  computed: {
    entries() {
      return ([]).concat(this.places)
    },

    mapConfig() {
      return {
        ...mapSettings,
        center: this.mapCenter
      };
    },

    mapCenter() {
      if(!this.markers || !this.markers.length) {
        return { lat: -22.907364, lng: -43.1775717 }
      }

      return this.markers[0] && this.markers[0].position
    },
  },

  props: {
    driver: {
      type: Object
    }
  },

  methods: {
    searchDebounced: _.debounce(async function (newVal) {
      this.searchAddresses(newVal)
    }, 500, {leading: false, trailing: true}),

    async getInfo(place_id, initial = false) {
      try {
        let res = await GoogleMaps.getInfo(place_id)

        this.markers.push({ position: res.data.result.geometry.location, id: Math.random() })
        if(initial) {
          this.initialPlace = res.data.result 
        } else {
          this.finalPlace = res.data.result 
        }
      } catch(err) {

        this.$message({
          type: 'error',
          message: ErrorMessage(err),
        }) 
      }
    },

    async searchAddresses(q) {
      try {
        let res = await GoogleMaps.search(q)

        this.loadingSearchFinal = false
        this.loadingSearchInitial = false
        this.places = res.data.predictions
      } catch(err) {
        this.loadingSearchFinal = false
        this.loadingSearchInitial = false
        this.$message({
          type: 'error',
          message: ErrorMessage(err),
        }) 
      }
    },

    next() {
      this.$router.push({
        name: 'schedules',
        params: {
          driver: this.driver,
          initialPlace: this.initialPlace,
          finalPlace: this.finalPlace
        }
      })
    }
  },
}
</script>

<style scoped>
.topbar {
  display: flex;
  margin-top: 28px;
  flex-wrap: wrap;
  position: absolute;
  z-index: 1;
}
.bullets {
  margin-left: 24px;
}
.initial-address {
  width: 100%;
  margin-left: 18px;
  margin-right: 18px;
}
.destination-name {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
}
.next-step {
  position: absolute;
  bottom: 24px;
  height: 50px;
  width: 100%;
  padding-left: 24px;
  padding-right: 24px;

}
</style>
