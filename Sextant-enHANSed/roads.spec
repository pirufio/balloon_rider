
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
		David Pfitzner <dwp@mso.anu.edu.au> [DP]
		GriffonSpade [GS]
"

[file]
gfx = "Sextant-enHANSed/roads"

[grid_roads]

x_top_left = 1
y_top_left = 1
dx = 60
dy = 60
pixel_border = 1

tiles = { "row", "column", "tag"

; Roads

; [DP][GS]
 0, 0, "road.road_isolated"
 0, 1, "road.road_n"
 0, 2, "road.road_ne"
 0, 3, "road.road_e"
 0, 4, "road.road_se"
 0, 5, "road.road_s"
 0, 6, "road.road_sw"
 0, 7, "road.road_w"
 0, 8, "road.road_nw"

; Road corners

  0,  9, "road.road_c_nw"
  0, 10, "road.road_c_ne"
  0, 11, "road.road_c_sw"
  0, 12, "road.road_c_se"

; Railroads

; [GS]
 1, 0, "road.rail_isolated"
 1, 1, "road.rail_n"
 1, 2, "road.rail_ne"
 1, 3, "road.rail_e"
 1, 4, "road.rail_se"
 1, 5, "road.rail_s"
 1, 6, "road.rail_sw"
 1, 7, "road.rail_w"
 1, 8, "road.rail_nw"

; Railroad corners

  1,  9, "road.rail_c_nw"
  1, 10, "road.rail_c_ne"
  1, 11, "road.rail_c_sw"
  1, 12, "road.rail_c_se"

; Maglev

; [GS]
; Maglev isolated

 2,   0, "road.maglev_isolated"

; Cardinal maglevs, connections north, south, east, west:

 2,   1, "road.maglev_c_n1e0s0w0"
 2,   2, "road.maglev_c_n0e1s0w0"
 2,   3, "road.maglev_c_n1e1s0w0"
 2,   4, "road.maglev_c_n0e0s1w0"
 2,   5, "road.maglev_c_n1e0s1w0"
 2,   6, "road.maglev_c_n0e1s1w0"
 2,   7, "road.maglev_c_n1e1s1w0"
 2,   8, "road.maglev_c_n0e0s0w1"
 2,   9, "road.maglev_c_n1e0s0w1"
 2,  10, "road.maglev_c_n0e1s0w1"
 2,  11, "road.maglev_c_n1e1s0w1"
 2,  12, "road.maglev_c_n0e0s1w1"
 2,  13, "road.maglev_c_n1e0s1w1"
 2,  14, "road.maglev_c_n0e1s1w1"
 2,  15, "road.maglev_c_n1e1s1w1"

; Diagonal maglevs, connections same, rotated 45 degrees clockwise:

 3,   1, "road.maglev_d_ne1se0sw0nw0"
 3,   2, "road.maglev_d_ne0se1sw0nw0"
 3,   3, "road.maglev_d_ne1se1sw0nw0"
 3,   4, "road.maglev_d_ne0se0sw1nw0"
 3,   5, "road.maglev_d_ne1se0sw1nw0"
 3,   6, "road.maglev_d_ne0se1sw1nw0"
 3,   7, "road.maglev_d_ne1se1sw1nw0"
 3,   8, "road.maglev_d_ne0se0sw0nw1"
 3,   9, "road.maglev_d_ne1se0sw0nw1"
 3,  10, "road.maglev_d_ne0se1sw0nw1"
 3,  11, "road.maglev_d_ne1se1sw0nw1"
 3,  12, "road.maglev_d_ne0se0sw1nw1"
 3,  13, "road.maglev_d_ne1se0sw1nw1"
 3,  14, "road.maglev_d_ne0se1sw1nw1"
 3,  15, "road.maglev_d_ne1se1sw1nw1"

; Maglev corners

  0, 14, "road.maglev_c_nw"
  0, 15, "road.maglev_c_ne"
  1, 14, "road.maglev_c_sw"
  1, 15, "road.maglev_c_se"

; Highways

; [GS]
 4, 0, "road.highway_isolated"
 4, 1, "road.highway_n"
 4, 2, "road.highway_ne"
 4, 3, "road.highway_e"
 4, 4, "road.highway_se"
 4, 5, "road.highway_s"
 4, 6, "road.highway_sw"
 4, 7, "road.highway_w"
 4, 8, "road.highway_nw"

; Highway corners

  4,  9, "road.highway_c_nw"
  4, 10, "road.highway_c_ne"
  4, 11, "road.highway_c_sw"
  4, 12, "road.highway_c_se"


}
