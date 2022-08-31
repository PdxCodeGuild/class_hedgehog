const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            search: "",
            pokemons: [],
            selectedGroup: null,
            page: 1,
            limit: 20
        }
    },
    methods: {
        searchPokemon: function() {
            fetch(`searchPokemon/${this.search}`)
            .then(response => response.json())
            .then(data => {
                this.pokemons = data.data
            })
        },
        backPage: function() {
            if (this.page > 1) {
                this.page--
            }
            this.collectPokemon()
        },
        forwardPage: function() {
            if (this.page < 8) {
                this.page++
            }
            this.collectPokemon()
        },
        collectPokemon: function() {
            fetch(`/pokemon/${this.page}/${this.limit}`)
            .then(response => response.json())
            .then(data => {
                this.pokemons = data.data
            })
        }
    },
    created: function() {
        this.collectPokemon()
    }
}).mount("#app")

