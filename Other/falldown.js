/*
@title: Falldown mini
@author: 
@tags: []
@addedOn: 2024-00-00
*/

const player = "p"
const wall = "w"
const wallL = "L"
const wallR = "R"

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
  [ wall, bitmap`
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
................
................` ],
  [ wallL, bitmap`
LLLLLLLLLLLLL...
LLLLLLLLLLLLL...
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
................
................` ], 
  [ wallR, bitmap`
...LLLLLLLLLLLLL
...LLLLLLLLLLLLL
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
................
................` ], 
)

setSolids([ player, wall, wallL, wallR ])

let level = 0
const levels = [
  map`
.....p.....
wwwwL.Rwwww
...........
wwwL.Rwwwww
...........
...........
...........
...........
...........
...........`
]

setMap(levels[level])

setPushables({
  [ player ]: []
})

onInput("s", () => {
  getFirst(player).y += 1
})

afterInput(() => {
  
})