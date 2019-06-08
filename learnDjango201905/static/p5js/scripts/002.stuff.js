function setup() {

    createCanvas( window.innerWidth, window.innerHeight - 100 );

    frameRate(16);

    background(25);

    stroke(0, 200, 0);
    strokeWeight(5);

    noFill();
}

var x = 30;
function draw() {
    for(var i=0; i<16; i++){
        ellipse(x+i*30, 50, 10, 180);
    }
}