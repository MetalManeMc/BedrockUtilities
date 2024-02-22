# Created by MetalManeMc
# You may use and modify without restrictions, but you must keep this disclaimer intact when sharing

from json import dumps

bone_rules = {
    "normaln": "q.block_property('cbw:direction') == 0 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == false)",
    "upsiden": "q.block_property('cbw:direction') == 0 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == true)",
    "normals": "q.block_property('cbw:direction') == 1 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == false)",
    "upsides": "q.block_property('cbw:direction') == 1 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == true)",
    "normalw": "q.block_property('cbw:direction') == 2 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == false)",
    "upsidew": "q.block_property('cbw:direction') == 2 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == true)",
    "normale": "q.block_property('cbw:direction') == 3 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == false)",
    "upsidee": "q.block_property('cbw:direction') == 3 && (q.block_property('cbw:shape') == 'straight' && q.block_property('cbw:upside_down') == true)",
    "inner_right0": "(q.block_property('cbw:direction') == 0 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'inner_right')) || (q.block_property('cbw:direction') == 3 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'inner_left'))",
    "inner_left0": "(q.block_property('cbw:direction') == 0 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'inner_left')) || (q.block_property('cbw:direction') == 2 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'inner_right'))",
    "inner_right1": "(q.block_property('cbw:direction') == 1 || q.block_property('cbw:direction') == 3) && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'inner_right')",
    "inner_left1": "(q.block_property('cbw:direction') == 1 || q.block_property('cbw:direction') == 2) && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'inner_left')",
    "outer_right0": "(q.block_property('cbw:direction') == 0 || q.block_property('cbw:direction') == 2) && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'outer_right')",
    "outer_left0": "(q.block_property('cbw:direction') == 0 || q.block_property('cbw:direction') == 3) && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'outer_left')",
    "outer_right1": "(q.block_property('cbw:direction') == 1 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'outer_right')) || (q.block_property('cbw:direction') == 2 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'outer_left'))",
    "outer_left1": "(q.block_property('cbw:direction') == 1 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'outer_left')) || (q.block_property('cbw:direction') == 3 && (q.block_property('cbw:upside_down') == false && q.block_property('cbw:shape') == 'outer_right'))",
    "inner_right0u": "(q.block_property('cbw:direction') == 0 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'inner_right')) || (q.block_property('cbw:direction') == 3 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'inner_left'))",
    "inner_left0u": "(q.block_property('cbw:direction') == 0 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'inner_left')) || (q.block_property('cbw:direction') == 2 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'inner_right'))",
    "inner_right1u": "(q.block_property('cbw:direction') == 1 || q.block_property('cbw:direction') == 3) && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'inner_right')",
    "inner_left1u": "(q.block_property('cbw:direction') == 1 || q.block_property('cbw:direction') == 2) && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'inner_left')",
    "outer_right0u": "(q.block_property('cbw:direction') == 0 || q.block_property('cbw:direction') == 2) && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'outer_right')",
    "outer_left0u": "(q.block_property('cbw:direction') == 0 || q.block_property('cbw:direction') == 3) && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'outer_left')",
    "outer_right1u": "(q.block_property('cbw:direction') == 1 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'outer_right')) || (q.block_property('cbw:direction') == 2 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'outer_left'))",
    "outer_left1u": "(q.block_property('cbw:direction') == 1 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'outer_left')) || (q.block_property('cbw:direction') == 3 && (q.block_property('cbw:upside_down') == true && q.block_property('cbw:shape') == 'outer_right'))"
}
identifier = "geometry.custom_stairs"

res = []

base = {i[0]: False for i in bone_rules.items()}

for x in bone_rules.items():
    adaptation = {i[0]: i[1] for i in base.items()}
    del adaptation[x[0]]
    append = {
        "condition": x[1],
        "components": {
            "minecraft:geometry": {
                "identifier": identifier,
                "bone_visibility": adaptation
            }
        }
    }
    res.append(append)

open(identifier+".txt", "w").write(dumps(res, indent="    ")[1:-1])
print("{"+'"identifier":"'+identifier+'","bone_visibility":'+dumps(base)+"}")
