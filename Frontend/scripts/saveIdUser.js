// import userId from "../scripts/sessionStoreId";


function handleClickEvent() {
  const update = document.querySelector(".url-edit");
    update.addEventListener('click', () => {
        //console.log("aquie identificador");
        console.log(update.textContent);
    });
}

export { handleClickEvent };
