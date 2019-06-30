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

    <div class="title-pattern">
      Planeje sua rota
    </div>

    <div class="mt-3 mx-3" v-for='(date, i) in daysSelected' style="text-align: left;">
      <v-select
        v-model='date.day'
        :items="daysOfWeek"
        label="Dia da semana"
        solo
        hide-details
      ></v-select>

      <div style="display: flex;">
        <v-text-field
          label="Horário de início"
          v-model='date.initialHour'
          style="width: 40%; margin-top: 12px; margin-right: 5%;"
        ></v-text-field>

        <v-text-field
          label="Horário de início"
          v-model='date.finalHour'
          style="width: 40%; margin-top: 12px;"
        ></v-text-field>

      </div>
      <v-btn @click="add()" class="ma-0 pa-0" flat color="blue" v-if='i == daysSelected.length - 1'>
        <v-icon>add</v-icon>
        Adicionar
      </v-btn>
    </div>

    <div class="my-5 px-3">
      <v-btn @click="calculate()" class="px-3" flat color="#fff" style="background: #000; width: 100%; margin: 0">
        Calcular o preço
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
  name: 'Schedules',

  data() {
    return {
      daysOfWeek: ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'],

      daysSelected: [{
        day: 'Domingo',
        initialHour: '08:00',
        finalHour: '12:00'
      }]
    }
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
    }
  },

  created() {

  },

  methods: {
    calculate() {
      this.$router.push({
        name: 'estimate-price',
        params: {
          driver: this.driver,
          initialPlace: this.initialPlace,
          finalPlace: this.finalPlace,
          daysSelected: this.daysSelected,
        }
      })
    },

    add() {
      this.daysSelected.push({
        day: 'Domingo',
      })
    }
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
</style>
