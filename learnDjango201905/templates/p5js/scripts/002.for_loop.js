function setup() {

    createCanvas( window.innerWidth, window.innerHeight - 100 );

    frameRate(16);

    background(25);

    stroke(0, 200, 0);
    strokeWeight(1);

    noFill();
}

var x = -240;
function draw() {
    translate(width/2, height/2 - 100);
    for(var i=0; i<16; i++){
        ellipse(x+i*30, 50, 30, 180);
    }
}

// translate(X, Y)
// for loop
// frateRate
// stroke(random(255),random(255),random(255));