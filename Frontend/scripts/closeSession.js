function close() {
    localStorage.clear();
    sessionStorage.clear();
    document.cookie.split(";").forEach(function (c) {
      document.cookie = c
        .replace(/^ +/, "")
        .replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
        
    });
  }
  
  // window.onload = () => {
  //   close();
  // };
  
  document.querySelector("#logoutButton").addEventListener("click", function() {
    close();
    window.location.href = "/";
  });
  
  
  function retroceder() {
    window.history.back();
  }
  
  document.getElementById('retrocederBtn').addEventListener('click', function() {
    window.history.back();
  });