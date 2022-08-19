const current = document.querySelector("#current")
const submitBtn = document.querySelector("#submit-btn")

// function getLatLong(){
//     navigator.geolocation.getCurrentPosition(position => {
//         console.log(position.coords.latitude)
//         console.log(position.coords.longitude)
//     })

// }

// submitBtn.addEventListener("click", function() {
//     fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689& exclude=hourly,daily&appid=${apiKey}`)
//     .then(response => response.json())
//     .then(data => currentWeather(data))

// .catch(err => alert("It's broken!"))
// })

submitBtn.addEventListener("click", () => {
    let lat;
    let long;
    
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(position => {
            lat = position.coords.latitude
            long = position.coords.longitude
            
            fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${long}& exclude=hourly,daily&appid=${apiKey}`)
            .then(response => response.json())
            .then(data => currentWeather(data))
            
            .catch(err => alert("It's broken!"))
            
        })
    }
    
})


function currentWeather(data) {
    console.log(data)
    const date = document.createElement("div")
    let unix_timestamp = data.current.dt
    let dateTime = new Date(unix_timestamp*1000)
    date.textContent = `Today's Date: ${dateTime}`
    current.appendChild(date)
    
    const icon = document.createElement("img")
    icon.src = `http://openweathermap.org/img/wn/${data.current.weather[0].icon}.png`
    current.appendChild(icon)
    
    const desc = document.createElement("div")
    desc.textContent = `Weather: ${data.current.weather[0].description}`
    current.appendChild(desc)
    
    const temp = document.createElement("div")
    const tempature = Math.round(1.8*(data.current.temp-273)+32)
    temp.textContent = `🌶️Tempature: ${tempature}°F`
    current.appendChild(temp)
    
    const feels = document.createElement("div")
    const feelsLike = Math.round(1.8*(data.current.feels_like-273)+32)
    feels.textContent = `Feels like: ${feelsLike}°F`
    current.appendChild(feels)
    
    const humidity = document.createElement("div")
    humidity.textContent = `🥵Humidity: ${data.current.humidity}%`
    current.appendChild(humidity)
    
    const clouds = document.createElement("div")
    clouds.textContent = `☁️Clouds: ${data.current.clouds}%`
    current.appendChild(clouds)
    
    const uvi = document.createElement("div")
    uvi.textContent = `☀️UVI: ${data.current.uvi}`
    current.appendChild(uvi)
    
    const winds = document.createElement("div")
    winds.textContent = `💨Wind speed: ${data.current.wind_speed}`
    current.appendChild(winds)
}