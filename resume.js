function changeVisibility(window) {
    const elem = document.getElementById(window);
    if (elem.style.display == "none"){
        elem.style.display = "block";
    }
    else{
        elem.style.display = "none";
    }
  }