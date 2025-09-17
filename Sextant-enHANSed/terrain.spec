
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
	Hogne Håskjold <hogne@freeciv.org> [HH]
    Tatu Rissanen <tatu.rissanen@hut.fi> [TR]
    Jeff Mallatt <jjm@codewell.com> (miscellaneous) [JM]
    Eleazar (buoy) [El]
    The Square Cow (inaccessible terrain) [Cow]
	GriffonSpade [GS]
    Architetto Francesco [http://www.public-domain-photos.com/] [AF]
	Unknown Battle For Wesnoth artists [BFW]
	Hans Lemurson (irrigation, farmland) [HL]
	Unknown/Other [??]
"

[file]
gfx = "Sextant-enHANSed/terrain"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 60
dy = 60
pixel_border = 1

tiles = { "row", "column", "tag"

; Grassland, and whether terrain to north, south, east, west 
; is more grassland:

  0,  1, "t.l0.grassland1"					;[TR]?
  0,  1, "t.l0.forest1"						;[TR]?
  0,  1, "t.l0.hills1"						;[TR]?
  0,  1, "t.l0.mountains1"					;[TR]?
  0,  2, "t.l0.inaccessible1"				;[Cow]

  0,  0, "t.l1.grassland1"
  0,  0, "t.l1.hills1"
  0,  0, "t.l1.forest1"
  0,  0, "t.l1.mountains1"
  0,  0, "t.l1.desert1"
  0,  0, "t.l1.jungle1"
  0,  0, "t.l1.plains1"
  0,  0, "t.l1.swamp1"
  0,  0, "t.l1.tundra1"

  0,  0, "t.l2.grassland1"
  0,  0, "t.l2.hills1"
  0,  0, "t.l2.forest1"
  0,  0, "t.l2.mountains1"
  0,  0, "t.l2.arctic1"
  0,  0, "t.l2.jungle1"
  0,  0, "t.l2.plains1"
  0,  0, "t.l2.swamp1"
  0,  0, "t.l2.tundra1"

; Desert Embellishments
; [TR]
  1,  0, "t.l2.desert1"
  1,  0, "t.l2.desert2"
  1,  0, "t.l2.desert3"
  1,  0, "t.l2.desert4"
  1,  0, "t.l2.desert5"
  1,  0, "t.l2.desert6"
  1,  0, "t.l2.desert7"
  1,  0, "t.l2.desert8"
  1,  0, "t.l2.desert9"
  1,  1, "t.l2.desert10"
  1,  0, "t.l2.desert11"
  1,  0, "t.l2.desert12"
  1,  0, "t.l2.desert13"
  1,  0, "t.l2.desert14"
  1,  0, "t.l2.desert15"
  1,  0, "t.l2.desert16"
  1,  0, "t.l2.desert17"
  1,  0, "t.l2.desert18"
  1,  0, "t.l2.desert19"
  1,  2, "t.l2.desert20"
  1,  0, "t.l2.desert21"
  1,  0, "t.l2.desert22"
  1,  0, "t.l2.desert23"
  1,  0, "t.l2.desert24"
  1,  0, "t.l2.desert25"
  1,  0, "t.l2.desert26"
  1,  0, "t.l2.desert27"
  1,  0, "t.l2.desert28"
  1,  0, "t.l2.desert29"
  1,  3, "t.l2.desert30"
  1,  0, "t.l2.desert31"
  1,  0, "t.l2.desert32"
  1,  0, "t.l2.desert33"
  1,  0, "t.l2.desert34"
  1,  0, "t.l2.desert35"
  1,  0, "t.l2.desert36"
  1,  0, "t.l2.desert37"
  1,  0, "t.l2.desert38"
  1,  0, "t.l2.desert39"
  1,  4, "t.l2.desert40"
  1,  0, "t.l2.desert41"
  1,  0, "t.l2.desert42"
  1,  0, "t.l2.desert43"
  1,  0, "t.l2.desert44"
  1,  0, "t.l2.desert45"
  1,  0, "t.l2.desert46"
  1,  0, "t.l2.desert47"
  1,  0, "t.l2.desert48"
  1,  0, "t.l2.desert49"
  1,  5, "t.l2.desert50"
  1,  0, "t.l2.desert51"
  1,  0, "t.l2.desert52"
  1,  0, "t.l2.desert53"
  1,  0, "t.l2.desert54"
  1,  0, "t.l2.desert55"
  1,  0, "t.l2.desert56"
  1,  0, "t.l2.desert57"
  1,  0, "t.l2.desert58"
  1,  0, "t.l2.desert59"
  1,  6, "t.l2.desert60"
  1,  0, "t.l2.desert61"
  1,  0, "t.l2.desert62"
  1,  0, "t.l2.desert63"
  1,  0, "t.l2.desert64"
  1,  0, "t.l2.desert65"
  1,  0, "t.l2.desert66"
  1,  0, "t.l2.desert67"
  1,  0, "t.l2.desert68"
  1,  0, "t.l2.desert69"
  1,  7, "t.l2.desert70"
  1,  0, "t.l2.desert71"
  1,  0, "t.l2.desert72"
  1,  0, "t.l2.desert73"
  1,  0, "t.l2.desert74"
  1,  0, "t.l2.desert75"
  1,  0, "t.l2.desert76"
  1,  0, "t.l2.desert77"
  1,  0, "t.l2.desert78"
  1,  0, "t.l2.desert79"
  1,  8, "t.l2.desert80"
  1,  0, "t.l2.desert81"
  1,  0, "t.l2.desert82"
  1,  0, "t.l2.desert83"
  1,  0, "t.l2.desert84"
  1,  0, "t.l2.desert85"
  1,  0, "t.l2.desert86"
  1,  0, "t.l2.desert87"
  1,  0, "t.l2.desert88"
  1,  0, "t.l2.desert89"
  1,  9, "t.l2.desert90"
  1,  0, "t.l2.desert91"
  1,  0, "t.l2.desert92"
  1,  0, "t.l2.desert93"
  1,  0, "t.l2.desert94"
  1,  0, "t.l2.desert95"
  1,  0, "t.l2.desert96"
  1,  0, "t.l2.desert97"
  1,  0, "t.l2.desert98"
  1,  0, "t.l2.desert99"
  1, 10, "t.l2.desert100"
  1,  0, "t.l2.desert101"
  1,  0, "t.l2.desert102"
  1,  0, "t.l2.desert103"
  1,  0, "t.l2.desert104"
  1,  0, "t.l2.desert105"
  1,  0, "t.l2.desert106"
  1,  0, "t.l2.desert107"
  1,  0, "t.l2.desert108"
  1,  0, "t.l2.desert109"
  1, 11, "t.l2.desert110"
  1,  0, "t.l2.desert111"
  1,  0, "t.l2.desert112"
  1,  0, "t.l2.desert113"
  1,  0, "t.l2.desert114"
  1,  0, "t.l2.desert115"
  1,  0, "t.l2.desert116"
  1,  0, "t.l2.desert117"
  1,  0, "t.l2.desert118"
  1,  0, "t.l2.desert119"
  1, 12, "t.l2.desert120"
  1,  0, "t.l2.desert121"
  1,  0, "t.l2.desert122"
  1,  0, "t.l2.desert123"
  1,  0, "t.l2.desert124"
  1,  0, "t.l2.desert125"
  1,  0, "t.l2.desert126"
  1,  0, "t.l2.desert127"
  1,  0, "t.l2.desert128"
  1,  0, "t.l2.desert129"
  1, 13, "t.l2.desert130"
  1,  0, "t.l2.desert131"
  1,  0, "t.l2.desert132"
  1,  0, "t.l2.desert133"
  1,  0, "t.l2.desert134"
  1,  0, "t.l2.desert135"
  1,  0, "t.l2.desert136"
  1,  0, "t.l2.desert137"
  1,  0, "t.l2.desert138"
  1,  0, "t.l2.desert139"
  1, 14, "t.l2.desert140"
  1,  0, "t.l2.desert141"
  1,  0, "t.l2.desert142"
  1,  0, "t.l2.desert143"
  1,  0, "t.l2.desert144"
  1,  0, "t.l2.desert145"
  1,  0, "t.l2.desert146"
  1,  0, "t.l2.desert147"
  1,  0, "t.l2.desert148"
  1,  0, "t.l2.desert149"
  1, 15, "t.l2.desert150"
  1,  0, "t.l2.desert151"
  1,  0, "t.l2.desert152"
  1,  0, "t.l2.desert153"
  1,  0, "t.l2.desert154"
  1,  0, "t.l2.desert155"
  1,  0, "t.l2.desert156"
  1,  0, "t.l2.desert157"
  1,  0, "t.l2.desert158"
  1,  0, "t.l2.desert159"
  
; Arctic Ice Shelf
; [TR]?[GS]
  2,  0, "t.l1.arctic_n1e1s1w1"
  2,  1, "t.l1.arctic_n0e1s1w1"
  2,  2, "t.l1.arctic_n1e0s1w1"
  2,  3, "t.l1.arctic_n0e0s1w1"
  2,  4, "t.l1.arctic_n1e1s0w1"
  2,  5, "t.l1.arctic_n0e1s0w1"
  2,  6, "t.l1.arctic_n1e0s0w1"
  2,  7, "t.l1.arctic_n0e0s0w1"
  2,  8, "t.l1.arctic_n1e1s1w0"
  2,  9, "t.l1.arctic_n0e1s1w0"
  2, 10, "t.l1.arctic_n1e0s1w0"
  2, 11, "t.l1.arctic_n0e0s1w0"
  2, 12, "t.l1.arctic_n1e1s0w0"
  2, 13, "t.l1.arctic_n0e1s0w0"
  2, 14, "t.l1.arctic_n1e0s0w0"
  2, 15, "t.l1.arctic_n0e0s0w0"

; Forest, and whether terrain to north, south, east, west 
; is more forest.

  3,  0, "t.l1.forest_n1e1s1w1"
  3,  1, "t.l1.forest_n0e1s1w1"
  3,  2, "t.l1.forest_n1e0s1w1"
  3,  3, "t.l1.forest_n0e0s1w1"
  3,  4, "t.l1.forest_n1e1s0w1"
  3,  5, "t.l1.forest_n0e1s0w1"
  3,  6, "t.l1.forest_n1e0s0w1"
  3,  7, "t.l1.forest_n0e0s0w1"
  3,  8, "t.l1.forest_n1e1s1w0"
  3,  9, "t.l1.forest_n0e1s1w0"
  3, 10, "t.l1.forest_n1e0s1w0"
  3, 11, "t.l1.forest_n0e0s1w0"
  3, 12, "t.l1.forest_n1e1s0w0"
  3, 13, "t.l1.forest_n0e1s0w0"
  3, 14, "t.l1.forest_n1e0s0w0"
  3, 15, "t.l1.forest_n0e0s0w0"

; Hills, and whether terrain to north, south, east, west 
; is more hills.

  4,  0, "t.l1.hills_n1e1s1w1"
  4,  1, "t.l1.hills_n0e1s1w1"
  4,  2, "t.l1.hills_n1e0s1w1"
  4,  3, "t.l1.hills_n0e0s1w1"
  4,  4, "t.l1.hills_n1e1s0w1"
  4,  5, "t.l1.hills_n0e1s0w1"
  4,  6, "t.l1.hills_n1e0s0w1"
  4,  7, "t.l1.hills_n0e0s0w1"
  4,  8, "t.l1.hills_n1e1s1w0"
  4,  9, "t.l1.hills_n0e1s1w0"
  4, 10, "t.l1.hills_n1e0s1w0"
  4, 11, "t.l1.hills_n0e0s1w0"
  4, 12, "t.l1.hills_n1e1s0w0"
  4, 13, "t.l1.hills_n0e1s0w0"
  4, 14, "t.l1.hills_n1e0s0w0"
  4, 15, "t.l1.hills_n0e0s0w0"

; Mountains, and whether terrain to north, south, east, west 
; is more mountains.

  5,  0, "t.l1.mountains_n1e1s1w1"
  5,  1, "t.l1.mountains_n0e1s1w1"
  5,  2, "t.l1.mountains_n1e0s1w1"
  5,  3, "t.l1.mountains_n0e0s1w1"
  5,  4, "t.l1.mountains_n1e1s0w1"
  5,  5, "t.l1.mountains_n0e1s0w1"
  5,  6, "t.l1.mountains_n1e0s0w1"
  5,  7, "t.l1.mountains_n0e0s0w1"
  5,  8, "t.l1.mountains_n1e1s1w0"
  5,  9, "t.l1.mountains_n0e1s1w0"
  5, 10, "t.l1.mountains_n1e0s1w0"
  5, 11, "t.l1.mountains_n0e0s1w0"
  5, 12, "t.l1.mountains_n1e1s0w0"
  5, 13, "t.l1.mountains_n0e1s0w0"
  5, 14, "t.l1.mountains_n1e0s0w0"
  5, 15, "t.l1.mountains_n0e0s0w0"

; Ocean, and whether terrain to north, south, east, west 
; is more ocean (else shoreline)

; [TR]?[GS]
  6,  0, "t.l1.coast_n1e1s1w1"
  6,  1, "t.l1.coast_n0e1s1w1"
  6,  2, "t.l1.coast_n1e0s1w1"
  6,  3, "t.l1.coast_n0e0s1w1"
  6,  4, "t.l1.coast_n1e1s0w1"
  6,  5, "t.l1.coast_n0e1s0w1"
  6,  6, "t.l1.coast_n1e0s0w1"
  6,  7, "t.l1.coast_n0e0s0w1"
  6,  8, "t.l1.coast_n1e1s1w0"
  6,  9, "t.l1.coast_n0e1s1w0"
  6,  10, "t.l1.coast_n1e0s1w0"
  6,  11, "t.l1.coast_n0e0s1w0"
  6,  12, "t.l1.coast_n1e1s0w0"
  6,  13, "t.l1.coast_n0e1s0w0"
  6,  14, "t.l1.coast_n1e0s0w0"
  6,  15, "t.l1.coast_n0e0s0w0"

; [TR]?[GS]
  6,  0, "t.l1.floor_n1e1s1w1"
  6,  1, "t.l1.floor_n0e1s1w1"
  6,  2, "t.l1.floor_n1e0s1w1"
  6,  3, "t.l1.floor_n0e0s1w1"
  6,  4, "t.l1.floor_n1e1s0w1"
  6,  5, "t.l1.floor_n0e1s0w1"
  6,  6, "t.l1.floor_n1e0s0w1"
  6,  7, "t.l1.floor_n0e0s0w1"
  6,  8, "t.l1.floor_n1e1s1w0"
  6,  9, "t.l1.floor_n0e1s1w0"
  6,  10, "t.l1.floor_n1e0s1w0"
  6,  11, "t.l1.floor_n0e0s1w0"
  6,  12, "t.l1.floor_n1e1s0w0"
  6,  13, "t.l1.floor_n0e1s0w0"
  6,  14, "t.l1.floor_n1e0s0w0"
  6,  15, "t.l1.floor_n0e0s0w0"

; [TR]?[GS]
  6,  0, "t.l1.lake_n1e1s1w1"
  6,  1, "t.l1.lake_n0e1s1w1"
  6,  2, "t.l1.lake_n1e0s1w1"
  6,  3, "t.l1.lake_n0e0s1w1"
  6,  4, "t.l1.lake_n1e1s0w1"
  6,  5, "t.l1.lake_n0e1s0w1"
  6,  6, "t.l1.lake_n1e0s0w1"
  6,  7, "t.l1.lake_n0e0s0w1"
  6,  8, "t.l1.lake_n1e1s1w0"
  6,  9, "t.l1.lake_n0e1s1w0"
  6,  10, "t.l1.lake_n1e0s1w0"
  6,  11, "t.l1.lake_n0e0s1w0"
  6,  12, "t.l1.lake_n1e1s0w0"
  6,  13, "t.l1.lake_n0e1s0w0"
  6,  14, "t.l1.lake_n1e0s0w0"
  6,  15, "t.l1.lake_n0e0s0w0"

; [TR]?[GS]
  6,  0, "t.l1.inaccessible_n1e1s1w1"
  6,  1, "t.l1.inaccessible_n0e1s1w1"
  6,  2, "t.l1.inaccessible_n1e0s1w1"
  6,  3, "t.l1.inaccessible_n0e0s1w1"
  6,  4, "t.l1.inaccessible_n1e1s0w1"
  6,  5, "t.l1.inaccessible_n0e1s0w1"
  6,  6, "t.l1.inaccessible_n1e0s0w1"
  6,  7, "t.l1.inaccessible_n0e0s0w1"
  6,  8, "t.l1.inaccessible_n1e1s1w0"
  6,  9, "t.l1.inaccessible_n0e1s1w0"
  6,  10, "t.l1.inaccessible_n1e0s1w0"
  6,  11, "t.l1.inaccessible_n0e0s1w0"
  6,  12, "t.l1.inaccessible_n1e1s0w0"
  6,  13, "t.l1.inaccessible_n0e1s0w0"
  6,  14, "t.l1.inaccessible_n1e0s0w0"
  6,  15, "t.l1.inaccessible_n0e0s0w0"

; Ice Shelves

; [TR]?[GS]
  7,   0, "t.l2.coast_n1e1s1w1"
  7,   1, "t.l2.coast_n0e1s1w1"
  7,   2, "t.l2.coast_n1e0s1w1"
  7,   3, "t.l2.coast_n0e0s1w1"
  7,   4, "t.l2.coast_n1e1s0w1"
  7,   5, "t.l2.coast_n0e1s0w1"
  7,   6, "t.l2.coast_n1e0s0w1"
  7,   7, "t.l2.coast_n0e0s0w1"
  7,   8, "t.l2.coast_n1e1s1w0"
  7,   9, "t.l2.coast_n0e1s1w0"
  7,  10, "t.l2.coast_n1e0s1w0"
  7,  11, "t.l2.coast_n0e0s1w0"
  7,  12, "t.l2.coast_n1e1s0w0"
  7,  13, "t.l2.coast_n0e1s0w0"
  7,  14, "t.l2.coast_n1e0s0w0"
  7,  15, "t.l2.coast_n0e0s0w0"


; [TR]?[GS]
  7,   0, "t.l2.floor_n1e1s1w1"
  7,   1, "t.l2.floor_n0e1s1w1"
  7,   2, "t.l2.floor_n1e0s1w1"
  7,   3, "t.l2.floor_n0e0s1w1"
  7,   4, "t.l2.floor_n1e1s0w1"
  7,   5, "t.l2.floor_n0e1s0w1"
  7,   6, "t.l2.floor_n1e0s0w1"
  7,   7, "t.l2.floor_n0e0s0w1"
  7,   8, "t.l2.floor_n1e1s1w0"
  7,   9, "t.l2.floor_n0e1s1w0"
  7,  10, "t.l2.floor_n1e0s1w0"
  7,  11, "t.l2.floor_n0e0s1w0"
  7,  12, "t.l2.floor_n1e1s0w0"
  7,  13, "t.l2.floor_n0e1s0w0"
  7,  14, "t.l2.floor_n1e0s0w0"
  7,  15, "t.l2.floor_n0e0s0w0"


; [TR]?[GS]
  7,   0, "t.l2.lake_n1e1s1w1"
  7,   1, "t.l2.lake_n0e1s1w1"
  7,   2, "t.l2.lake_n1e0s1w1"
  7,   3, "t.l2.lake_n0e0s1w1"
  7,   4, "t.l2.lake_n1e1s0w1"
  7,   5, "t.l2.lake_n0e1s0w1"
  7,   6, "t.l2.lake_n1e0s0w1"
  7,   7, "t.l2.lake_n0e0s0w1"
  7,   8, "t.l2.lake_n1e1s1w0"
  7,   9, "t.l2.lake_n0e1s1w0"
  7,  10, "t.l2.lake_n1e0s1w0"
  7,  11, "t.l2.lake_n0e0s1w0"
  7,  12, "t.l2.lake_n1e1s0w0"
  7,  13, "t.l2.lake_n0e1s0w0"
  7,  14, "t.l2.lake_n1e0s0w0"
  7,  15, "t.l2.lake_n0e0s0w0"


; [TR]?[GS]
  7,   0, "t.l2.inaccessible_n1e1s1w1"
  7,   1, "t.l2.inaccessible_n0e1s1w1"
  7,   2, "t.l2.inaccessible_n1e0s1w1"
  7,   3, "t.l2.inaccessible_n0e0s1w1"
  7,   4, "t.l2.inaccessible_n1e1s0w1"
  7,   5, "t.l2.inaccessible_n0e1s0w1"
  7,   6, "t.l2.inaccessible_n1e0s0w1"
  7,   7, "t.l2.inaccessible_n0e0s0w1"
  7,   8, "t.l2.inaccessible_n1e1s1w0"
  7,   9, "t.l2.inaccessible_n0e1s1w0"
  7,  10, "t.l2.inaccessible_n1e0s1w0"
  7,  11, "t.l2.inaccessible_n0e0s1w0"
  7,  12, "t.l2.inaccessible_n1e1s0w0"
  7,  13, "t.l2.inaccessible_n0e1s0w0"
  7,  14, "t.l2.inaccessible_n1e0s0w0"
  7,  15, "t.l2.inaccessible_n0e0s0w0"

; Darkness (unexplored) to north, south, east, west 

  0,  6, "mask.tile"
  0,  4, "tx.fog"

; Rivers (as special type), and whether north, south, east, west 
; also has river or is ocean:

; [TR]?[GS]
  8,  0, "road.river_s_n0e0s0w0"
  8,  1, "road.river_s_n1e0s0w0"
  8,  2, "road.river_s_n0e1s0w0"
  8,  3, "road.river_s_n1e1s0w0"
  8,  4, "road.river_s_n0e0s1w0"
  8,  5, "road.river_s_n1e0s1w0"
  8,  6, "road.river_s_n0e1s1w0"
  8,  7, "road.river_s_n1e1s1w0"
  8,  8, "road.river_s_n0e0s0w1"
  8,  9, "road.river_s_n1e0s0w1"
  8, 10, "road.river_s_n0e1s0w1"
  8, 11, "road.river_s_n1e1s0w1"
  8, 12, "road.river_s_n0e0s1w1"
  8, 13, "road.river_s_n1e0s1w1"
  8, 14, "road.river_s_n0e1s1w1"
  8, 15, "road.river_s_n1e1s1w1"

; River outlets, river to north, south, east, west 

; [TR]?
   0,  7, "road.river_outlet_n"
   0,  8, "road.river_outlet_w"
   0,  9, "road.river_outlet_s"
   0, 10, "road.river_outlet_e"

; Terrain special resources:

; [??]
  9,  0, "ts.spice"
  9,  1, "ts.furs"
  9,  2, "ts.peat"
  9,  3, "ts.arctic_ivory"
  9,  4, "ts.fruit"
  9,  5, "ts.iron"
  9,  6, "ts.whales"
  9,  7, "ts.wheat"
  9,  8, "ts.pheasant"
  9,  9, "ts.buffalo"
  9, 10, "ts.silk"
  9, 11, "ts.wine"

; [??]
 10,  0, "ts.seals"
 10,  1, "ts.oasis"
 10,  2, "ts.forest_game"
 10,  3, "ts.grassland_resources", "ts.river_resources"
 10,  4, "ts.coal"
 10,  5, "ts.gems"
 10,  6, "ts.gold"
 10,  7, "ts.fish"
 10,  8, "ts.oil", "ts.arctic_oil"
 10,  9, "ts.tundra_game"

; Terrain Strategic Resources

 10, 10, "ts.saltpeter"				;(Amplio Coal)
 10, 11, "ts.aluminum"				;(Amplio Iron)
 10, 12, "ts.uranium"				;(Amplio Gold)
 10, 13, "ts.horses"				;(Amplio Horses)
 10, 14, "ts.elephant"				;[AF]
 10, 15, "ts.rubber"				;[GS]

; Terrain improvements and similar:

 11,  0, "tx.farmland"				;[GS]
 11,  1, "tx.irrigation"			;[GS]
 11,  2, "tx.mine"					;[BFW]
 11,  3, "tx.oil_mine"				;[??]
 11,  4, "tx.oil_rig"				;[??][GS]
 11,  5, "tx.pollution"				;[??]
 11,  6, "tx.sea_pollution"			;[??][GS]
 11,  7, "tx.fallout"				;{??}

; Bases

 11,  9, "base.buoy_mg"				; [El]
 11, 10, "base.airstrip_mg"			; [HH][GS]
 11, 11, "base.airbase_mg"			; [HH]
 11, 12, "base.outpost_fg"			; [TR]?[GS]
 11, 13, "base.outpost_bg"			; [TR]?[GS]
 11, 14, "base.fortress_fg"			; [HH]?[GS]
 11, 15, "base.fortress_bg"			; [HH]?[GS]

; Misc

  9, 12, "tx.village"				; [BFW][GS]
  9, 13, "base.ruins_mg"			; [BFW][GS]

}
