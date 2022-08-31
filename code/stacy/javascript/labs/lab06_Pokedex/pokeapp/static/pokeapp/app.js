

const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            // variables go here
            message: "It works!",
            pokemon: [],
            searchTerm: ""
        }
    },
    methods: {
        // functions go here
        pokeSearch: function(searchTerm) {
            fetch(`/pokemon/?searchTerm=${searchTerm}`)
            .then(response => response.json())
            .then(data => {
                this.pokemon = data.data
            })
        },

    },
    watch: {
        // onchange functions go here, tied to variables in data
        pokemon: function() {

        },
    },
    created: function() {
        // what happens when app is created?
        fetch("/pokemon/")
        .then(response => response.json())
        .then(data => {
            // console.log(data)
            this.pokemon = data.data
        })
    },
    mounted: function() {
        // what happens when app is mounted?

    }
}).mount("#app")