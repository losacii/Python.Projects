function setup() {
        createCanvas( window.innerWidth, window.innerHeight - 100 );
        background(25);
        noFill();
        print("Width: " + width)

    }

var x = -innerWidth/2;
function draw() {
    translate(width/2, height/2);
    background(0, 30);

    stroke(255); strokeWeight(0.2);
    line(-width/2, 0, width/2, 0);
    line(0, -height/2, 0, height/2);

    stroke(0, 255, 0); strokeWeight(10);
    rect(-150, -100, 300, 200);

    x += 3;
    if(x > width / 2 + 200){
        x = -width/2 -50;
    }
    y = 150 * sin(x / 20.0); 
    point(x, y);
}