kfunction searchDisease(){

let search =
document.getElementById("diseaseSearch").value.toLowerCase();


let diseases={

"maize":"Fall armyworm - inspect leaves and use proper treatment",

"bean":"Bean rust - remove infected leaves",

"rice":"Rice blast - improve field management"

};


let result =
diseases[search] || "No disease found";


document.getElementById("diseaseResults").innerHTML =
"<p>"+result+"</p>";

}
