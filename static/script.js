async function searchCrop(){

    const crop = document.getElementById("cropSearch").value;

    const response = await fetch(`/api/crops?search=${crop}`);

    const data = await response.json();


    let output = "";

    data.forEach(item => {

        output += `
        <div class="card">

        <h3>${item.name}</h3>

        Season: ${item.season}<br>
        Water: ${item.water}<br>
        Soil: ${item.soil}<br>
        Region: ${item.region}

        </div>
        `;

    });


    document.getElementById("cropResults").innerHTML = output;

}



async function getWeather(){

    const city = document.getElementById("city").value;


    const response = await fetch(`/api/weather?city=${city}`);

    const data = await response.json();


    document.getElementById("weatherResult").innerHTML = `

    <div class="card">

    <h3>${data.city}</h3>

    Temperature: ${data.temperature} °C <br>

    Humidity: ${data.humidity}% <br>

    Condition: ${data.condition}

    </div>

    `;

}
