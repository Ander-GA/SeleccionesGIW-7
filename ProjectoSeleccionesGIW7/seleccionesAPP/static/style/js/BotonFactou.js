
    document.addEventListener("DOMContentLoaded", function () {

      const factous = [
        "Messi es el GOAT del Deporte",
        "Sancet acabara su carrera con 10 balones de oro, futuro GOAT del deporte",
        "Nico Williams > Vinicius JR",
        "Prados, Galaxy, Sancet > Busi, Iniesta, Xavi",
        "El bicho es el GOAT del futbool europeo",
        "Nico Guru e Iñaki son el mejor tridente del futbol moderno"
      ];
  
      const factoboton = document.createElement("button");
      const facto = document.createElement("p");
  
      factoboton.textContent = "Suelta ese factouuuuu";
      factoboton.style.padding = "10px 20px";
      factoboton.style.backgroundColor = "#0055ff";
      factoboton.style.color = "#fff";
      factoboton.style.border = "none";
      factoboton.style.borderRadius = "5px";
      factoboton.style.cursor = "pointer";
      factoboton.style.marginTop = "15px";
  
      facto.style.marginTop = "10px";
      facto.style.fontSize = "1.1em";
      facto.style.color = "#333";
      facto.style.textAlign = "center";
  
      factoboton.addEventListener("click", function () {
        const randomFact = factous[Math.floor(Math.random() * factous.length)];
        facto.textContent = randomFact;
      });
  
      const contentDiv = document.getElementById("content");
      contentDiv.appendChild(factoboton);
      contentDiv.appendChild(facto);
    });
  