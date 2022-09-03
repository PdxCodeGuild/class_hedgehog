const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            pokemon: [],
            search: '',
            page: 1,
            limit: 20,
        }
    },
    methods: {
        fetchPokemon: function() {
            fetch(`./pokemon/${this.search}`)
            .then(response => response.json())
            .then(data => {
                // console.log(data) check to see what the data is returning if nothing is
                this.pokemon = data.poke
            })
        },
        backPage: function() {

        },
        nextPage: function() {

        }
    },
    
    created: function() {
        fetch(`./pokemon`)
        .then(response => response.json())
        .then(data => {
            this.pokemon = data.poke
        })
    },
    mounted: function () {

    }
    
}).mount("#app")