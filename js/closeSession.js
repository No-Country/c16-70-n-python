function close() {
    console.log("close session");
    localStorage.clear();
    sessionStorage.clear();
    document.cookie.split(";").forEach(function(c) {
        document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
    });
}





document.querySelector(".cerrar-sesion").addEventListener("click", () => {
    close();
    window.location.href = "../Home Page/Index.html";
});


