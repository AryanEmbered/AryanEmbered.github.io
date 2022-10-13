function changeVisibility(window) {
    const proj = document.getElementById('projects');
    const res = document.getElementById('resume');
    
    const elem = document.getElementById(window);
    console.log(window)
    console.log(elem.style.display)

    
    if (window == 'resume' && proj.style.display == "block"){
        proj.style.display = "none";
    }
    else if (window == 'projects' && resume.style.display == "block"){
        res.style.display = "none";
    }

    if (elem.style.display == "none" || elem.style.display == ""){
        elem.style.display = "block";
    }
    else{
        elem.style.display = "none";
    }
  }
