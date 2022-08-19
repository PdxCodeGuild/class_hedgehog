const current = document.querySelector('#current')

const choices = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]

navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude)
    console.log(position.coords.longitude)
    fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&units=imperial&exclude=hourly,daily&appid=${appid}`, {
        headers: {
          accept: "application/json"
        }
      }).then(response => response.json())
      .then(data => weather(data))
      .catch(err => console.error(err))
})


function weather(data){
    const date = document.createElement('li')
    unix_timestamp = data.current.dt
    datetime = new Date(unix_timestamp*1000)
    date.textContent = `Date: ${datetime}`
    current.appendChild(date)
    
    const weatherIcon = document.createElement('img')
    weatherIcon.src = `http://openweathermap.org/img/wn/${data.current.weather[0].icon}.png`
    current.appendChild(weatherIcon)
    
    const weatherDesc = document.createElement('li')
    weatherDesc.textContent = `Weather: ${data.current.weather[0].description}`
    current.appendChild(weatherDesc)

    const temp =document.createElement('li')
    temp.textContent = `Temp: ${data.current.temp}°F`
    current.appendChild(temp)

    const feelsLike = document.createElement('li')
    feelsLike.textContent = `Feels like: ${data.current.feels_like}°F`
    current.appendChild(feelsLike)

    const pressure = document.createElement('li')
    pressure.textContent = `Pressure: ${data.current.pressure} hPa`
    current.appendChild(pressure)

    const humidity = document.createElement('li')
    humidity.textContent = `Humidity: ${data.current.humidity}%`
    current.appendChild(humidity)

    const dewPoint = document.createElement('li')
    dewPoint.textContent = `Dew Point: ${data.current.dew_point}°F`
    current.appendChild(dewPoint)

    const cloudCover = document.createElement('li')
    cloudCover.textContent = `Cloud Cover: ${data.current.clouds}%`
    current.appendChild(cloudCover)

    const uvi = document.createElement('li')
    uvi.textContent = `Uvi: ${data.current.uvi}`
    current.appendChild(uvi)

    const visibility = document.createElement('li')
    visibility.textContent = `Visibility: ${data.current.visibility} m`
    current.appendChild(visibility)

    const windSpeed = document.createElement('li')
    windSpeed.textContent = `Wind Speed: ${data.current.wind_speed} mph`
    current.appendChild(windSpeed)
    
    const gusts = document.createElement('li')
    gusts.textContent = `Gusts: ${data.current.wind_gust} mph`
    current.appendChild(gusts)

    const windDir = document.createElement('li')
    i = Math.round(data.current.wind_deg/22.5)
    windComp = choices[i]
    windDir.textContent = `Wind Direction: ${windComp}`
    current.appendChild(windDir)

    const sunrise = document.createElement('li')
    unix_timestamp = data.current.sunrise
    datetime = new Date(unix_timestamp*1000)
    sunrise.textContent = `Sunrise: ${datetime}`
    current.appendChild(sunrise)

    const sunset = document.createElement('li')
    unix_timestamp = data.current.sunset
    datetime = new Date(unix_timestamp*1000)
    sunset.textContent = `Sunset: ${datetime}`
    current.appendChild(sunset)

}    


