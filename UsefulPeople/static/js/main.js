
function disp(div) {
    if (div.style.display == "none") {
        div.style.display = "block";
        document.getElementById('resume_button').style.display = "none";
    } else {
        div.style.display = "none";
    }
}
