document.addEventListener("DOMContentLoaded", function(){

const ctx = document.getElementById("marketChart");


if(ctx){

new Chart(ctx, {

type:"bar",

data:{

labels:[
"Maize",
"Beans",
"Rice",
"Potatoes"
],

datasets:[{

label:"Price RWF/kg",

data:[
600,
850,
1200,
500
]

}]

}

});

}

});
const ctx=document.getElementById("marketChart");


new Chart(ctx,{

type:"line",

data:{


labels:[
"Jan",
"Feb",
"Mar",
"Apr",
"May"
],


datasets:[{

label:"Maize Price",

data:[
300,
350,
400,
380,
450
]

}]

}


});
