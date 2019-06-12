function setup() {

    createCanvas( window.innerWidth, window.innerHeight - 100 );

    frameRate(16);

    background(25);

    stroke(0, 200, 0);
    strokeWeight(1);

    noFill();
}

var x = 15;
num = 1
function draw() {
    translate(width/2, height/2 - 100);

    num += 1
    ellipse(x, 50, 50+num*5, 30+num*10);
}
