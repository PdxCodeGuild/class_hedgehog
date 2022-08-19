const currentWeather = document.querySelector("#weather");

let position = navigator.geolocation.getCurrentPosition(position => {
        console.log("Latitude: " + position.coords.latitude);
        console.log("Longitude: " + position.coords.longitude);
        fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${position.coords.latitude}&lon=${position.coords.longitude}&exclude=hourly,daily&appid=${AnthonyKey}`).then(response => response.json()).then(data => displayWeather(data)).catch(err => console.error(err));
    });

function displayWeather(data) {
    console.log(data);
    let img = document.createElement('img');
    img.src = `http://openweathermap.org/img/wn/${data.current.weather[0].icon}.png`;
    let time = document.createElement("div");
    time.innerText = new Date(data.current.dt*1000);
    let description = document.createElement("div");
    description.innerText = data.current.weather[0].description;
    currentWeather.append(time, img, description);
};

// async function getWeather() {
//     try {
//     let response = await fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=37&lon=100&exclude=hourly,daily&appid=${AnthonyKey}`); // console.log(response);
//     let data = await response.json(); // console.log(data);
//     let unixTimeStamp = data.current.dt; // console.log(unixTimeStamp);
//     let datetime = new Date(unixTimeStamp*1000); // console.log(datetime);
//     let icon = data.current.weather[0].icon; // console.log(weatherIcon);
//     let weatherDescription = data.current.weather[0].description; // console.log(description);
//     let img = document.createElement('img');
//     img.src = `http://openweathermap.org/img/wn/${icon}.png`;
//     let time = document.createElement("div");
//     time.innerText = datetime;
//     let description = document.createElement("div");
//     description.innerText = weatherDescription;
//     currentWeather.append(time, img, description);
//     return data;
//     } catch (err) {
//         console.log(err)
//     };
//     console.log(data);
// };

// let data = getWeather().then((data) => console.log(data));