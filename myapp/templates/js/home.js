function openModal() {
    var modal = document.getElementById("myModal");
    var overlay = document.querySelector(".overlay");
    modal.style.display = "block";
    overlay.style.display = "block";
}

function closeModal() {
    var modal = document.getElementById("myModal");
    var overlay = document.querySelector(".overlay");
    modal.style.display = "none";
    overlay.style.display = "none";
}
