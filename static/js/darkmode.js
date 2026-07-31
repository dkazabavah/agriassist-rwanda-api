const button = document.getElementById("theme-toggle");


button.addEventListener("click",()=>{

document.body.classList.toggle("dark");


localStorage.setItem(
"theme",
document.body.classList.contains("dark")
);

});


if(localStorage.getItem("theme") === "true"){

document.body.classList.add("dark");

}
