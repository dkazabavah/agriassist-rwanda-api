function askAI(){

let question =
document.getElementById("question").value.toLowerCase();


let answer="";


if(question.includes("maize")){
answer="Maize grows well during rainy seasons. Monitor pests regularly.";
}

else if(question.includes("disease")){
answer="Remove infected crops and check leaf symptoms early.";
}

else{

answer="Check weather, soil and market prices before planting.";

}


document.getElementById("answer").innerHTML =
"<p>🤖 AI: "+answer+"</p>";

}
