const menus = document.querySelectorAll("#menuLine button");
const menuTexts = document.querySelectorAll("#menuLine button a")

function hovered() {
    menus.forEach((menu) =>
        menu.classList.remove("active"));
    const selectedMenu = this.parentNode;
    selectedMenu.classList.add("active");
}

function hoverout() {
    menus.forEach((menu) =>
        menu.classList.remove("active"));
}

function clicked() {
    menus.forEach((menu) =>
        menu.classList.remove("selected"));
    const selectedMenu = this.parentNode;
    selectedMenu.classList.add("selected");
}

menuTexts.forEach((item) => {
    item.addEventListener("mouseover", hovered);
    item.addEventListener("mouseout", hoverout);
    item.addEventListener("click", clicked);
});