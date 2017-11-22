//Vatsal Savani
//A Simple Clock

function millies() {
  let tempDate = new Date()
  return tempDate.getMilliseconds()
}


function setup() {
  createCanvas(400, 450);
  angleMode(DEGREES);
}

function draw() {
  background(28,0,48);
  translate(200, 200);
  rotate(-90);

  let secC = [8,66,89];
  let minC = [23,160,191];
  let hrC = [144,230,221];
  let milC = [255,255,255];

  let hr = hour();
  let mn = minute();
  let sc = second();
  let mil = millies();

  strokeWeight(8);
  stroke(secC[0], secC[1], secC[2]);
  noFill();
  let secondAngle = map(sc, 0, 60, 0, 360);
  arc(0, 0, 280, 280, 0, secondAngle);

  stroke(minC[0], minC[1], minC[2]);
  let minuteAngle = map(mn, 0, 60, 0, 360);
  arc(0, 0, 260, 260, 0, minuteAngle);

  stroke(hrC[0], hrC[1], hrC[2]);
  let hourAngle = map(hr % 12, 0, 12, 0, 360);
  arc(0, 0, 240, 240, 0, hourAngle);

  stroke(milC[0], milC[1], milC[2]);
  let milAng = map(mil, 0, 1000, 0, 360);
  if (sc % 2 == 1) {
    arc(0,0,300, 300, 0, milAng);
  } else {
    arc(0,0, 300, 300, milAng, 0);
  }

  push();
  rotate(secondAngle);
  stroke(secC[0], secC[1], secC[2]);
  line(0, 0, 100, 0);
  pop();

  push();
  rotate(minuteAngle);
  stroke(minC[0], minC[1], minC[2]);
  line(0, 0, 75, 0);
  pop();

  push();
  rotate(hourAngle);
  stroke(hrC[0], hrC[1], hrC[2]);
  line(0, 0, 50, 0);
  pop();

  stroke(255);
  point(0, 0);

  // rotate(90);
  // fill(255);
  // noStroke();


  rotate(90);
  translate(-200, -200);

  fill(255);
  noStroke();
  textAlign(CENTER, CENTER);
  textSize(35);

  if (hr < 10) {
    hr = '0' + hr;
  } 
  if (mn < 10) {
    mn = '0' + mn;
  }
  if (sc < 10) {
    sc = '0' + sc
  }

  push();
  textSize(15);
  text('The TimeKeeper by Vatsal Savani', 200, 20);
  pop();
  text(hr + ':' + mn + ':' + sc, 200, 410);

}


