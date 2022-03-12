const bodyObject = document.querySelector("body");
const icon = bodyObject.querySelector(".title");
const seats = bodyObject.querySelector(".seats");
const logos = bodyObject.querySelectorAll(".logo");

// const portraits = ["./image/portrait1", "./image/portrait2"];
// const lines = ["./image/line1", "./image/line2"];
// const silhouettes = ["./image/silhouette1", "./image/silhouette2"];

let countWidth = 4;
let countHeight = 4;
let list = [0, 6, 7, 10, 11];

logos.forEach(function(element){
    let num = 0;
    let randWidth = 0;
    let randHeight = 0;
    let randSize = 1;
    let randDeg = 0;
    while (list.indexOf(num) > -1) {
        randWidth = parseInt(Math.random() * countWidth);
        randHeight = parseInt(Math.random() * countHeight);
        num = (randHeight * countWidth) + randWidth + 1;
        randSize = Math.random() * 0.3 + 0.5;
        randDeg = Math.floor(Math.random() * 40 - 20);
    }
    list.push(num);
    element.style = `--l: ${randWidth}; --t: ${randHeight}; --s:${randSize}; --r:${randDeg}deg`;

})