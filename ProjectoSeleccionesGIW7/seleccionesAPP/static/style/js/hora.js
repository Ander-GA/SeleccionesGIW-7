    document.addEventListener("DOMContentLoaded", function() {
    const greetingElement = document.createElement("p");
    const currentHour = new Date().getHours();
    let greetingMessage;

    if (currentHour < 12) {
      greetingMessage = "¡Buenos días!";
    } else if (currentHour < 18) {
      greetingMessage = "¡Buenas tardes!";
    } else {
      greetingMessage = "¡Buenas noches!";
    }

    greetingElement.textContent = greetingMessage;
    greetingElement.style.fontSize = "1.2em";
    greetingElement.style.color = "#555";
    greetingElement.style.marginTop = "10px";
    greetingElement.style.textAlign = "center";

    const header = document.getElementById("header");
    header.appendChild(greetingElement);
  });
