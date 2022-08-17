
# Dad Joke API

Use the [Dad Joke API](https://icanhazdadjoke.com/api) to get a dad joke and display it to the user.


## Part 1

Use fetch or axios to send an HTTP request to `https://icanhazdadjoke.com/` with the `accept` header as `application/json`. This will return a dad joke in JSON format. You can then use the `.json()` method on the response to get a javascript object. Get the joke out of the object and show it to the user.

```Javascript
fetch("https://icanhazdadjoke.com/", {
  headers: {
    accept: "application/json"
  }
}).then(response => response.json())
.then(data => console.log(data))
```


## Part 2 

Add the ability to "search" for jokes using [another endpoint](https://icanhazdadjoke.com/api#search-for-dad-jokes).

## Part 3

Add some styling! Flex your css skills.
