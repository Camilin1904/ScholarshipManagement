function htmlDecode(str) {
    const doc = new DOMParser().parseFromString(str, "text/html");
    return doc.documentElement.textContent;
  }
  
  function arrayFixer(lista) {
      var resultado = [];
      for(var i = 0; i < lista.length; i++) {
          var elemento = lista[i];
          if(elemento !== "[[" && elemento !== "]]" && elemento !== "], [" && elemento !== '"' &&
          elemento !== "[" && elemento !== "]" && elemento !== "," && elemento !== ' ') {
              resultado.push(elemento);
          }
      }
      return resultado;
  }
  
  // Definir los colores base en hexadecimal
  var baseColors = ["#E2E9F3", "#2D6A9F", "#FFFFFF", "#3A4459"];
  
  // Definir una función para mezclar dos colores y obtener un color intermedio
  function mixColors(color1, color2, ratio) {
    // Convertir los colores a números enteros
    var c1 = parseInt(color1.substring(1), 16);
    var c2 = parseInt(color2.substring(1), 16);
  
    // Calcular los componentes rojo, verde y azul del color resultante
    var r = Math.round(((c1 >> 16) & 0xFF) * ratio + ((c2 >> 16) & 0xFF) * (1 - ratio));
    var g = Math.round(((c1 >> 8) & 0xFF) * ratio + ((c2 >> 8) & 0xFF) * (1 - ratio));
    var b = Math.round((c1 & 0xFF) * ratio + (c2 & 0xFF) * (1 - ratio));
  
    // Convertir el color resultante a hexadecimal
    var color = "#" + r.toString(16).padStart(2, "0") + g.toString(16).padStart(2, "0") + b.toString(16).padStart(2, "0");
  
    // Devolver el color resultante
    return color;
  }
  
  // Definir una función para generar una paleta de colores a partir de los colores base
  function generatePalette(baseColors, size) {
    // Crear un arreglo vacío para almacenar los colores de la paleta
    var palette = [];
  
    // Calcular el número de combinaciones posibles entre los colores base
    var combinations = baseColors.length * (baseColors.length - 1) / 2;
  
    // Calcular el número de tonos intermedios que se deben generar por cada combinación
    var shades = Math.floor(size / combinations);
  
    // Iterar por cada par de colores base
    for (var i = 0; i < baseColors.length - 1; i++) {
      for (var j = i + 1; j < baseColors.length; j++) {
        // Añadir los colores base a la paleta
        palette.push(baseColors[i]);
        palette.push(baseColors[j]);
  
        // Iterar por cada tono intermedio
        for (var k = 1; k < shades; k++) {
          // Calcular el ratio de mezcla entre los colores base
          var ratio = k / shades;
  
          // Mezclar los colores base y obtener el color intermedio
          var color = mixColors(baseColors[i], baseColors[j], ratio);
  
          // Añadir el color intermedio a la paleta
          palette.push(color);
        }
      }
    }
  
    // Devolver la paleta de colores
    return palette;
  }
  
  // Invocar la función para generar una paleta de 27 colores
  var palette = generatePalette(baseColors, 27);
  
  let ctx = document.getElementById("chart").getContext("2d");
  let chart = new Chart(ctx, {
    type: "pie",
    data: {
     labels: arrayFixer(htmlDecode("{{semesterNames}}").split('\'')),
     datasets: [
      {
        label: "Porcentaje de Estudiantes por Semestre",
        backgroundColor: palette,
        data: arrayFixer("{{semester}}")
      }
     ]
    },
    options: {
     title: {
      text: "Porcentaje de Estudiantes por Semestre",
      display: true
     }
    },
    plugins: [ChartDataLabels]
  });
  
  let ctx2 = document.getElementById("chart2").getContext("2d");
  let chart2 = new Chart(ctx2, {
    type: "bar",
    data: {
     labels: arrayFixer(htmlDecode("{{careerNames}}").split('\'')),
     datasets: [
      {
        label: "Cantidad de Estudiantes por Carrera",
        backgroundColor: palette,
        data: arrayFixer("{{career}}")
      }
     ]
    },
    options: {
    indexAxis: 'y',
     title: {
      text: "Cantidad de Estudiantes por Carrera",
      display: true
     }
    }
  });
  
  let ctx3 = document.getElementById("chart3").getContext("2d");
  let chart3 = new Chart(ctx3, {
    type: "bar",
    data: {
     labels: arrayFixer(htmlDecode("{{facultyNames}}").split('\'')),
     datasets: [
      {
        label: "Cantidad de Estudiantes por Facultad",
        backgroundColor: palette,
        data: arrayFixer("{{faculty}}")
      }
     ]
    },
    options: {
     title: {
      text: "Cantidad de Estudiantes por Facultad",
      display: true
     }
    }
  });