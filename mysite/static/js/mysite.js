// Twój kod JavaScript tutaj
console.log("JavaScript file loaded successfully.");

// Funkcja do przewijania strony do góry
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Pokaż przycisk, gdy użytkownik przewinie stronę do samego dołu
window.onscroll = function() {
    var topButton = document.getElementById("topButton");
    var heroImage = document.querySelector(".hero-image");
    var heroImageHeight = heroImage ? heroImage.offsetHeight : 0;
    var totalHeight = document.body.offsetHeight + heroImageHeight;

    if ((window.innerHeight + window.scrollY) >= totalHeight) {
        topButton.style.display = "block";
    } else {
        topButton.style.display = "none";
    }
};