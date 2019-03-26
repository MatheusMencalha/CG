float solX, solY, terraX, terraY, luaX, luaY;
float rSol, rTerra, rLua;
float thetaSol, thetaTerra, thetaLua;

void setup(){
  size(1000,700);
  solX = width/2;
  solY = height/2;
  rSol = 200;
  rTerra = rSol/2;
  rLua = rSol/5;
  terraX = solX - 300;
  terraY = solY;
  luaX = solX - 300;
  luaY = solY - 100;
  thetaTerra = PI/100;
  thetaLua = PI/100;

}

void draw(){
  background(0,0,0);
  
  //sol
  fill(255,255,0);
  circle( solX, solY, rSol);
  
  //terra
  fill(0,0,255);
  circle( terraX, terraY, rTerra);
  
  //lua
  fill(255,255,255);
  circle( luaX, luaY, rLua);
  
  terraX -= solX;
  terraY -= solY;
  luaX -= solX;
  luaY -= solY;
  
  float novoTerraX = (terraX * cos(thetaTerra) + terraY * sin(thetaTerra)) + solX;// translação: axcosTheta + aysinTheta | aycosTheta - axsinTheta (o solX/Y eh usado pois o sol se torna o centro)
  float novoTerraY = (terraY * cos(thetaTerra) - terraX * sin(thetaTerra)) + solY;
  float novoLuaX = (luaX * cos(thetaLua) + luaY * sin(thetaLua)) + solX;
  float novoLuaY = (luaY * cos(thetaLua) - luaX * sin(thetaLua)) + solY;
  
  terraX = novoTerraX;
  terraY = novoTerraY;
  luaX = novoLuaX;
  luaY = novoLuaY;
  
  luaX -= terraX;
  luaY -= terraY;
  novoLuaX = (luaX * cos(thetaLua) + luaY * sin(thetaLua)) + terraX;
  novoLuaY = (luaY * cos(thetaLua) - luaX * sin(thetaLua)) + terraY;
  
  luaX = novoLuaX;
  luaY = novoLuaY;
}
