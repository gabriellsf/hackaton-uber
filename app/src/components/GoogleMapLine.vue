<script>
import { LINE_PATH_CONFIG } from "@/constants/mapSettings";
import inside from 'point-in-polygon'

export default {
  props: {
    google: {
      type: Object,
      required: true
    },
    map: {
      type: Object,
      required: true
    },
    path: {
      type: Array,
      required: true
    },
    lineId: {},
    strokeColor: { },
    strokeOpacity: { },
    strokeWeight: { },
    fillColor: { },
    fillOpacity: { },
    markers: {}
  },

  mounted() {
    const { Polyline } = this.google.maps;
    new Polyline({
      path: this.path,
      strokeColor: this.strokeColor,
      strokeOpacity: this.strokeOpacity,
      strokeWeight: this.strokeWeight,
      fillColor: this.fillColor,
      fillOpacity: this.fillOpacity,
      map: this.map,
      ...LINE_PATH_CONFIG
    });
  },

  created() {
    if(this.markers && this.markers.length){
            //normalize path

      let normalizedPath = []

      this.path.map((point) => {
        normalizedPath.push(point)
      })

      let normalizedMarkers = []

      this.markers.map((mark) => {
        normalizedMarkers.push(mark.position)
      })

      let marker

      var polygon = new this.google.maps.Polygon({paths: normalizedPath})

      var point = new this.google.maps.LatLng(normalizedMarkers[0].lat, normalizedMarkers[0].lng)

      let markersStatus = this.google.maps.geometry.poly.containsLocation(point, polygon)

      if(markersStatus) {
        marker = Object.assign({
          status: 'approved',
          lineId: this.lineId,
        }, this.markers[0])
        this.$emit('updateZones', marker)
        return 
      }
      marker = Object.assign({
        status: 'reproved',
        lineId: this.lineId,
      }, this.markers[0])
      this.$emit('updateZones', marker)
      return
    }
  },

  render() {},
};
</script>
