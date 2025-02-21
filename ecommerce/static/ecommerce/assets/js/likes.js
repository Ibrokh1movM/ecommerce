document.addEventListener("DOMContentLoaded", function() {
    let likeButton = document.getElementById("like-button");
    let likeCount = document.getElementById("like-count");

    let hasLiked = localStorage.getItem("liked") === "true";

    if (hasLiked) {
        likeButton.classList.add("active");
    }

    likeButton.addEventListener("click", function() {
        let action = hasLiked ? "unlike" : "like"; // Agar bosilgan bo'lsa unlike bo'ladi
        fetch(`/like/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ action: action })
        })
        .then(response => response.json())
        .then(data => {
            likeCount.textContent = data.likes;
            hasLiked = !hasLiked;
            localStorage.setItem("liked", hasLiked ? "true" : "false");
            likeButton.classList.toggle("active");
        });
    });
});
