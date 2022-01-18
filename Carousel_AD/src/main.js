const carouselBox = document.querySelector("#carouselBox");
const carouselInner = carouselBox.querySelector("#carouselInner");
const adBoxs = carouselInner.querySelectorAll(".adBox");
const leftBtn = carouselBox.querySelector("#leftAd");
const rightBtn = carouselBox.querySelector("#rightAd");
const firstAd = carouselInner.firstChild;
const lastAd = carouselInner.lastChild;

let leftSelected = 0;
let selected = 1;
let rightSelected = 2;
let ads = [leftSelected, selected, rightSelected];

console.log(selected);

function moveToAd(type) {
    if(type === 0) {
        for(let i = 0; i < 3; i++) {
            ads[i] -= 1;
            if(ads[i] < 0) {
                ads[i] = adBoxs.length - 1;
            }
        }
    } else {
        for(let i = 0; i < 3; i++) {
            ads[i] += 1;
            if(ads[i] > adBoxs.length - 1) {
                ads[i] = 0;
            }
        }
    }
    leftSelected = ads[0];
    selected = ads[1];
    rightSelected = ads[2];
}

function hidden() {
    for(let i=0; i<adBoxs.length; i++) {
        adBoxs[i].classList.add("hidden");
    }

    adBoxs[selected].classList.remove("hidden");
    adBoxs[leftSelected].classList.remove("hidden");
    adBoxs[rightSelected].classList.remove("hidden");

    carouselInner.insertBefore(adBoxs[selected], adBoxs[rightSelected]);
    carouselInner.insertBefore(adBoxs[leftSelected], adBoxs[selected]);

    console.log(selected);
}

function btnLeft() {

    moveToAd(0);
    hidden();
}

function btnRight() {
    moveToAd(1);
    hidden();
}

leftBtn.addEventListener('click', btnLeft);
rightBtn.addEventListener('click', btnRight);