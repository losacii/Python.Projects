function setup() {

    createCanvas( window.innerWidth, window.innerHeight - 100 );

    frameRate(16);

    background(25);

    stroke(0, 200, 0);
    strokeWeight(1);

    noFill();
}

var x = 15;
num = 1;
jump = 0.2;
function draw() {
    num += 1

    translate(width/2, height/2);
    rotate(num * jump)

    alpha = 255 - num * 2
    if (alpha < 0){
        background(25);
        alpha = 255;
        num = 1;
        jump *= -1;
    }
    stroke(0, 200, 0, alpha);
    ellipse(0, 0, 50+num*5, 30+num*10);
}
