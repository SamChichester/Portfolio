const words = ["developer", "computer scientist", "programmer", "engineer"];
const colors = ["#e63946", "#457b9d", "#2a9d8f", "#f4a261"];
let i = 0;
let timer;

function typingEffect() {
    let word = words[i].split("");
    document.querySelector(".text").style.color = colors[i % colors.length]; // Change text color
    let loopTyping = function() {
        if (word.length > 0) {
            document.querySelector(".text").innerHTML += word.shift();
        } else {
            setTimeout(deletingEffect, 1000); // Delay before starting to delete
            return false;
        }
        timer = setTimeout(loopTyping, 200);
    };
    loopTyping();
}

function deletingEffect() {
    let word = words[i].split("");
    let loopDeleting = function() {
        if (word.length > 0) {
            word.pop();
            document.querySelector(".text").innerHTML = word.join("");
        } else {
            if (words.length > (i + 1)) {
                i++;
            } else {
                i = 0;
            }
            setTimeout(typingEffect, 500); // Delay before starting to type again
            return false;
        }
        timer = setTimeout(loopDeleting, 100);
    };
    loopDeleting();
}

document.addEventListener("DOMContentLoaded", function() {
    typingEffect();
});
