// const weatherEl = document.getElementById("weather-el")

const temp = document.getElementById("temp")
const sunrise = document.getElementById("sunrise")
const sunset = document.getElementById("sunset")
const icon = document.getElementById("icon")
const descriptionEl = document.getElementById("description-el")

navigator.geolocation.getCurrentPosition(position => {
  let lat = position.coords.latitude
  let long = position.coords.longitude
    fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}&exclude=hourly,daily,minutely&appid=${apiKey}&units=imperial`)
    .then((response) => response.json())  
    .then((data) => {
        temp.innerHTML = data.current.temp.toFixed() + "&deg;F"
        let sunriseTimestamp = new Date(data.current.sunrise*1000)
        sunrise.textContent = `Sunrise: ${sunriseTimestamp.getHours()}:${sunriseTimestamp.getMinutes()} AM`
        let sunsetTimestamp = new Date(data.current.sunset*1000)
        sunset.textContent = `Sunset: ${sunsetTimestamp.getHours()-12}:${sunsetTimestamp.getMinutes()} PM`
        descriptionEl.textContent = data.current.weather[0].description
        icon.src = `http://openweathermap.org/img/wn/${data.current.weather[0].icon}.png`
       
    })

})



