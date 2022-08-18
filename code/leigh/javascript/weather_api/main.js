const current = document.querySelector("#current")

navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude)
    console.log(position.coords.longitude)
    
    fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${position.coords.latitude}&lon=${position.coords.longitude}& exclude=hourly,daily&appid=${weatherKey}`)
    .then(response => response.json())
    .then(data => postWeather(data))
})

function postWeather(data) {
    console.log(data)
    const dt = document.createElement("div")
    let unix_timestamp = data.current.dt
    let dateTime = new Date(unix_timestamp*1000)
    dt.textContent = `Time: ${dateTime}`
    current.appendChild(dt)

    const icon = document.createElement("img")
    icon.src = `http://openweathermap.org/img/wn/${data.current.weather[0].icon}.png`
    current.appendChild(icon)

    const cloudsDiv = document.createElement("div")
    cloudsDiv.textContent = `Clouds: ${data.current.weather[0].description} ${data.current.clouds}%`
    current.appendChild(cloudsDiv)

    const humidity = document.createElement("div")
    humidity.textContent = `Humidity: ${data.current.humidity}%`
    current.appendChild(humidity)

    const temp = document.createElement("div")
    temp.textContent = `Temperature: ${data.current.temp}`
    current.appendChild(temp)

    const uvi = document.createElement("div")
    uvi.textContent = `Uvi: ${data.current.uvi}`
    current.appendChild(uvi)

    const pressure = document.createElement("div")
    pressure.textContent = `Pressure: ${data.current.pressure}`
    current.appendChild(pressure)

    const wind_deg = document.createElement("div")
    wind_deg.textContent = `Wind Deg.: ${data.current.wind_deg}`
    current.appendChild(wind_deg)

    const wind_gust = document.createElement("div")
    wind_gust.textContent = `Wind Gust.: ${data.current.wind_gust}`
    current.appendChild(wind_gust)

    const wind_speed = document.createElement("div")
    wind_speed.textContent = `Wind Speed: ${data.current.wind_speed}`
    current.appendChild(wind_speed)

    const dewPointDiv = document.createElement("div")
    dewPointDiv.textContent = `Dew Point: ${data.current.dew_point}`
    current.appendChild(dewPointDiv)

    const feelsLike = document.createElement("div")
    feelsLike.textContent = `Feels Like: ${data.current.feels_like}`
    current.appendChild(feelsLike)
    
    const sunrise = document.createElement("div")
    unix_timestamp = data.current.sunrise
    dateTime = new Date(unix_timestamp*1000)
    sunrise.textContent = `Time: ${dateTime}`
    current.appendChild(sunrise)

    const sunset = document.createElement("div")
    unix_timestamp = data.current.sunset
    dateTime = new Date(unix_timestamp*1000)
    sunset.textContent = `Time: ${dateTime}`
    current.appendChild(sunset)

    const visibility = document.createElement("div")
    visibility.textContent = `Visibility: ${data.current.visibility}`
    current.appendChild(visibility)
}