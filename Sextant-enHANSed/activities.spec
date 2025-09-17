
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
	Hogne Håskjold [HH]
	GriffonSpade [GS]
	Eleazar [El]
"

[file]
gfx = "Sextant-enHANSed/activities"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 60
dy = 60
pixel_border = 1

tiles = { "row", "column", "tag"

; Road Activities

  0,  0, "unit.road"					;[GS]
  0,  1, "unit.rail"					;[GS]
  0,  2, "unit.maglev"					;[GS]
  0,  3, "unit.highway"					;[GS]

; Base Activities

  1,  0, "unit.outpost"					;[GS]
  1,  1, "unit.airstrip"				;[GS]
  1,  2, "unit.fortress"				;[HH][GS]
  1,  3, "unit.airbase"					;[HH][GS]
  1,  4, "unit.buoy"					;[El][GS]

; Unit activity letters:  (note unit icons have just "u.")

  2,  0, "unit.fortified"				;[HH]?
  2,  1, "unit.fortifying"				;[GS]
  2,  2, "unit.sentry"
  2,  3, "unit.patrol"
  2,  4, "unit.pillage"

  3,  0, "unit.connect"
  3,  1, "unit.auto_attack",
         "unit.auto_settler"
  3,  2, "unit.goto"
  3,  3, "unit.convert"
  3,  4, "unit.auto_explore"

  4,  0, "unit.mine"
  4,  1, "unit.irrigate"
  4,  2, "unit.transform"
  4,  3, "unit.pollution"
  4,  4, "unit.fallout"

}
