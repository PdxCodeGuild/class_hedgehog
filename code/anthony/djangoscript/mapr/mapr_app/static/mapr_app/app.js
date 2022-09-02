const app = Vue.createApp({
  delimiters: ['[[', ']]'],
  data() {
    return {
      message: "Hello from Vue",
      groups: [],
      selectedGroup: null,
      locations: [],
      map: null,
      layerGroup: null,
    }
  },
  methods: {
    fetchLocations: function() {
      fetch(`/api/groups/${this.selectedGroup}`)
      .then(response => response.json())
      .then(data => {
        this.locations = data.data
      })
    },
    configMap: function() {
      this.layerGroup = L.layerGroup()
      this.layerGroup.addTo(this.map)

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(this.map);
    }
  },
  watch: {
    locations: function(locations){
      this.layerGroup.clearLayers()
      for(let user of locations){
        this.layerGroup.addLayer(
          L.marker([user.location__latitude, user.location__longitude])
          .bindPopup(user.username)
          .openPopup()
        )
      }
    }
  },
  // Called when the app is created
  created: function(){
    fetch("/api/groups")
    .then(response => response.json())
    .then(data => {
      this.groups = data.data
    })
  },
  // Called when app is mounted to the DOM
  mounted: function () {
    navigator.geolocation.getCurrentPosition(position => {
      this.map = L.map('map')
      .setView([position.coords.latitude, position.coords.longitude], 5)
      this.configMap()
    }, err => {
      this.map = L.map('map')
      .setView([0,0], 3)
      this.configMap()
      console.error(err)
    })
  }
}).mount("#app")
