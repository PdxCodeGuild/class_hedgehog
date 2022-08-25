const temp = document.querySelector("#temp")
const sunrise = document.querySelector("#sunrise")
const sunset = document.querySelector("#sunset")
const icon = document.querySelector("#icon")
const image = document.querySelector("#image")
const weatherDescription = document.querySelector("#weather-description")


navigator.geolocation.getCurrentPosition((position) => {
  lat = position.coords.latitude
  long = position.coords.longitude
  fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&exclude=minutely,hourly,daily&appid=${api_key}&units=imperial`)
  .then(response => response.json())
  .then(data => {
    temp.innerHTML = data.current.temp.toFixed() + "&deg;F"
    let sunriseTimestamp = new Date(data.current.sunrise * 1000)
    sunrise.textContent = `Sunrise: ${sunriseTimestamp.getHours()}:${sunriseTimestamp.getMinutes()}am`
    let sunsetTimestamp = new Date(data.current.sunset * 1000)
    sunset.textContent = `Sunset: ${sunriseTimestamp.getHours()}:${sunsetTimestamp.getMinutes()}pm`

    // with icon
    icon.classList.add(`owf-${data.current.weather[0].id}-n`)

    // with image
    image.src = `http://openweathermap.org/img/wn/${data.current.weather[0].icon}.png`
    image.alt = data.current.weather[0].description

    weatherDescription.textContent = data.current.weather[0].description
  })
})

// String(sunriseTimestamp.getMinutes()).padStart(2, "0")
// image.src = `http://openweathermap.org/img/wn/${data.current.weather[0].icon}.png`


// navigator.geolocation.getCurrentPosition((position) => {
//   lat = position.coords.latitude
//   long = position.coords.longitude
//   fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&exclude=hourly,daily&appid=${api_key}`)
//   .then(function (response){
//     return response.json()
//   }).then(function (data) {
//    console.log(data)
//   })
// })



// Arrow function
// const doSomething = () => {
// }
