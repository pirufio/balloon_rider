
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.5-spec"

[info]

artists = "
		Hans Lemurson (Yield Icons) [HL]
"

[file]
gfx = "Sextant-enHANSed/extras"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 60
dy = 60
pixel_border = 1

tiles = { "row", "column", "tag"
; Numbers: city size: (also used for goto)

  0,  0, "city.size_0"
  0,  1, "city.size_1"
  0,  2, "city.size_2"
  0,  3, "city.size_3"
  0,  4, "city.size_4"
  0,  5, "city.size_5"
  0,  6, "city.size_6"
  0,  7, "city.size_7"
  0,  8, "city.size_8"
  0,  9, "city.size_9"
  1,  0, "city.size_00"
  1,  1, "city.size_10"
  1,  2, "city.size_20"
  1,  3, "city.size_30"
  1,  4, "city.size_40"
  1,  5, "city.size_50"
  1,  6, "city.size_60"
  1,  7, "city.size_70"
  1,  8, "city.size_80"
  1,  9, "city.size_90"
  2,  1, "city.size_100"
  2,  2, "city.size_200"
  2,  3, "city.size_300"
  2,  4, "city.size_400"
  2,  5, "city.size_500"
  2,  6, "city.size_600"
  2,  7, "city.size_700"
  2,  8, "city.size_800"
  2,  9, "city.size_900"

; Numbers: city tile food/shields/trade y/g/b

  3,  0, "city.t_food_0"
  3,  1, "city.t_food_1"
  3,  2, "city.t_food_2"
  3,  3, "city.t_food_3"
  3,  4, "city.t_food_4"
  3,  5, "city.t_food_5"
  3,  6, "city.t_food_6"
  3,  7, "city.t_food_7"
  3,  8, "city.t_food_8"
  3,  9, "city.t_food_9"

  4,  0, "city.t_shields_0"
  4,  1, "city.t_shields_1"
  4,  2, "city.t_shields_2"
  4,  3, "city.t_shields_3"
  4,  4, "city.t_shields_4"
  4,  5, "city.t_shields_5"
  4,  6, "city.t_shields_6"
  4,  7, "city.t_shields_7"
  4,  8, "city.t_shields_8"
  4,  9, "city.t_shields_9"

  5,  0, "city.t_trade_0"
  5,  1, "city.t_trade_1"
  5,  2, "city.t_trade_2"
  5,  3, "city.t_trade_3"
  5,  4, "city.t_trade_4"
  5,  5, "city.t_trade_5"
  5,  6, "city.t_trade_6"
  5,  7, "city.t_trade_7"
  5,  8, "city.t_trade_8"
  5,  9, "city.t_trade_9"

; Unit hit-point bars: approx percent of hp remaining

  6,   0, "unit.hp_100"
  6,   1, "unit.hp_90"
  6,   2, "unit.hp_80"
  6,   3, "unit.hp_70"
  6,   4, "unit.hp_60"
  6,   5, "unit.hp_50"
  6,   6, "unit.hp_40"
  6,   7, "unit.hp_30"
  6,   8, "unit.hp_20"
  6,   9, "unit.hp_10"
  7,   9, "unit.hp_0"

; Veteran Levels: up to 9 military honors for experienced units

  7,  0, "unit.vet_1"
  7,  1, "unit.vet_2"
  7,  2, "unit.vet_3"
  7,  3, "unit.vet_4"
  7,  4, "unit.vet_5"
  7,  5, "unit.vet_6"
  7,  6, "unit.vet_7"
  7,  7, "unit.vet_8"
  7,  8, "unit.vet_9"

  ; Unit Misc:

  8,  0, "unit.tired"
  8,  1, "unit.lowfuel"
  8,  2, "unit.stack"
  8,  3, "unit.loaded"
  8,  4, "user.attention"


}
