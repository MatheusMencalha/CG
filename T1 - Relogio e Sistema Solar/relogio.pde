int radius = 350;
int sx = 600;
int sy = 500; 
int cx, cy;
 
void setup() {
  size(600, 500);
  cx = width/2;
  cy = height/2;
}
 
void draw() {
  background(255, 255, 255);
  noFill();
  ellipse(cx, cy, radius, radius);

  // draw clock
  for (int i = 0; i < 12; i ++) {
      float ang = i * 30 * PI / 180;
      float sina = sin(ang);
      float cosa = cos(ang);
      int x1 = (int)(cx + (radius / 2 - 30) * sina);
      int y1 = (int)(cy + (radius / 2 - 30) * cosa);
      int x2 = (int)(cx + radius / 2 * sina);
      int y2 = (int)(cy + radius / 2 * cosa);
      line(x1, y1, x2, y2);
  }
    for (int i = 0; i < 60; i ++) {
      float ang = i * 6 * PI / 180;
      float sina = sin(ang);
      float cosa = cos(ang);
      int x1 = (int)(cx + (radius / 2 - 20) * sina);
      int y1 = (int)(cy + (radius / 2 - 20) * cosa);
      int x2 = (int)(cx + radius / 2 * sina);
      int y2 = (int)(cy + radius / 2 * cosa);
      line(x1, y1, x2, y2);
      strokeWeight(3);
  }
  float h, m, s;
  h = hour();
  m = minute();
  s = second();
  textSize(32);
  fill(50);
  text("Time: " + (int)h + ":" + (int)m + ":" + (int)s, 1, height);
  // draw second
  strokeWeight(2);
  float ang = (30 - s) * 6 * PI / 180;
  float sina = sin(ang);
  float cosa = cos(ang);  
  int sx = (int)(cx + radius / 2.3 * sina);
  int sy = (int)(cy + radius / 2.3 * cosa);
  line(cx, cy, sx, sy);
  
  
  // draw minute
  strokeWeight(3);
  m += (s / 60.0);
  ang = (30 - m) * 6 * PI / 180;
  sina = sin(ang);
  cosa = cos(ang);
  int mx = (int)(cx + radius / 3 * sina);
  int my = (int)(cy + radius / 3 * cosa);  
  line(cx, cy, mx, my);
  
  // draw hour
  strokeWeight(5);
  h += (m / 60.0);  
  ang = (30 - h) * 30 * PI / 180;
  sina = sin(ang);
  cosa = cos(ang);
  int hx = (int)(cx + radius / 4 * sina);
  int hy = (int)(cy + radius / 4 * cosa);  
  line(cx, cy, hx, hy);
}
