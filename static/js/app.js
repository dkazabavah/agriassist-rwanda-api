async function loadDashboard(){

    const weather = await fetch("/api/weather?city=Kigali")
    const weatherData = await weather.json()


    document.getElementById("weather").innerHTML =
    `
    ${weatherData.city}<br>
    ${weatherData.temperature}°C<br>
    ${weatherData.condition}
    `



    const tips = await fetch("/api/tips")
    const tipsData = await tips.json()

    document.getElementById("tips").innerHTML =
    tipsData[0]?.tip || "No tips available"



    const diseases = await fetch("/api/diseases")
    const diseaseData = await diseases.json()

    document.getElementById("diseases").innerHTML =
    diseaseData[0]?.name || "No diseases"



    const markets = await fetch("/api/markets")
    const marketData = await markets.json()

    document.getElementById("markets").innerHTML =
    `${marketData[0]?.crop}: ${marketData[0]?.price} RWF`



    const calendar = await fetch("/api/calendar")
    const calendarData = await calendar.json()


    let rows=""

    calendarData.forEach(item=>{

        rows += `
        <tr>
        <td>${item.crop}</td>
        <td>${item.planting_season}</td>
        <td>${item.harvesting_period}</td>
        <td>${item.region}</td>
        </tr>
        `

    })


    document.getElementById("calendar").innerHTML = rows

}

function askAI(){

let q=document.getElementById("question").value;


let answer="";


if(q.toLowerCase().includes("maize")){

answer="Plant maize during rainy seasons. Use fertilizer and monitor fall armyworm.";

}

else if(q.toLowerCase().includes("fertilizer")){

answer="Use compost manure and balanced NPK fertilizer.";

}

else{

answer="AI recommendation: Maintain soil health, monitor weather and track crops.";

}


document.getElementById("answer").innerHTML=answer;

}




fetch("/api/tips")
.then(res=>res.json())
.then(data=>{

document.getElementById("tips").innerHTML=
JSON.stringify(data);

});



fetch("/api/markets")
.then(res=>res.json())
.then(data=>{

document.getElementById("markets").innerHTML=
JSON.stringify(data);

});

loadDashboard()
