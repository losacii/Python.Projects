    function setup() {
        createCanvas( window.innerWidth, window.innerHeight - 100 );
        background(25);
        noFill();

        stroke(255); strokeWeight(1);
        line(0, height/2, width, height/2);
        line(width/2, 0, width/2, height);

        stroke(0, 255, 0); strokeWeight(10);
        rect(width/2-150, height/2-100, 300, 200);

    }

    function draw() {
    }

    // Canvas

    // background

    // fill, noFill
    // stroke, strokeWeight

    // line, rect

    // setup(), draw()
