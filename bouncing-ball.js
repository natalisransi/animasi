var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d'); 

var radius = 20; //variabel utama yang digunakan sebagai radius dari bola, 
				//dan jarak ketika bola bersinggungan ketika mencapai ujung.
var color = "#C71585";
var g = 0.1; // akselerasi karena gravitasi
var x = 50;  // posisi horizontal awal
var y = 50;  // posisi vertical awal
var vx = 2;  // kecepatan horisontal awal
var vy = 0;  // kecepatan vertical awal
 
window.onload = init; 
 
function init() {
  setInterval(onEachStep, 1000/60); // 60 fps
};
 
function onEachStep() {
  vy = vy + g; // gravitasi meningkatkan kecepatan vertikal
  x =x+ vx; // kecepatan horizontal meningkatkan posisi horizontal
  y = y+ vy ; //kecepatan vertikal meningkatkan posisi vertikal
 
  if (y > canvas.height - radius){ // jika bola menyentuh tanah
    y = canvas.height - radius; // reposisi di tanah
    vy *= -0.8; // kemudian mundur dan kurangi kecepatan vertikalnya
  }
  if (x > canvas.width + radius){ // jika bola melampaui kanvas
    x = -radius; // membungkusnya
  }
  drawBall(); // draw the ball
};
 
function drawBall() {
    with (context){
		//menghapus screen lama
        clearRect(0, 0, canvas.width, canvas.height); 
        fillStyle = color;
        beginPath();
		
		//membuat objek bola
        arc(x, y, radius, 0, 2*Math.PI, true);
        closePath();
        fill();
    };
};