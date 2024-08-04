/*
@title: Falldown mini
@author: 
@tags: []
@addedOn: 2024-00-00
*/

const player = "p"
const walls = "w"
const wallsL = "L"
const wallsR = "R"
const invisWall = "i"

setLegend(
  [ player, bitmap`
....33333333....
...3333333333...
..330003300033..
.33302133L20333.
3333010330L03333
3333333333333333
3333333HH3333333
3333333HH3333333
3333833333383333
3333888888883333
3333388228833333
3333338888333333
.33333333333333.
..333333333333..
...3333333333...
....33333333....` ],
  [ walls, bitmap`
LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL
................
................
................
................
................
................
................
................
................
................
................
................
................` ],
  [ wallsL, bitmap`
LLLLLLLLLLLLLLL.
LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.
................
................
................
................
................
................
................
................
................
................
................
................
................` ], 
  [ wallsR, bitmap`
.LLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLL
.LLLLLLLLLLLLLLL
................
................
................
................
................
................
................
................
................
................
................
................
................` ], 
  [ invisWall, bitmap`
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222
2222222222222222` ]
)

setSolids([ player, walls, wallsL, wallsR, invisWall ])

let go = false;
let gameIsOn = false;
const levels = [
  map`
...........
wwwwL.Rwwww
...........
wwwL.Rwwwww
p..........
wwwwwwwwwL.
...........
.Rwwwwwwwww
...........
iiiiiiiiiii`,
  map`
...........
...........
...........
...........
...........
....iii....
....ipi....
....iii....
...........
...........`,
]

// setMap(levels[level])
setLevel(1, "Press J to start", "/reset!")

setPushables({
  [ walls ]: [ player ],
  [ wallsL ]: [ player ],
  [ wallsR ]: [ player ]
})

function wallUpdate(){
  if (gameIsOn){
    moveWallsUp();
    // killRedundantWalls()
    spawnMoreWalls();
  }
}

function setLevel(l, text1="", text2=""){
  clearText();
  setMap(levels[l])
  if (text1!=""){
    addText(text1, {
      x: 1,
      y: 1,
      color: color`3`
    })
  }
  if (text2!=""){
    addText(text2, {
      x: 1,
      y: 4,
      color: color`7`
    })
  }
}

function checkIfWallNeeded(){ // 8
  for (let i = 0; i < 11; i++){
    if (getTile(i, 8).length > 1){
      let type = getTile(i, 8)[0]['_type']
      let type2 = getTile(i, 8)[1]['_type']
      for (let letter of ["w", "L", "R"]){
        if (type == letter || type1 == letter)
          return false;
      }
    }
    if (getTile(i, 8).length > 0){
      let type = getTile(i, 8)[0]['_type']
      for (let letter of ["w", "L", "R"]){
        if (type == letter)
          return false;
      }
    }
  }
  return true;
}

function spawnMoreWalls(){
  if (checkIfWallNeeded()){
    let x = randint(10); // 0-10
    if (x == 0){
      addSprite(1, 9, wallsR);
      for (let i = 2; i < 11; i++){
        addSprite(i, 9, walls);
      }
    } // Speacial case!
    else if (x == 10){
      for (let i = 0; i < 9; i++){
        addSprite(i, 9, walls);
      }
      addSprite(9, 9, wallsL);
    } // Speacial case!
    else {
      for (let i = 0; i < x-1; i++){
        addSprite(i, 9, walls);
      }
      addSprite(x-1, 9, wallsL);
      addSprite(x+1, 9, wallsR);
      for (let i = x+2; i < 11; i++){
        addSprite(i, 9, walls);
      }
    }
  }
}

function moveWallsUp(){
  for (let wall of getAll(walls)){
    wall.y -= 1;
    if (wall.y == 0){wall.remove();}
  }
  for (let wall of getAll(wallsL)){
    wall.y -= 1;
    if (wall.y == 0){wall.remove();}
  }
  for (let wall of getAll(wallsR)){
    wall.y -= 1;
    if (wall.y == 0){wall.remove();}
  }
}

function playerUpdate(){
  fixGlitch();
  gravity();
}

function fixGlitch(){
  if (checkForGlitch()){
    
  }
}

function checkBelowPlayer(){
  let pl = getFirst(player)
  if (getTile(pl.x, pl.y+1).length > 0){
    return false;
  }
  return true;
}

function gravity(){
  if (checkBelowPlayer()){
    getFirst(player).y += 1;
  }
}

function randint(max) {
  return Math.floor(Math.random() * max);
}

function gameUpdate(){
  if (go){
    wallUpdate();
    // getInput();
    go = false;
  }else{go=true;}
  playerUpdate();
}

function getInput(){
  onInput("a", () => {
    getFirst(player).x -= 1;
  })
  onInput("d", () => {
    getFirst(player).x += 1;
  })
  onInput("j", () => {
    setLevel(0);
    gameIsOn = true;
  })
}

// let wallUpdateInt = setInterval(wallUpdate, 2000);
// let playerUpdateInt = setInterval(playerUpdate, 2000);
// let wallUpdateInt = setInterval(wallUpdate, 750);
// let playerUpdateInt = setInterval(playerUpdate, 500);
let gameUpdateInt = setInterval(gameUpdate, 375);
onInput("a", () => {
  getFirst(player).x -= 1;
})
onInput("d", () => {
  getFirst(player).x += 1;
})
onInput("j", () => {
  setLevel(0);
  gameIsOn = true;
})