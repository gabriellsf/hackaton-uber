import Axios from 'axios'
import Vue from 'vue'
const MAPS_KEY = process.env.VUE_APP_MAPS_KEY

class GoogleMaps {
  constructor(){}

  async search(q) {
    return await Axios.get('https://cors-anywhere.herokuapp.com/https://maps.googleapis.com/maps/api/place/autocomplete/json?components=country:br&language=pt_BR&&key=' + MAPS_KEY + '&input=' + q)
  }

  async getInfo(id) {
    return await Axios.get('https://cors-anywhere.herokuapp.com/https://maps.googleapis.com/maps/api/place/details/json?language=pt_BR&key=' + MAPS_KEY + '&placeid=' + id)
  }

}

export default (new GoogleMaps)