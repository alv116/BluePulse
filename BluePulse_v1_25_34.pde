int[] data = new int[256];
float tiempo = 0;

void settings() {
  fullScreen();
}

void setup() {
  for (int i = 0; i < data.length; i++) {
    data[i] = height / 2;
  }
  frameRate(30); // Animación más lenta
}

void draw() {
  background(0);

  // Señal muy aleatoria con mezcla de ruido, sinusoides, pulsos y picos
  float ruidoAleatorio = random(-100, 100);
  float sinusoide = 40 * sin(tiempo * random(0.5, 2));
  float ondaRuidosa = 50 * noise(tiempo * random(0.01, 0.1));
  float pico = (random(1) > 0.985) ? random(80, 150) : 0; // Picos esporádicos

  int nuevoValor = int(height / 2 + ruidoAleatorio + sinusoide + ondaRuidosa + pico);
  nuevoValor = constrain(nuevoValor, 0, height - 1);

  // Desplazar datos
  for (int i = 1; i < data.length; i++) {
    data[i - 1] = data[i];
  }
  data[data.length - 1] = nuevoValor;

  // Dibujar línea única
  stroke(0, 255, 0);
  strokeWeight(2);
  noFill();

  beginShape();
  for (int i = 0; i < data.length; i++) {
    vertex(i * (width / float(data.length)), height - data[i]);
  }
  endShape();

  // Línea base
  stroke(0, 100, 0);
  strokeWeight(1);
  line(0, height / 2, width, height / 2);

  // Avanzar tiempo lentamente
  tiempo += 0.03;
}
