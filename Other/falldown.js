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
)

setSolids([ player, walls, wallsL, wallsR ])

let level = 0
const levels = [
  map`
.....p.....
wwwwL.Rwwww
...........
wwwL.Rwwwww
...........
wwwwwwwwwL.
...........
.Rwwwwwwwww
...........
wwwwwL.Rwww`
]

setMap(levels[level])

setPushables({
  [ walls ]: [ player ],
  [ wallsL ]: [ player ],
  [ wallsR ]: [ player ]
})

function wallUpdate(){
  moveWallsUp()
  // killRedundantWalls()
  spawnMoreWalls()
}

function checkIfWallNeeded(){ // 8
  for (let i = 0; i < 11; i++){
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
    if (x == 0){} // Speacial case!
    else if (x == 10){} // Speacial case!
    else {
      for (let i = 0; i < x-1; i++){
        addSprite(i, 9, walls);
      }
      addSprite(x-1, 9, wallsL)
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

function randint(max) {
  return Math.floor(Math.random() * max);
}

let wallUpdateInt = setInterval(wallUpdate, 2000);
// let wallUpdateInt = setInterval(wallUpdate, 750);
// let playerUpdateInt = setInterval(playerUpdate, 200);

onInput("s", () => {
  getFirst(player).y += 1
})
onInput("a", () => {
  getFirst(player).x -= 1;
})
onInput("d", () => {
  getFirst(player).x += 1;
})
afterInput(() => {
  
})