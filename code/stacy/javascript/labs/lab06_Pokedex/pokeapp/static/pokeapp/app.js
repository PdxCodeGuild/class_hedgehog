

const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            // variables go here
            message: "It works!",
            pokemon: [],
            searchTerm: "",
            page: 1,
            maxPage: 0,
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
        previousPage: function(){
            if (this.page === 1) {
                pass
            } else {
                this.page -= 1
                fetch(`/pokemon/?page=${this.page}`)
                .then(response => response.json())
                .then(data => {
                console.log(data.data, "hello")
                this.pokemon = data.data
                })
            }
        },
        nextPage: function(){
            if (this.page >= this.maxPage) {
                pass
            } else {
                this.page += 1
                fetch(`/pokemon/?page=${this.page}`)
                .then(response => response.json())
                .then(data => {
                console.log(data.data, "hello")
                this.pokemon = data.data
                })
            }
        },
    },
    watch: {
        // onchange functions go here, tied to variables in data
        
    },
    created: function() {
        // what happens when app is created?
        fetch(`/pokemon/?page=${this.page}`)
        .then(response => response.json())
        .then(data => {
            console.log(data.data, "hello")
            this.pokemon = data.data
            this.maxPage = data.data[this.pokemon.length -1]
            console.log(this.maxPage)
        })
    },
    mounted: function() {
        // what happens when app is mounted

    }
}).mount("#app")


