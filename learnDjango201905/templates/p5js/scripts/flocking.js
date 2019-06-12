var FPS = 30;

const flock = [];

function setup() {

    createCanvas(
        window.innerWidth,
        window.innerHeight
    );

    frameRate(FPS);

    background(0);
    colorMode(HSB);

    textAlign(CENTER, CENTER);
    textFont("Consolas");
    textSize(14);

    // 
    for (let i = 0; i < 128; i++) {
        flock.push(new Boid());
    }
}

var ang = 0;

function draw() {

    background(0);

    for (let boid of flock) {
        boid.align(flock);
        boid.cohesion(flock);
        boid.separate(flock);
        boid.checkBoundary();
        boid.update();
        boid.render();
    }
}


class Boid {

    constructor() {

        this.position = createVector(random(width), random(height));

        this.velocity = p5.Vector.random2D();
        this.velocity.setMag(random(0.3, 1.6));

        this.acceleration = createVector();

        this.maxForce = 0.2;
        this.maxSpeed = 4;

        this.clr = color(random(255), random(255), random(255));

    }

    update() {
        this.velocity.add(this.acceleration);
        this.position.add(this.velocity);


        this.acceleration.limit(this.maxForce);
        this.velocity.limit(this.maxSpeed);

        this.acceleration.mult(0);
    }

    render() {
        strokeWeight(5);
        stroke(this.clr);
        point(this.position.x, this.position.y);
    }

    checkBoundary() {

        if (this.position.x > width) {
            this.position.x = 0;
        } else if (this.position.x < 0) {
            this.position.x = width;
        }

        if (this.position.y > height) {
            this.position.y = 0;
        } else if (this.position.y < 0) {
            this.position.y = height;
        }

    }


    align(boids) {
        let perceptionRadius = 30;
        let steer = createVector();
        let total = 0;
        for (let other of boids) {
            let d = dist(this.position.x, this.position.y,
                other.position.x, other.position.y);
            if (other != this && d < perceptionRadius) {
                steer.add(other.velocity);  // 
                total++;
            }
        }
        if (total > 0) {
            steer.div(total);
            this.acceleration.add(steer.div(10));
        }
    }


    cohesion(boids) {
        let perceptionRadius = 500;
        let steer = createVector();
        let total = 0;
        for (let other of boids) {
            let d = dist(this.position.x, this.position.y,
                other.position.x, other.position.y);
            if (other != this && d < perceptionRadius) {
                steer.add(other.position);  // 
                total++;
            }
        }
        if (total > 0) {
            steer.div(total);
            steer.sub(this.position);
            steer.setMag(1.0 / 8);
            this.acceleration.add(steer);
        }
    }

    separate(boids) {
        let perceptionRadius = 100;
        let steer = createVector();
        let total = 0;
        for (let other of boids) {
            let d = dist(this.position.x, this.position.y,
                other.position.x, other.position.y);
            if (other != this && d < perceptionRadius) {
                total++;
                let diff = p5.Vector.sub(this.position, other.position);
                diff.div(d * 3); //
                steer.add(diff);
            }
        }
        if (total > 0) {
            steer.div(total);
            this.acceleration.add(steer);
        }
    }

}