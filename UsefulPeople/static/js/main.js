function disp(div) {
    if (div.style.display == "none") {
        div.style.display = "block";
        document.getElementById('resume_button').style.display = "none";
    } else {
        div.style.display = "none";
    }
}

var curFieldNameId = 1;
function addField() {
    countOfFields++;
    curFieldNameId++;
    var div = document.createElement("form");
    div.innerHTML = "<input name="name_" + curFieldNameId + "" type="text" /> <a onclick="return deleteField(this)" href="#">[X]</a>";
    document.getElementById("parentId").appendChild(div);
    return false;
}
