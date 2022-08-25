const temp = document.querySelector("#temp")
const sunrise = document.querySelector("#sunrise")
const sunset = document.querySelector("#sunset")
const icon = document.querySelector("#icon")
const weatherDescription = document.querySelector("#weather-description")

navigator.geolocation.getCurrentPosition(position => {
    lat = position.coords.latitude
    long = position.coords.longitude

    fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}& exclude=minutely,hourly,daily&appid=${apiKey}&units=imperial`)
    .then(response => response.json())
    // .then(data => console.log(data))
    .then(data => {
        temp.innerHTML = data.current.temp.toFixed() + "&deg;F"
        let  sunriseTimestamp = new Date(data.current.sunrise * 1000)
        sunrise.textContent = `Sunrise: ${sunriseTimestamp.getHours()}:${sunriseTimestamp.getMinutes()}am`
        let sunsetTimestamp = new Date(data.current.sunset * 1000)
        sunset.textContent = `Sunset: ${sunsetTimestamp.getHours()-12}:${sunsetTimestamp.getMinutes()}pm`
        icon.classList.add(`owf-${data.current.weather[0].id}`)
        weatherDescription.textContent = data.current.weather[0].description
    })
})

// function weather(data) {
//     console.log(data)
// }