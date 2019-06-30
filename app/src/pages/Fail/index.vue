<template>
  <div class="fail">
    <v-layout class="mx-4 mt-4" wrap style="align-items: center; flex: none;">
      <v-flex xs6 lg4 md4>
        <img src="@/assets/logo.png" />
      </v-flex>

      <v-flex></v-flex>

      <v-flex xs2 lg2 md2>
        <img src="@/assets/govbr.png" />
      </v-flex>
    </v-layout> 
    <v-flex></v-flex>

    <div>
      <img src="@/assets/fail.png" width="200" />
    </div>

    <div class="first-text">
      Este municipio ainda não utiliza o empreenda.aqui 😭
    </div>

    <div class="other-text">
      Solicite que <b style="color: #6500F0;">{{address.vicinity }}</b> utilize a plataforma
    </div>

    <div>
      <v-btn @click="request()" flat style="width: 182px; height: 56px; background-color: #6500F0; color: #fff;">
        EU QUERO
      </v-btn><br />
      <v-btn flat @click="$router.go(-1)">VOLTAR</v-btn>
    </div>

    <v-flex></v-flex>

    <div class="brasilia">
      <img src="@/assets/brasilia.jpg" />
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import ErrorMessage from '@/helpers/ErrorMessage'

export default {
  name: 'Fail',

  props: {
    address: {
      type: Object
    },
  },

  methods: {
    async request() {
      try {
        await Axios.get('https://cors-anywhere.herokuapp.com/https://script.google.com/macros/s/AKfycbwzZiRvzD3wYwPncZHbhC3ktc5casFsGYoctAYV0tuD5NjPBS61/exec?action=insert&address='+this.address.formatted_address)

        this.$notify({
          type: 'success',
          message: 'Deu certo, em breve o Empreenda Aqui estará na sua cidade :)',
        }) 
      } catch(err) {
        this.$message({
          type: 'error',
          message: ErrorMessage(err),
        }) 
      }
    }
  }
}
</script>

<style>
.first-text {
  font-size: 42px;
  margin-bottom: 16px;
}
.other-text {
  font-size: 32px;
  margin-bottom: 24px;
}
@media (max-width: 901px) {
  .fail {
    max-height: 100vh; overflow: hidden;
  }
}
@media (max-width: 600px) {
  .fail {
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
</style>