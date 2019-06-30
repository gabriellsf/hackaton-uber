<template>
  <div class="cnae">
    <v-layout class="mx-4 mt-4" wrap style="align-items: center;">
      <v-flex xs6 lg2 md2>
        <img src="@/assets/logo.png" />
      </v-flex>

      <v-flex></v-flex>

      <v-flex xs2 lg1 md1>
        <img src="@/assets/govbr.png" />
      </v-flex>
    </v-layout> 
    <v-layout wrap style="justify-content: center;"> 
      <div class="text-xs-center mt-3 main-text" style="font-family: Roboto; width: 100%">
        Esse é o último passo :)
      </div>

      <div class="mt-5 second-text" style="font-family: Roboto; width: 100%">
        Quais atividades sua empresa vai exercer?
      </div>

      <v-container grid-list-xs text-xs-center style="max-width: 800px;">
        <v-layout row align-center class="white elevation-1 search-area pl-3 mr-0" style="min-height: 56px" :class="$vuetify.breakpoint.xsOnly ? 'pr-0' : 'pr-4'">
          <v-combobox
            v-model='targetCNAEs'
            :items="entries"
            :search-input.sync="search"
            :multiple="true"
            chips
            deletable-chips
            hide-details
            hide-no-data
            no-data-text="Nenhum resultado"
            placeholder="Ex: Restaurante, pousada, escola ..."
            class="pt-0 search-address search-cnae"
            return-object
            item-text="description"
            append-icon="chevron-down"
            :no-filter="true"
          >
            <div class="prepend" slot="prepend">
              <v-progress-circular v-if='loading' indeterminate color="primary" size="24" width="2"></v-progress-circular>
              <v-icon :size="$vuetify.breakpoint.xsOnly ? '28' : '32'" v-else>search</v-icon>
            </div>
          </v-combobox>
        </v-layout>
        <div class="info-text">Você pode pesquisar por atividade e nós encontraremos o CNAE referente</div>
      </v-container>
    </v-layout>

    <v-flex></v-flex>

    <div>
      <v-btn @click="$router.push({ name: 'zones', params: { address: address, cnaes: targetCNAEs } })" class="query-button" flat style="width: 182px; height: 56px; color: #fff;" :disabled="!targetCNAEs.length">
        CONSULTAR
      </v-btn><br />
      <v-btn flat @click="$router.go(-1)">VOLTAR</v-btn>
    </div>
    <div class="brasilia">
      <img src="@/assets/brasilia.jpg" />
    </div>
  </div>
</template>
<script type="text/javascript">
import _ from 'lodash'
import ErrorMessage from '@/helpers/ErrorMessage'
import CNAEs from '@/pages/CNAE/CNAEs.json'

export default {
  name: 'CNAE',

  data() {
    return {
      search: null,
      loading: false,
      targetCNAEs: [], 

      items: [],
    }
  },

  props: {
    address: {
      type: Object
    }
  },

  watch: {
    search (val) {
      val && val !== this.select && this.querySelections(val)
    }
  },

  computed: {
    entries() {
      // return this.items
      return ([]).concat(this.items)
    },
  },

  methods: {
    iconForTarget(sector) {
      return {
        'Agronegócio': 'mdi-account',
        'Serviços'   : 'mdi-book-multiple',
        'Indústria'  : 'mdi-book-multiple',
        'Comércio'   : 'mdi-book-multiple',
      }[sector]
    },

   querySelections (v) {
      this.loading = true

      setTimeout(() => {
        this.items = CNAEs.filter(e => {
          return (e.description || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loading = false
      }, 100)
    },

    advance() {
      if(!this.address || !this.address.place_id) return
      this.loading = true

      this.checkAddress(this.address.place_id)
    }
  }
}
</script>

<style scoped>
.main-text {
  font-size: 42px;
  max-width: 900px;
  margin-left: 12px;
  margin-right: 12px;
}
.second-text {
  font-size: 32px;
}
.info-text {
  color: #999595;
  font-size: 14px;
  font-family: Roboto;
  margin-top: 12px;
  text-align: left;
}
@media (max-width: 600px) {
  .main-text {
    font-size: 22px;
    margin-top: 32px!important;
  }
  .second-text {
    font-size: 18px;
    margin-top: 0px!important;
  }
  .home {
    min-height: 100vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
}
@media (max-width: 900px) {
  .brasilia {
    width: 130%;
    margin-left: -15%;
    background-size: cover;
  }
  .brasilia > img {
    margin-bottom: -10px;
  }
}
@media (max-width: 901px) {
  .cnae {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
}


</style>