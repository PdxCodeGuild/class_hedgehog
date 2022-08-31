const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            pokemon: [],
            search: '',
        }
    },
    methods: {
        fetchPokemon: function(search) {
            fetch(`./pokemon/${this.search}`)
            .then(response => response.json())
            .then(data => {
                this.pokemon = data.poke
            })
        }
    },
    
    created: function() {
        fetch('./pokemon')
        .then(response => response.json())
        .then(data => {
            this.pokemon = data.poke
        })
    },
    mounted: function () {

    }
    
}).mount("#app")