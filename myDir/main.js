const main = document.querySelector("#main");
const menus = document.querySelectorAll(".btn_menu");
const indicator = document.querySelector("#indicator");

function selectMenu() {
    classlist = ["home", "service", "info", "QnA"];
    for (let i = 0; i < classlist.length; i++) {
        if (this.classList.contains(classlist[i])) {
            classlist.forEach((item) => 
                {
                    main.classList.remove(item);
                    indicator.classList.remove(item);
                }
            );
            main.classList.add(classlist[i]);
            indicator.classList.add(classlist[i]);
        }
    } 
}

menus.forEach((item) => 
    item.addEventListener('click' ,selectMenu));