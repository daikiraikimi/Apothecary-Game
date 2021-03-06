#Remember, no herbs will show up unless you have read the herb identification book that unlocks them. 
#If the forest is empty, check this first before thinking there is a bug.



##############################################################################
# Forest One
#
# Collect herbs. Cool, Rocky.

label forest_loop:
    $ renpy.pause()
    jump forest_loop

label forest001_layout:
    $ forest001_spawn = renpy.random.randint(1, 5)
    

label forest001:
    init python: 
        message = "message"
    
    $ current_loc = "forest001"
    
    scene bg forest001
    show screen forest001
    show screen basic_overlay
    
#    "Your random number is [forest001_spawn]."

    hide screen forest001
    call check_events
    show screen forest001
    jump forest_loop


screen forest001:
    tag menu2
    
    if forest001_spawn == 1:
    
        if herbID3 in shelf.list_books() and forest001_poppy_col:
            imagebutton:
                idle "gui/inv/herb021_idle.png"
                hover "gui/inv/herb021_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_poppy_col", False), Jump("forest001_poppy") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest001_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_stjohns_col", False), Jump("forest001_stjohns") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest001_rosemary_col:
            imagebutton:
                idle "gui/inv/herb019_idle.png"
                hover "gui/inv/herb019_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_rosemary_col", False), Jump("forest001_rosemary") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest001_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_mint_col", False), Jump("forest001_mint") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest001_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_chamomile_col", False), Jump("forest001_chamomile") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest001_spawn == 2:
        
        if herbID1 in shelf.list_books() and forest001_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_thistle_col", False), Jump("forest001_thistle") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest001_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_oregano_col", False), Jump("forest001_oregano") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest001_licorice_col:
            imagebutton:
                idle "gui/inv/herb030_idle.png"
                hover "gui/inv/herb030_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_licorice_col", False), Jump("forest001_licorice") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest001_redclover_col:
            imagebutton:
                idle "gui/inv/herb023_idle.png"
                hover "gui/inv/herb023_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_redclover_col", False), Jump("forest001_redclover") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest001_poppy_col:
            imagebutton:
                idle "gui/inv/herb021_idle.png"
                hover "gui/inv/herb021_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_poppy_col", False), Jump("forest001_poppy") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
                
    if forest001_spawn == 3:
    
        if herbID1 in shelf.list_books() and forest001_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_blackberry_col", False), Jump("forest001_blackberry") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest001_garlic_col:
            imagebutton:
                idle "gui/inv/herb005_idle.png"
                hover "gui/inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_garlic_col", False), Jump("forest001_garlic") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest001_mullein_col:
            imagebutton:
                idle "gui/inv/herb022_idle.png"
                hover "gui/inv/herb022_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_mullein_col", False), Jump("forest001_mullein") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest001_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_oak_col", False), Jump("forest001_oak") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest001_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_thistle_col", False), Jump("forest001_thistle") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
                
    if forest001_spawn == 4:
    
        if herbID3 in shelf.list_books() and forest001_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_burdock_col", False), Jump("forest001_burdock") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest001_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_stjohns_col", False), Jump("forest001_stjohns") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest001_poppy_col:
            imagebutton:
                idle "gui/inv/herb021_idle.png"
                hover "gui/inv/herb021_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_poppy_col", False), Jump("forest001_poppy") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
            
            
        if herbID2 in shelf.list_books() and forest001_hyssop_col:
            imagebutton:
                idle "gui/inv/herb011_idle.png"
                hover "gui/inv/herb011_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_hyssop_col", False), Jump("forest001_hyssop") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest001_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_mint_col", False), Jump("forest001_mint") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
    
    if forest001_spawn == 5:
    
        if herbID3 in shelf.list_books() and forest001_mullein_col:
            imagebutton:
                idle "gui/inv/herb022_idle.png"
                hover "gui/inv/herb022_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_mullein_col", False), Jump("forest001_mullein") ]
                xpos 800 ypos 320
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest001_borage_col:
            imagebutton:
                idle "gui/inv/herb012_idle.png"
                hover "gui/inv/herb012_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_borage_col", False), Jump("forest001_borage") ]
                xpos 600 ypos 390
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest001_sage_col:
            imagebutton:
                idle "gui/inv/herb009_idle.png"
                hover "gui/inv/herb009_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_sage_col", False), Jump("forest001_sage") ]
                xpos 1120 ypos 480
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest001_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_blackberry_col", False), Jump("forest001_blackberry") ]
                xpos 200 ypos 330
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest001_redclover_col:
            imagebutton:
                idle "gui/inv/herb023_idle.png"
                hover "gui/inv/herb023_hover.png"
                focus_mask True
                clicked [ SetVariable("forest001_redclover_col", False), Jump("forest001_redclover") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
    
label forest001_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest001
    
label forest001_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest001
    
label forest001_oak:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Oak",item="Oak")
    
    jump forest001
    
label forest001_garlic:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest001
    
label forest001_mint:
    $ player_bag.add_item("herb006", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest001
    
label forest001_oregano:
    $ player_bag.add_item("herb007", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest001
    
label forest001_chamomile:
    $ player_bag.add_item("herb016", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Chamomile",item="Chamomile")
    
    jump forest001

label forest001_mullein:
    $ player_bag.add_item("herb022", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Mullein",item="Mullein")
    
    jump forest001

label forest001_redclover:
    $ player_bag.add_item("herb023", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Red Clover",item="Red Clover")
    
    jump forest001

label forest001_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest001

label forest001_burdock:
    $ player_bag.add_item("herb026", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Burdock",item="Burdock")
    
    jump forest001

label forest001_sage:
    $ player_bag.add_item("herb009", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest001

label forest001_hyssop:
    $ player_bag.add_item("herb011", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest001

label forest001_borage:
    $ player_bag.add_item("herb012", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest001

label forest001_rosemary:
    $ player_bag.add_item("herb019", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Rosemary",item="Rosemary")
    
    jump forest001

label forest001_licorice:
    $ player_bag.add_item("herb030", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Licorice",item="Licorice")
    
    jump forest001

label forest001_poppy:
    $ player_bag.add_item("herb021", quality=70, custom_tags=["bitter"])
    $ F1Harvest = True
    show screen inventory_popup2(message="Received Poppy",item="Poppy")
    
    jump forest001

label leave_forest001:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    

##############################################################################
# Forest Two
#
# Collect herbs. Dense, Dry.

label forest002_layout:
    $ forest002_spawn = renpy.random.randint(1, 5)
    

label forest002:
    init python: 
        message = "message"
    
    $ current_loc = "forest002"
    
    scene bg forest002
    show screen forest002
    show screen basic_overlay
    
#    "Your random number is [forest002_spawn]."

    hide screen forest002
    call check_events
    show screen forest002

    jump forest_loop

screen forest002:
    tag menu2
        
    if forest002_spawn == 1:
    
        if herbID2 in shelf.list_books() and forest002_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_chamomile_col", False), Jump("forest002_chamomile") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
        
        if herbID1 in shelf.list_books() and forest002_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_dandelion_col", False), Jump("forest002_dandelion") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest002_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_blackberry_col", False), Jump("forest002_blackberry") ]
                xpos 400 ypos 470
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest002_licorice_col:
            imagebutton:
                idle "gui/inv/herb030_idle.png"
                hover "gui/inv/herb030_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_licorice_col", False), Jump("forest002_licorice") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest002_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_thistle_col", False), Jump("forest002_thistle") ]
                xpos 665 ypos 360
                xanchor 0 yanchor 0
                
    if forest002_spawn == 2:
        
        if herbID3 in shelf.list_books() and forest002_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_burdock_col", False), Jump("forest002_burdock") ]
                xpos 665 ypos 360
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest002_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_blackberry_col", False), Jump("forest002_blackberry") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest002_calendula_col:
            imagebutton:
                idle "gui/inv/herb017_idle.png"
                hover "gui/inv/herb017_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_calendula_col", False), Jump("forest002_calendula") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest002_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_stjohns_col", False), Jump("forest002_stjohns") ]
                xpos 400 ypos 470
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest002_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_chamomile_col", False), Jump("forest002_chamomile") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
                
    if forest002_spawn == 3:
    
        if herbID1 in shelf.list_books() and forest002_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_oak_col", False), Jump("forest002_oak") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest002_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_chamomile_col", False), Jump("forest002_chamomile") ]
                xpos 665 ypos 360
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest002_redclover_col:
            imagebutton:
                idle "gui/inv/herb023_idle.png"
                hover "gui/inv/herb023_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_redclover_col", False), Jump("forest002_redclover") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest002_laurel_col:
            imagebutton:
                idle "gui/inv/herb010_idle.png"
                hover "gui/inv/herb010_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_laurel_col", False), Jump("forest002_laurel") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest002_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_dandelion_col", False), Jump("forest002_dandelion") ]
                xpos 400 ypos 470
                xanchor 0 yanchor 0
                
    if forest002_spawn == 4:
    
        if herbID2 in shelf.list_books() and forest002_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_chamomile_col", False), Jump("forest002_chamomile") ]
                xpos 400 ypos 470
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest002_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_stjohns_col", False), Jump("forest002_stjohns") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest002_parsley_col:
            imagebutton:
                idle "gui/inv/herb008_idle.png"
                hover "gui/inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_parsley_col", False), Jump("forest002_parsley") ]
                xpos 665 ypos 360
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest002_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_oregano_col", False), Jump("forest002_oregano") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest002_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_oak_col", False), Jump("forest002_oak") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
    
    if forest002_spawn == 5:
    
        if herbID2 in shelf.list_books() and forest002_rosemary_col:
            imagebutton:
                idle "gui/inv/herb019_idle.png"
                hover "gui/inv/herb019_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_rosemary_col", False), Jump("forest002_rosemary") ]
                xpos 1000 ypos 550
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest002_hyssop_col:
            imagebutton:
                idle "gui/inv/herb011_idle.png"
                hover "gui/inv/herb011_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_hyssop_col", False), Jump("forest002_hyssop") ]
                xpos 400 ypos 470
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest002_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_burdock_col", False), Jump("forest002_burdock") ]
                xpos 50 ypos 490
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest002_mullein_col:
            imagebutton:
                idle "gui/inv/herb022_idle.png"
                hover "gui/inv/herb022_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_mullein_col", False), Jump("forest002_mullein") ]
                xpos 665 ypos 360
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest002_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest002_chamomile_col", False), Jump("forest002_chamomile") ]
                xpos 800 ypos 400
                xanchor 0 yanchor 0
            
    
label forest002_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest002

label forest002_dandelion:
    $ player_bag.add_item("herb002", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest002
    
label forest002_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest002
    
label forest002_oak:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Oak",item="Oak")
    
    jump forest002
    
label forest002_oregano:
    $ player_bag.add_item("herb007", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest002
    
label forest002_parsley:
    $ player_bag.add_item("herb008", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Parsley",item="Parsley")
    
    jump forest002
    
label forest002_chamomile:
    $ player_bag.add_item("herb016", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Chamomile",item="Chamomile")
    
    jump forest002
    
label forest002_mullein:
    $ player_bag.add_item("herb022", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Mullein",item="Mullein")
    
    jump forest002

label forest002_redclover:
    $ player_bag.add_item("herb023", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Red Clover",item="Red Clover")
    
    jump forest002

label forest002_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest002
    
label forest002_burdock:
    $ player_bag.add_item("herb026", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Burdock",item="Burdock")
    
    jump forest002
    
label forest002_laurel:
    $ player_bag.add_item("herb010", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Laurel",item="Laurel")
    
    jump forest002

label forest002_hyssop:
    $ player_bag.add_item("herb011", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest002
    
label forest002_calendula:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Calendula",item="Calendula")
    
    jump forest002

label forest002_rosemary:
    $ player_bag.add_item("herb019", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Rosemary",item="Rosemary")
    
    jump forest002
    
label forest002_licorice:
    $ player_bag.add_item("herb030", quality=70, custom_tags=["bitter"])
    $ F2Harvest = True
    show screen inventory_popup2(message="Received Licorice",item="Licorice")
    
    jump forest002
    
label leave_forest002:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Three
#
# Collect herbs. Dense, Dry.


label forest003_layout:
    $ forest003_spawn = renpy.random.randint(1, 5)
    

label forest003:
    init python: 
        message = "message"
    
    $ current_loc = "forest003"
    
    scene bg forest003
    show screen forest003
    show screen basic_overlay
    
#    "Your random number is [forest003_spawn]."

    hide screen forest003
    call check_events
    show screen forest003
    
    jump forest_loop

screen forest003:
    tag menu2
        
    if forest003_spawn == 1:
    
        if herbID2 in shelf.list_books() and forest003_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_chamomile_col", False), Jump("forest003_chamomile") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest003_borage_col:
            imagebutton:
                idle "gui/inv/herb012_idle.png"
                hover "gui/inv/herb012_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_borage_col", False), Jump("forest003_borage") ]
                xpos 1120 ypos 500
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest003_redclover_col:
            imagebutton:
                idle "gui/inv/herb023_idle.png"
                hover "gui/inv/herb023_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_redclover_col", False), Jump("forest003_redclover") ]
                xpos 420 ypos 460
                xanchor 0 yanchor 0
            
            
        if herbID2 in shelf.list_books() and forest003_chamomile2_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_chamomile2_col", False), Jump("forest003_chamomile2") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest003_sage_col:
            imagebutton:
                idle "gui/inv/herb009_idle.png"
                hover "gui/inv/herb009_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_sage_col", False), Jump("forest003_sage") ]
                xpos 800 ypos 600
                xanchor 0 yanchor 0
                
    if forest003_spawn == 2:
        
        if herbID2 in shelf.list_books() and forest003_rosemary_col:
            imagebutton:
                idle "gui/inv/herb019_idle.png"
                hover "gui/inv/herb019_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_rosemary_col", False), Jump("forest003_rosemary") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest003_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_chamomile_col", False), Jump("forest003_chamomile") ]
                xpos 1120 ypos 500
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest003_borage_col:
            imagebutton:
                idle "gui/inv/herb012_idle.png"
                hover "gui/inv/herb012_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_borage_col", False), Jump("forest003_borage") ]
                xpos 420 ypos 460
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest003_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_oak_col", False), Jump("forest003_oak") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest003_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_stjohns_col", False), Jump("forest003_stjohns") ]
                xpos 800 ypos 600
                xanchor 0 yanchor 0
                
    if forest003_spawn == 3:
    
        if herbID1 in shelf.list_books() and forest003_parsley_col:
            imagebutton:
                idle "gui/inv/herb008_idle.png"
                hover "gui/inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_parsley_col", False), Jump("forest003_parsley") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest003_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_chamomile_col", False), Jump("forest003_chamomile") ]
                xpos 1120 ypos 500
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest003_licorice_col:
            imagebutton:
                idle "gui/inv/herb030_idle.png"
                hover "gui/inv/herb030_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_licorice_col", False), Jump("forest003_licorice") ]
                xpos 420 ypos 460
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest003_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_burdock_col", False), Jump("forest003_burdock") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest003_garlic_col:
            imagebutton:
                idle "gui/inv/herb005_idle.png"
                hover "gui/inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_garlic_col", False), Jump("forest003_garlic") ]
                xpos 800 ypos 600
                xanchor 0 yanchor 0
                
    if forest003_spawn == 4:
    
        if herbID1 in shelf.list_books() and forest003_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_oregano_col", False), Jump("forest003_oregano") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest003_mullein_col:
            imagebutton:
                idle "gui/inv/herb022_idle.png"
                hover "gui/inv/herb022_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_mullein_col", False), Jump("forest003_mullein") ]
                xpos 1120 ypos 500
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest003_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_thistle_col", False), Jump("forest003_thistle") ]
                xpos 420 ypos 460
                xanchor 0 yanchor 0
            
            
        if herbID2 in shelf.list_books() and forest003_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_chamomile_col", False), Jump("forest003_chamomile") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest003_calendula_col:
            imagebutton:
                idle "gui/inv/herb017_idle.png"
                hover "gui/inv/herb017_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_calendula_col", False), Jump("forest003_calendula") ]
                xpos 800 ypos 600
                xanchor 0 yanchor 0
    
    if forest003_spawn == 5:
    
        if herbID3 in shelf.list_books() and forest003_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_burdock_col", False), Jump("forest003_burdock") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest003_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_thistle_col", False), Jump("forest003_thistle") ]
                xpos 1120 ypos 500
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest003_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_chamomile_col", False), Jump("forest003_chamomile") ]
                xpos 420 ypos 460
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest003_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_blackberry_col", False), Jump("forest003_blackberry") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest003_sage_col:
            imagebutton:
                idle "gui/inv/herb009_idle.png"
                hover "gui/inv/herb009_hover.png"
                focus_mask True
                clicked [ SetVariable("forest003_sage_col", False), Jump("forest003_sage") ]
                xpos 800 ypos 600
                xanchor 0 yanchor 0
            
    
label forest003_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest003
    
label forest003_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest003
    
label forest003_oak:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Oak",item="Oak")
    
    jump forest003
    
label forest003_garlic:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest003
    
label forest003_oregano:
    $ player_bag.add_item("herb007", quality=70, custom_tags=["bitter"])
    $ pc_inv.take(herb007)
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest003
    
label forest003_parsley:
    $ player_bag.add_item("herb008", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Parsley",item="Parsley")
    
    jump forest003
    
label forest003_chamomile:
    $ player_bag.add_item("herb016", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Chamomile",item="Chamomile")
    
    jump forest003
    
label forest003_chamomile2:
    $ player_bag.add_item("herb016", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Chamomile",item="Chamomile")
    
    jump forest003
    
label forest003_mullein:
    $ player_bag.add_item("herb022", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Mullein",item="Mullein")
    
    jump forest003

label forest003_redclover:
    $ player_bag.add_item("herb023", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Red Clover",item="Red Clover")
    
    jump forest003

label forest003_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest003
    
label forest003_burdock:
    $ player_bag.add_item("herb026", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Burdock",item="Burdock")
    
    jump forest003

label forest003_sage:
    $ player_bag.add_item("herb009", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest003
    
label forest003_borage:
    $ player_bag.add_item("herb012", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest003
    
label forest003_calendula:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Calendula",item="Calendula")
    
    jump forest003

label forest003_rosemary:
    $ player_bag.add_item("herb019", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Rosemary",item="Rosemary")
    
    jump forest003
    
label forest003_licorice:
    $ player_bag.add_item("herb030", quality=70, custom_tags=["bitter"])
    $ F3Harvest = True
    show screen inventory_popup2(message="Received Licorice",item="Licorice")
    
    jump forest003
    
label leave_forest003:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Four
#
# Collect herbs. Open, Sunny.


label forest004_layout:
    $ forest004_spawn = renpy.random.randint(1, 5)
    

label forest004:
    init python: 
        message = "message"
    
    $ current_loc = "forest004"
    
    scene bg forest004
    show screen forest004
    show screen basic_overlay
    
#    "Your random number is [forest004_spawn]."

    hide screen forest004
    call check_events
    show screen forest004

    jump forest_loop

screen forest004:
    tag menu2
    
    if forest004_spawn == 1:
    
        if herbID1 in shelf.list_books() and forest004_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_dandelion_col", False), Jump("forest004_dandelion") ]
                xpos 300 ypos 600
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest004_hyssop_col:
            imagebutton:
                idle "gui/inv/herb011_idle.png"
                hover "gui/inv/herb011_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_hyssop_col", False), Jump("forest004_hyssop") ]
                xpos 1000 ypos 450
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest004_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_stjohns_col", False), Jump("forest004_stjohns") ]
                xpos 20 ypos 480
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest004_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_oak_col", False), Jump("forest004_oak") ]
                xpos 350 ypos 475
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest004_plantain_col:
            imagebutton:
                idle "gui/inv/herb015_idle.png"
                hover "gui/inv/herb015_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_plantain_col", False), Jump("forest004_plantain") ]
                xpos 800 ypos 550
                xanchor 0 yanchor 0
                
    if forest004_spawn == 2:
        
        if herbID1 in shelf.list_books() and forest004_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_mint_col", False), Jump("forest004_mint") ]
                xpos 300 ypos 600
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest004_plantain_col:
            imagebutton:
                idle "gui/inv/herb015_idle.png"
                hover "gui/inv/herb015_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_plantain_col", False), Jump("forest004_plantain") ]
                xpos 1000 ypos 450
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest004_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_burdock_col", False), Jump("forest004_burdock") ]
                xpos 20 ypos 480
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest004_sage_col:
            imagebutton:
                idle "gui/inv/herb009_idle.png"
                hover "gui/inv/herb009_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_sage_col", False), Jump("forest004_sage") ]
                xpos 350 ypos 475
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest004_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_violet_col", False), Jump("forest004_violet") ]
                xpos 800 ypos 550
                xanchor 0 yanchor 0
                
    if forest004_spawn == 3:
    
        if herbID1 in shelf.list_books() and forest004_parsley_col:
            imagebutton:
                idle "gui/inv/herb008_idle.png"
                hover "gui/inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_parsley_col", False), Jump("forest004_parsley") ]
                xpos 300 ypos 600
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest004_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_burdock_col", False), Jump("forest004_burdock") ]
                xpos 1000 ypos 450
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest004_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_chamomile_col", False), Jump("forest004_chamomile") ]
                xpos 20 ypos 480
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest004_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_dandelion_col", False), Jump("forest004_dandelion") ]
                xpos 350 ypos 475
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest004_calendula_col:
            imagebutton:
                idle "gui/inv/herb017_idle.png"
                hover "gui/inv/herb017_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_calendula_col", False), Jump("forest004_calendula") ]
                xpos 800 ypos 550
                xanchor 0 yanchor 0
                
    if forest004_spawn == 4:
    
        if herbID3 in shelf.list_books() and forest004_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_stjohns_col", False), Jump("forest004_stjohns") ]
                xpos 300 ypos 600
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest004_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_blackberry_col", False), Jump("forest004_blackberry") ]
                xpos 1000 ypos 450
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest004_rosemary_col:
            imagebutton:
                idle "gui/inv/herb019_idle.png"
                hover "gui/inv/herb019_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_rosemary_col", False), Jump("forest004_rosemary") ]
                xpos 20 ypos 480
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest004_licorice_col:
            imagebutton:
                idle "gui/inv/herb030_idle.png"
                hover "gui/inv/herb030_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_licorice_col", False), Jump("forest004_licorice") ]
                xpos 350 ypos 475
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest004_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_violet_col", False), Jump("forest004_violet") ]
                xpos 800 ypos 550
                xanchor 0 yanchor 0
    
    if forest004_spawn == 5:
    
        if herbID2 in shelf.list_books() and forest004_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_violet_col", False), Jump("forest004_violet") ]
                xpos 300 ypos 600
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest004_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_oak_col", False), Jump("forest004_oak") ]
                xpos 1000 ypos 450
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest004_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_mint_col", False), Jump("forest004_mint") ]
                xpos 20 ypos 480
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest004_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_oregano_col", False), Jump("forest004_oregano") ]
                xpos 350 ypos 475
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest004_mullein_col:
            imagebutton:
                idle "gui/inv/herb022_idle.png"
                hover "gui/inv/herb022_hover.png"
                focus_mask True
                clicked [ SetVariable("forest004_mullein_col", False), Jump("forest004_mullein") ]
                xpos 800 ypos 550
                xanchor 0 yanchor 0
            
    
label forest004_dandelion:
    $ player_bag.add_item("herb002", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest004
    
label forest004_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest004
    
label forest004_oak:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Oak",item="Oak")
    
    jump forest004
    
label forest004_mint:
    $ player_bag.add_item("herb006", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest004
    
label forest004_oregano:
    $ player_bag.add_item("herb007", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest004
    
label forest004_parsley:
    $ player_bag.add_item("herb008", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Parsley",item="Parsley")
    
    jump forest004
    
label forest004_plantain:
    $ player_bag.add_item("herb015", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Plantain",item="Plantain")
    
    jump forest004

label forest004_chamomile:
    $ player_bag.add_item("herb016", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Chamomile",item="Chamomile")
    
    jump forest004

label forest004_violet:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Violet",item="Violet")
    
    jump forest004
    
label forest004_mullein:
    $ player_bag.add_item("herb022", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Mullein",item="Mullein")
    
    jump forest004
    
label forest004_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest004
    
label forest004_burdock:
    $ player_bag.add_item("herb026", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Burdock",item="Burdock")
    
    jump forest004
    
label forest004_sage:
    $ player_bag.add_item("herb009", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest004
    
label forest004_hyssop:
    $ player_bag.add_item("herb011", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest004
    
label forest004_calendula:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Calendula",item="Calendula")
    
    jump forest004

label forest004_rosemary:
    $ player_bag.add_item("herb019", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Rosemary",item="Rosemary")
    
    jump forest004
    
label forest004_licorice:
    $ player_bag.add_item("herb030", quality=70, custom_tags=["bitter"])
    $ F4Harvest = True
    show screen inventory_popup2(message="Received Licorice",item="Licorice")
    
    jump forest004
    
label leave_forest004:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Five
#
# Collect herbs. Open, Sunny. 


label forest005_layout:
    $ forest005_spawn = renpy.random.randint(1, 5)
    

label forest005:
    init python: 
        message = "message"
    
    $ current_loc = "forest005"
    
    scene bg forest005
    show screen forest005
    show screen basic_overlay
    
#    "Your random number is [forest005_spawn]."

    hide screen forest005
    call check_events
    show screen forest005

    jump forest_loop

screen forest005:
    tag menu2
    
    if forest005_spawn == 1:
    
        if herbID3 in shelf.list_books() and forest005_mullein_col:
            imagebutton:
                idle "gui/inv/herb022_idle.png"
                hover "gui/inv/herb022_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_mullein_col", False), Jump("forest005_mullein") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest005_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_oak_col", False), Jump("forest005_oak") ]
                xpos 1120 ypos 550
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest005_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_stjohns_col", False), Jump("forest005_stjohns") ]
                xpos 150 ypos 370
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest005_lemonbalm_col:
            imagebutton:
                idle "gui/inv/herb029_idle.png"
                hover "gui/inv/herb029_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_lemonbalm_col", False), Jump("forest005_lemonbalm") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest005_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_burdock_col", False), Jump("forest005_burdock") ]
                xpos 935 ypos 370
                xanchor 0 yanchor 0
                
    if forest005_spawn == 2:
        
        if herbID2 in shelf.list_books() and forest005_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_violet_col", False), Jump("forest005_violet") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest005_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_blackberry_col", False), Jump("forest005_blackberry") ]
                xpos 1120 ypos 550
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest005_licorice_col:
            imagebutton:
                idle "gui/inv/herb030_idle.png"
                hover "gui/inv/herb030_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_licorice_col", False), Jump("forest005_licorice") ]
                xpos 150 ypos 370
                xanchor 0 yanchor 0
            
            
        if herbID2 in shelf.list_books() and forest005_plantain_col:
            imagebutton:
                idle "gui/inv/herb015_idle.png"
                hover "gui/inv/herb015_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_plantain_col", False), Jump("forest005_plantain") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest005_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_mint_col", False), Jump("forest005_mint") ]
                xpos 935 ypos 370
                xanchor 0 yanchor 0
                
    if forest005_spawn == 3:
    
        if herbID1 in shelf.list_books() and forest005_laurel_col:
            imagebutton:
                idle "gui/inv/herb010_idle.png"
                hover "gui/inv/herb010_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_laurel_col", False), Jump("forest005_laurel") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest005_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_thistle_col", False), Jump("forest005_thistle") ]
                xpos 1120 ypos 550
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest005_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_dandelion_col", False), Jump("forest005_dandelion") ]
                xpos 150 ypos 370
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest005_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_stjohns_col", False), Jump("forest005_stjohns") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest005_plantain_col:
            imagebutton:
                idle "gui/inv/herb015_idle.png"
                hover "gui/inv/herb015_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_plantain_col", False), Jump("forest005_plantain") ]
                xpos 935 ypos 370
                xanchor 0 yanchor 0
                
    if forest005_spawn == 4:
    
        if herbID1 in shelf.list_books() and forest005_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_thistle_col", False), Jump("forest005_thistle") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest005_rosemary_col:
            imagebutton:
                idle "gui/inv/herb019_idle.png"
                hover "gui/inv/herb019_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_rosemary_col", False), Jump("forest005_rosemary") ]
                xpos 1120 ypos 550
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest005_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_oak_col", False), Jump("forest005_oak") ]
                xpos 150 ypos 370
                xanchor 0 yanchor 0
            
            
        if herbID2 in shelf.list_books() and forest005_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_violet_col", False), Jump("forest005_violet") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest005_chamomile_col:
            imagebutton:
                idle "gui/inv/herb016_idle.png"
                hover "gui/inv/herb016_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_chamomile_col", False), Jump("forest005_chamomile") ]
                xpos 935 ypos 370
                xanchor 0 yanchor 0
    
    if forest005_spawn == 5:
    
        if herbID2 in shelf.list_books() and forest005_crownflower_col:
            imagebutton:
                idle "gui/inv/herb013_idle.png"
                hover "gui/inv/herb013_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_crownflower_col", False), Jump("forest005_crownflower") ]
                xpos 300 ypos 500
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest005_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_burdock_col", False), Jump("forest005_burdock") ]
                xpos 1120 ypos 550
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest005_garlic_col:
            imagebutton:
                idle "gui/inv/herb005_idle.png"
                hover "gui/inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_garlic_col", False), Jump("forest005_garlic") ]
                xpos 150 ypos 370
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest005_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_stjohns_col", False), Jump("forest005_stjohns") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest005_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest005_mint_col", False), Jump("forest005_mint") ]
                xpos 935 ypos 370
                xanchor 0 yanchor 0
            
    
label forest005_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest005

label forest005_dandelion:
    $ player_bag.add_item("herb002", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest005
    
label forest005_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest005
    
label forest005_oak:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Oak",item="Oak")
    
    jump forest005
    
label forest005_garlic:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest005
    
label forest005_mint:
    $ player_bag.add_item("herb006", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest005
    
label forest005_plantain:
    $ player_bag.add_item("herb015", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Plantain",item="Plantain")
    
    jump forest005

label forest005_chamomile:
    $ player_bag.add_item("herb016", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Chamomile",item="Chamomile")
    
    jump forest005

label forest005_violet:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Violet",item="Violet")
    
    jump forest005
    
label forest005_mullein:
    $ player_bag.add_item("herb022", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Mullein",item="Mullein")
    
    jump forest005
    
label forest005_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest005
    
label forest005_burdock:
    $ player_bag.add_item("herb026", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Burdock",item="Burdock")
    
    jump forest005
    
label forest005_laurel:
    $ player_bag.add_item("herb010", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Laurel",item="Laurel")
    
    jump forest005
    
label forest005_calendula:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Calendula",item="Calendula")
    
    jump forest005
    
label forest005_rosemary:
    $ player_bag.add_item("herb019", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Rosemary",item="Rosemary")
    
    jump forest005
    
label forest005_lemonbalm:
    $ player_bag.add_item("herb029", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Lemon Balm",item="Lemon Balm")
    
    jump forest005

label forest005_licorice:
    $ player_bag.add_item("herb030", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Licorice",item="Licorice")
    
    jump forest005

label forest005_crownflower:
    $ player_bag.add_item("herb013", quality=70, custom_tags=["bitter"])
    $ F5Harvest = True
    show screen inventory_popup2(message="Received Crown Flower",item="Crown Flower")
    
    jump forest005
    
label leave_forest005:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Six
#
# Collect herbs. Cool, Sparse.


label forest006_layout:
    $ forest006_spawn = renpy.random.randint(1, 5)
    

label forest006:
    init python: 
        message = "message"
    
    $ current_loc = "forest006"
    
    scene bg forest006
    show screen forest006
    show screen basic_overlay
    
#    "Your random number is [forest006_spawn]."

    hide screen forest006
    call check_events
    show screen forest006

    jump forest_loop

screen forest006:
    tag menu2
    
    if forest006_spawn == 1:
    
        if herbID1 in shelf.list_books() and forest006_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_dandelion_col", False), Jump("forest006_dandelion") ]
                xpos 400 ypos 500
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest006_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_mint_col", False), Jump("forest006_mint") ]
                xpos 1120 ypos 600
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest006_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_burdock_col", False), Jump("forest006_burdock") ]
                xpos 100 ypos 430
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest006_poppy_col:
            imagebutton:
                idle "gui/inv/herb021_idle.png"
                hover "gui/inv/herb021_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_poppy_col", False), Jump("forest006_poppy") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest006_parsley_col:
            imagebutton:
                idle "gui/inv/herb008_idle.png"
                hover "gui/inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_parsley_col", False), Jump("forest006_parsley") ]
                xpos 840 ypos 420
                xanchor 0 yanchor 0
                
    if forest006_spawn == 2:
        
        if herbID3 in shelf.list_books() and forest006_goldenseal_col:
            imagebutton:
                idle "gui/inv/herb028_idle.png"
                hover "gui/inv/herb028_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_goldenseal_col", False), Jump("forest006_goldenseal") ]
                xpos 400 ypos 500
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest006_comfrey_col:
            imagebutton:
                idle "gui/inv/herb027_idle.png"
                hover "gui/inv/herb027_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_comfrey_col", False), Jump("forest006_comfrey") ]
                xpos 1120 ypos 600
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest006_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_oak_col", False), Jump("forest006_oak") ]
                xpos 100 ypos 430
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest006_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_mint_col", False), Jump("forest006_mint") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest006_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_dandelion_col", False), Jump("forest006_dandelion") ]
                xpos 840 ypos 420
                xanchor 0 yanchor 0
                
    if forest006_spawn == 3:
    
        if herbID2 in shelf.list_books() and forest006_crownflower_col:
            imagebutton:
                idle "gui/inv/herb013_idle.png"
                hover "gui/inv/herb013_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_crownflower_col", False), Jump("forest006_crownflower") ]
                xpos 400 ypos 500
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest006_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_oregano_col", False), Jump("forest006_oregano") ]
                xpos 1120 ypos 600
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest006_garlic_col:
            imagebutton:
                idle "gui/inv/herb005_idle.png"
                hover "gui/inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_garlic_col", False), Jump("forest006_garlic") ]
                xpos 100 ypos 430
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest006_redclover_col:
            imagebutton:
                idle "gui/inv/herb023_idle.png"
                hover "gui/inv/herb023_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_redclover_col", False), Jump("forest006_redclover") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest006_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_burdock_col", False), Jump("forest006_burdock") ]
                xpos 840 ypos 420
                xanchor 0 yanchor 0
                
    if forest006_spawn == 4:
    
        if herbID3 in shelf.list_books() and forest006_redclover_col:
            imagebutton:
                idle "gui/inv/herb023_idle.png"
                hover "gui/inv/herb023_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_redclover_col", False), Jump("forest006_redclover") ]
                xpos 400 ypos 500
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest006_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_thistle_col", False), Jump("forest006_thistle") ]
                xpos 1120 ypos 600
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest006_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_dandelion_col", False), Jump("forest006_dandelion") ]
                xpos 100 ypos 430
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest006_burdock_col:
            imagebutton:
                idle "gui/inv/herb026_idle.png"
                hover "gui/inv/herb026_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_burdock_col", False), Jump("forest006_burdock") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest006_garlic_col:
            imagebutton:
                idle "gui/inv/herb005_idle.png"
                hover "gui/inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_garlic_col", False), Jump("forest006_garlic") ]
                xpos 840 ypos 420
                xanchor 0 yanchor 0
    
    if forest006_spawn == 5:
    
        if herbID3 in shelf.list_books() and forest006_goldenseal_col:
            imagebutton:
                idle "gui/inv/herb028_idle.png"
                hover "gui/inv/herb028_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_goldenseal_col", False), Jump("forest006_goldenseal") ]
                xpos 400 ypos 500
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest006_calendula_col:
            imagebutton:
                idle "gui/inv/herb017_idle.png"
                hover "gui/inv/herb017_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_calendula_col", False), Jump("forest006_calendula") ]
                xpos 1120 ypos 600
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest006_rosemary_col:
            imagebutton:
                idle "gui/inv/herb019_idle.png"
                hover "gui/inv/herb019_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_rosemary_col", False), Jump("forest006_rosemary") ]
                xpos 100 ypos 430
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest006_parsley_col:
            imagebutton:
                idle "gui/inv/herb008_idle.png"
                hover "gui/inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_parsley_col", False), Jump("forest006_parsley") ]
                xpos 600 ypos 440
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest006_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest006_oregano_col", False), Jump("forest006_oregano") ]
                xpos 840 ypos 420
                xanchor 0 yanchor 0
            
    
label forest006_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest006

label forest006_dandelion:
    $ player_bag.add_item("herb002", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest006
    
label forest006_oak:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Oak",item="Oak")
    
    jump forest006
    
label forest006_garlic:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest006
    
label forest006_mint:
    $ player_bag.add_item("herb006", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest006
    
label forest006_oregano:
    $ player_bag.add_item("herb007", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest006
    
label forest006_parsley:
    $ player_bag.add_item("herb008", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Parsley",item="Parsley")
    
    jump forest006
    
label forest006_redclover:
    $ player_bag.add_item("herb023", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Red Clover",item="Red Clover")
    
    jump forest006
    
label forest006_burdock:
    $ player_bag.add_item("herb026", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Burdock",item="Burdock")
    
    jump forest006
    
label forest006_calendula:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Calendula",item="Calendula")
    
    jump forest006

label forest006_rosemary:
    $ player_bag.add_item("herb019", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Rosemary",item="Rosemary")
    
    jump forest006

label forest006_comfrey:
    $ player_bag.add_item("herb027", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Comfrey",item="Comfrey")
    
    jump forest006
    
label forest006_crownflower:
    $ player_bag.add_item("herb013", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Crown Flower",item="Crown Flower")
    
    jump forest006
    
label forest006_poppy:
    $ player_bag.add_item("herb021", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Poppy",item="Poppy")
    
    jump forest006

label forest006_goldenseal:
    $ player_bag.add_item("herb028", quality=70, custom_tags=["bitter"])
    $ F6Harvest = True
    show screen inventory_popup2(message="Received Goldenseal",item="Goldenseal")
    
    jump forest006
    
label leave_forest006:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Seven
#
# Collect herbs. Marsh. Humid, Cool. 


label forest007_layout:
    $ forest007_spawn = renpy.random.randint(1, 5)
    

label forest007:
    init python: 
        message = "message"
    
    $ current_loc = "forest007"
    
    scene bg forest007
    show screen forest007
    show screen basic_overlay
    
#    "Your random number is [forest007_spawn]."

    hide screen forest007
    call check_events
    show screen forest007

    jump forest_loop

screen forest007:
    tag menu2
    
    if forest007_spawn == 1:
    
        if herbID1 in shelf.list_books() and forest007_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_oregano_col", False), Jump("forest007_oregano") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest007_comfrey_col:
            imagebutton:
                idle "gui/inv/herb027_idle.png"
                hover "gui/inv/herb027_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_comfrey_col", False), Jump("forest007_comfrey") ]
                xpos 1180 ypos 420
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest007_yellowdock_col:
            imagebutton:
                idle "gui/inv/herb025_idle.png"
                hover "gui/inv/herb025_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_yellowdock_col", False), Jump("forest007_yellowdock") ]
                xpos 140 ypos 385
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest007_mint_col:
            imagebutton:
                idle "gui/inv/herb006_idle.png"
                hover "gui/inv/herb006_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_mint_col", False), Jump("forest007_mint") ]
                xpos 500 ypos 390
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest007_marshmarigold_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_marshmarigold_col", False), Jump("forest007_marshmarigold") ]
                xpos 800 ypos 480
                xanchor 0 yanchor 0
                
    if forest007_spawn == 2:
        
        if herbID1 in shelf.list_books() and forest007_parsley_col:
            imagebutton:
                idle "gui/inv/herb008_idle.png"
                hover "gui/inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_parsley_col", False), Jump("forest007_parsley") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest007_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_basil_col", False), Jump("forest007_basil") ]
                xpos 1180 ypos 420
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest007_comfrey_col:
            imagebutton:
                idle "gui/inv/herb027_idle.png"
                hover "gui/inv/herb027_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_comfrey_col", False), Jump("forest007_comfrey") ]
                xpos 140 ypos 385
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest007_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_thistle_col", False), Jump("forest007_thistle") ]
                xpos 500 ypos 390
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest007_lemonbalm_col:
            imagebutton:
                idle "gui/inv/herb029_idle.png"
                hover "gui/inv/herb029_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_lemonbalm_col", False), Jump("forest007_lemonbalm") ]
                xpos 800 ypos 480
                xanchor 0 yanchor 0
                
    if forest007_spawn == 3:
    
        if herbID3 in shelf.list_books() and forest007_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_stjohns_col", False), Jump("forest007_stjohns") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest007_marshmarigold_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_marshmarigold_col", False), Jump("forest007_marshmarigold") ]
                xpos 1180 ypos 420
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest007_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_basil_col", False), Jump("forest007_basil") ]
                xpos 140 ypos 385
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest007_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_dandelion_col", False), Jump("forest007_dandelion") ]
                xpos 500 ypos 390
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest007_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_thistle_col", False), Jump("forest007_thistle") ]
                xpos 800 ypos 480
                xanchor 0 yanchor 0
                
    if forest007_spawn == 4:
    
        if herbID2 in shelf.list_books() and forest007_marshmarigold_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_marshmarigold_col", False), Jump("forest007_marshmarigold") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest007_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_basil_col", False), Jump("forest007_basil") ]
                xpos 1180 ypos 420
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest007_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_basil_col", False), Jump("forest007_basil") ]
                xpos 140 ypos 385
                xanchor 0 yanchor 0
            
            
        if herbID2 in shelf.list_books() and forest007_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_violet_col", False), Jump("forest007_violet") ]
                xpos 500 ypos 390
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest007_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_blackberry_col", False), Jump("forest007_blackberry") ]
                xpos 800 ypos 480
                xanchor 0 yanchor 0
    
    if forest007_spawn == 5:
    
        if herbID1 in shelf.list_books() and forest007_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_blackberry_col", False), Jump("forest007_blackberry") ]
                xpos 300 ypos 560
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest007_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_stjohns_col", False), Jump("forest007_stjohns") ]
                xpos 1180 ypos 420
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest007_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_violet_col", False), Jump("forest007_violet") ]
                xpos 140 ypos 385
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest007_goldenseal_col:
            imagebutton:
                idle "gui/inv/herb028_idle.png"
                hover "gui/inv/herb028_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_goldenseal_col", False), Jump("forest007_goldenseal") ]
                xpos 500 ypos 390
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest007_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest007_dandelion_col", False), Jump("forest007_dandelion") ]
                xpos 800 ypos 480
                xanchor 0 yanchor 0
            
    
label forest007_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest007

label forest007_dandelion:
    $ player_bag.add_item("herb002", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest007
    
label forest007_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest007
    
label forest007_mint:
    $ player_bag.add_item("herb006", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Mint",item="Mint")
    
    jump forest007
    
label forest007_oregano:
    $ player_bag.add_item("herb007", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest007
    
label forest007_parsley:
    $ player_bag.add_item("herb008", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Parsley",item="Parsley")
    
    jump forest007
    
label forest007_violet:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Violet",item="Violet")
    
    jump forest007

label forest007_basil:
    $ player_bag.add_item("herb020", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Basil",item="Basil")
    
    jump forest007
    
label forest007_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest007

label forest007_yellowdock:
    $ player_bag.add_item("herb025", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Yellow Dock",item="Yellow Dock")
    
    jump forest007
    
label forest007_comfrey:
    $ player_bag.add_item("herb027", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Comfrey",item="Comfrey")
    
    jump forest007

label forest007_lemonbalm:
    $ player_bag.add_item("herb029", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Lemon Balm",item="Lemon Balm")
    
    jump forest007
    
label forest007_marshmarigold:
    $ player_bag.add_item("herb014", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Marsh Marigold",item="Marsh Marigold")
    
    jump forest007
    
label forest007_goldenseal:
    $ player_bag.add_item("herb028", quality=70, custom_tags=["bitter"])
    $ F7Harvest = True
    show screen inventory_popup2(message="Received Goldenseal",item="Goldenseal")
    
    jump forest007
    
label leave_forest007:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Eight
#
# Collect herbs. Humid, Sunny.


label forest008_layout:
    $ forest008_spawn = renpy.random.randint(1, 5)
    

label forest008:
    init python: 
        message = "message"
    
    $ current_loc = "forest008"
    
    scene bg forest008
    show screen forest008
    show screen basic_overlay
    
#    "Your random number is [forest008_spawn]."

    hide screen forest008
    call check_events
    show screen forest008

    jump forest_loop

screen forest008:
    tag menu2
    
    if forest008_spawn == 1:
    
        if herbID2 in shelf.list_books() and forest008_borage_col:
            imagebutton:
                idle "gui/inv/herb012_idle.png"
                hover "gui/inv/herb012_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_borage_col", False), Jump("forest008_borage") ]
                xpos 300 ypos 400
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest008_lemonbalm_col:
            imagebutton:
                idle "gui/inv/herb029_idle.png"
                hover "gui/inv/herb029_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_lemonbalm_col", False), Jump("forest008_lemonbalm") ]
                xpos 1080 ypos 450
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest008_yellowdock_col:
            imagebutton:
                idle "gui/inv/herb025_idle.png"
                hover "gui/inv/herb025_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_yellowdock_col", False), Jump("forest008_yellowdock") ]
                xpos 20 ypos 330
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest008_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_oak_col", False), Jump("forest008_oak") ]
                xpos 620 ypos 360
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest008_parsley_col:
            imagebutton:
                idle "gui/inv/herb008_idle.png"
                hover "gui/inv/herb008_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_parsley_col", False), Jump("forest008_parsley") ]
                xpos 850 ypos 280
                xanchor 0 yanchor 0
                
    if forest008_spawn == 2:
        
        if herbID3 in shelf.list_books() and forest008_yellowdock_col:
            imagebutton:
                idle "gui/inv/herb025_idle.png"
                hover "gui/inv/herb025_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_yellowdock_col", False), Jump("forest008_yellowdock") ]
                xpos 300 ypos 400
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest008_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_blackberry_col", False), Jump("forest008_blackberry") ]
                xpos 1080 ypos 450
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest008_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_stjohns_col", False), Jump("forest008_stjohns") ]
                xpos 20 ypos 330
                xanchor 0 yanchor 0
            
            
        if herbID2 in shelf.list_books() and forest008_marshmarigold_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_marshmarigold_col", False), Jump("forest008_marshmarigold") ]
                xpos 620 ypos 360
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest008_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_basil_col", False), Jump("forest008_basil") ]
                xpos 850 ypos 280
                xanchor 0 yanchor 0
                
    if forest008_spawn == 3:
    
        if herbID3 in shelf.list_books() and forest008_lemonbalm_col:
            imagebutton:
                idle "gui/inv/herb029_idle.png"
                hover "gui/inv/herb029_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_lemonbalm_col", False), Jump("forest008_lemonbalm") ]
                xpos 300 ypos 400
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest008_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_basil_col", False), Jump("forest008_basil") ]
                xpos 1080 ypos 450
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest008_oak_col:
            imagebutton:
                idle "gui/inv/herb004_idle.png"
                hover "gui/inv/herb004_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_oak_col", False), Jump("forest008_oak") ]
                xpos 20 ypos 330
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest008_borage_col:
            imagebutton:
                idle "gui/inv/herb012_idle.png"
                hover "gui/inv/herb012_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_borage_col", False), Jump("forest008_borage") ]
                xpos 620 ypos 360
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest008_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_blackberry_col", False), Jump("forest008_blackberry") ]
                xpos 850 ypos 280
                xanchor 0 yanchor 0
                
    if forest008_spawn == 4:
    
        if herbID1 in shelf.list_books() and forest008_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_dandelion_col", False), Jump("forest008_dandelion") ]
                xpos 300 ypos 400
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest008_oregano_col:
            imagebutton:
                idle "gui/inv/herb007_idle.png"
                hover "gui/inv/herb007_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_oregano_col", False), Jump("forest008_oregano") ]
                xpos 1080 ypos 450
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest008_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_thistle_col", False), Jump("forest008_thistle") ]
                xpos 20 ypos 330
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest008_yellowdock_col:
            imagebutton:
                idle "gui/inv/herb025_idle.png"
                hover "gui/inv/herb025_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_yellowdock_col", False), Jump("forest008_yellowdock") ]
                xpos 620 ypos 360
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest008_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_stjohns_col", False), Jump("forest008_stjohns") ]
                xpos 850 ypos 280
                xanchor 0 yanchor 0
    
    if forest008_spawn == 5:
    
        if herbID2 in shelf.list_books() and forest008_plantain_col:
            imagebutton:
                idle "gui/inv/herb015_idle.png"
                hover "gui/inv/herb015_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_plantain_col", False), Jump("forest008_plantain") ]
                xpos 300 ypos 400
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest008_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_blackberry_col", False), Jump("forest008_blackberry") ]
                xpos 1080 ypos 450
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest008_plantain2_col:
            imagebutton:
                idle "gui/inv/herb015_idle.png"
                hover "gui/inv/herb015_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_plantain2_col", False), Jump("forest008_plantain2") ]
                xpos 20 ypos 330
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest008_thistle_col:
            imagebutton:
                idle "gui/inv/herb001_idle.png"
                hover "gui/inv/herb001_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_thistle_col", False), Jump("forest008_thistle") ]
                xpos 620 ypos 360
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest008_garlic_col:
            imagebutton:
                idle "gui/inv/herb005_idle.png"
                hover "gui/inv/herb005_hover.png"
                focus_mask True
                clicked [ SetVariable("forest008_garlic_col", False), Jump("forest008_garlic") ]
                xpos 850 ypos 280
                xanchor 0 yanchor 0
            
    
label forest008_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest008

label forest008_dandelion:
    $ player_bag.add_item("herb002", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest008
    
label forest008_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest008
    
label forest008_oak:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Oak",item="Oak")
    
    jump forest008
    
label forest008_garlic:
    $ player_bag.add_item("herb005", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Garlic",item="Garlic")
    
    jump forest008
    
label forest008_oregano:
    $ player_bag.add_item("herb007", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Oregano",item="Oregano")
    
    jump forest008
    
label forest008_parsley:
    $ player_bag.add_item("herb008", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Parsley",item="Parsley")
    
    jump forest008
    
label forest008_plantain:
    $ player_bag.add_item("herb015", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Plantain",item="Plantain")
    
    jump forest008
    
label forest008_plantain2:
    $ player_bag.add_item("herb015", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Plantain",item="Plantain")
    
    jump forest008
    
label forest008_violet:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Violet",item="Violet")
    
    jump forest008

label forest008_basil:
    $ player_bag.add_item("herb020", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Basil",item="Basil")
    
    jump forest008
    
label forest008_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest008

label forest008_yellowdock:
    $ player_bag.add_item("herb025", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Yellow Dock",item="Yellow Dock")
    
    jump forest008
    
label forest008_borage:
    $ player_bag.add_item("herb012", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Borage",item="Borage")
    
    jump forest008
    
label forest008_lemonbalm:
    $ player_bag.add_item("herb029", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Lemon Balm",item="Lemon Balm")
    
    jump forest008
    
label forest008_marshmarigold:
    $ player_bag.add_item("herb014", quality=70, custom_tags=["bitter"])
    $ F8Harvest = True
    show screen inventory_popup2(message="Received Marsh Marigold",item="Marsh Marigold")
    
    jump forest008
    
label leave_forest008:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02
    
    
##############################################################################
# Forest Nine
#
# Collect herbs. Humid, Warm,


label forest009_layout:
    $ forest009_spawn = renpy.random.randint(1, 5)
    

label forest009:
    init python: 
        message = "message"
    
    $ current_loc = "forest009"

    scene bg forest009
    show screen forest009
    show screen basic_overlay
    
#    "Your random number is [forest009_spawn]."

    hide screen forest009
    call check_events
    show screen forest009

    jump forest_loop

screen forest009:
    tag menu2
    
    if forest009_spawn == 1:
    
        if herbID1 in shelf.list_books() and forest009_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_blackberry_col", False), Jump("forest009_blackberry") ]
                xpos 300 ypos 380
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest009_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_dandelion_col", False), Jump("forest009_dandelion") ]
                xpos 1080 ypos 550
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest009_marshmarigold_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_marshmarigold_col", False), Jump("forest009_marshmarigold") ]
                xpos 190 ypos 210
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest009_sage_col:
            imagebutton:
                idle "gui/inv/herb009_idle.png"
                hover "gui/inv/herb009_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_sage_col", False), Jump("forest009_sage") ]
                xpos 600 ypos 240
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest009_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_basil_col", False), Jump("forest009_basil") ]
                xpos 830 ypos 140
                xanchor 0 yanchor 0
                
    if forest009_spawn == 2:
        
        if herbID3 in shelf.list_books() and forest009_yellowdock_col:
            imagebutton:
                idle "gui/inv/herb025_idle.png"
                hover "gui/inv/herb025_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_yellowdock_col", False), Jump("forest009_yellowdock") ]
                xpos 300 ypos 380
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest009_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_blackberry_col", False), Jump("forest009_blackberry") ]
                xpos 1080 ypos 550
                xanchor 0 yanchor 0
    
        if herbID2 in shelf.list_books() and forest009_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_violet_col", False), Jump("forest009_violet") ]
                xpos 190 ypos 210
                xanchor 0 yanchor 0
            
            
        if herbID3 in shelf.list_books() and forest009_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_stjohns_col", False), Jump("forest009_stjohns") ]
                xpos 600 ypos 240
                xanchor 0 yanchor 0
            
        if herbID1 in shelf.list_books() and forest009_laurel_col:
            imagebutton:
                idle "gui/inv/herb010_idle.png"
                hover "gui/inv/herb010_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_laurel_col", False), Jump("forest009_laurel") ]
                xpos 830 ypos 140
                xanchor 0 yanchor 0
                
    if forest009_spawn == 3:
    
        if herbID3 in shelf.list_books() and forest009_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_stjohns_col", False), Jump("forest009_stjohns") ]
                xpos 300 ypos 380
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest009_goldenseal_col:
            imagebutton:
                idle "gui/inv/herb028_idle.png"
                hover "gui/inv/herb028_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_goldenseal_col", False), Jump("forest009_goldenseal") ]
                xpos 1080 ypos 550
                xanchor 0 yanchor 0
    
        if herbID1 in shelf.list_books() and forest009_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_blackberry_col", False), Jump("forest009_blackberry") ]
                xpos 190 ypos 210
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest009_violet_col:
            imagebutton:
                idle "gui/inv/herb018_idle.png"
                hover "gui/inv/herb018_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_violet_col", False), Jump("forest009_violet") ]
                xpos 600 ypos 240
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest009_hyssop_col:
            imagebutton:
                idle "gui/inv/herb011_idle.png"
                hover "gui/inv/herb011_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_hyssop_col", False), Jump("forest009_hyssop") ]
                xpos 830 ypos 140
                xanchor 0 yanchor 0
                
    if forest009_spawn == 4:
    
        if herbID2 in shelf.list_books() and forest009_marshmarigold_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_marshmarigold_col", False), Jump("forest009_marshmarigold") ]
                xpos 300 ypos 380
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest009_marshmarigold2_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_marshmarigold2_col", False), Jump("forest009_marshmarigold2") ]
                xpos 1080 ypos 550
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest009_stjohns_col:
            imagebutton:
                idle "gui/inv/herb024_idle.png"
                hover "gui/inv/herb024_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_stjohns_col", False), Jump("forest009_stjohns") ]
                xpos 190 ypos 210
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest009_dandelion_col:
            imagebutton:
                idle "gui/inv/herb002_idle.png"
                hover "gui/inv/herb002_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_dandelion_col", False), Jump("forest009_dandelion") ]
                xpos 600 ypos 240
                xanchor 0 yanchor 0
            
        if herbID3 in shelf.list_books() and forest009_lemonbalm_col:
            imagebutton:
                idle "gui/inv/herb029_idle.png"
                hover "gui/inv/herb029_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_lemonbalm_col", False), Jump("forest009_lemonbalm") ]
                xpos 830 ypos 140
                xanchor 0 yanchor 0
    
    if forest009_spawn == 5:
    
        if herbID3 in shelf.list_books() and forest009_yellowdock_col:
            imagebutton:
                idle "gui/inv/herb025_idle.png"
                hover "gui/inv/herb025_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_yellowdock_col", False), Jump("forest009_yellowdock") ]
                xpos 300 ypos 380
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest009_basil_col:
            imagebutton:
                idle "gui/inv/herb020_idle.png"
                hover "gui/inv/herb020_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_basil_col", False), Jump("forest009_basil") ]
                xpos 1080 ypos 550
                xanchor 0 yanchor 0
    
        if herbID3 in shelf.list_books() and forest009_comfrey_col:
            imagebutton:
                idle "gui/inv/herb027_idle.png"
                hover "gui/inv/herb027_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_comfrey_col", False), Jump("forest009_comfrey") ]
                xpos 190 ypos 210
                xanchor 0 yanchor 0
            
            
        if herbID1 in shelf.list_books() and forest009_blackberry_col:
            imagebutton:
                idle "gui/inv/herb003_idle.png"
                hover "gui/inv/herb003_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_blackberry_col", False), Jump("forest009_blackberry") ]
                xpos 600 ypos 240
                xanchor 0 yanchor 0
            
        if herbID2 in shelf.list_books() and forest009_marshmarigold_col:
            imagebutton:
                idle "gui/inv/herb014_idle.png"
                hover "gui/inv/herb014_hover.png"
                focus_mask True
                clicked [ SetVariable("forest009_marshmarigold_col", False), Jump("forest009_marshmarigold") ]
                xpos 830 ypos 140
                xanchor 0 yanchor 0
            
    
label forest009_thistle:
    $ player_bag.add_item("herb001", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Thistle",item="Thistle")
    
    jump forest009

label forest009_dandelion:
    $ player_bag.add_item("herb002", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Dandelion",item="Dandelion")
    
    jump forest009
    
label forest009_blackberry:
    $ player_bag.add_item("herb003", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Blackberry",item="Blackberry")
    
    jump forest009
    
label forest009_violet:
    $ player_bag.add_item("herb017", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Violet",item="Violet")
    
    jump forest009

label forest009_basil:
    $ player_bag.add_item("herb020", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Basil",item="Basil")
    
    jump forest009
    
label forest009_stjohns:
    $ player_bag.add_item("herb024", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received St. John's Wort",item="St. John's Wort")
    
    jump forest009

label forest009_yellowdock:
    $ player_bag.add_item("herb025", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Yellow Dock",item="Yellow Dock")
    
    jump forest009
    
label forest009_sage:
    $ player_bag.add_item("herb009", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Sage",item="Sage")
    
    jump forest009

label forest009_laurel:
    $ player_bag.add_item("herb010", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Laurel",item="Laurel")
    
    jump forest009

label forest009_hyssop:
    $ player_bag.add_item("herb011", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Hyssop",item="Hyssop")
    
    jump forest009
    
label forest009_comfrey:
    $ player_bag.add_item("herb027", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Comfrey",item="Comfrey")
    
    jump forest009

label forest009_lemonbalm:
    $ player_bag.add_item("herb029", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Lemon Balm",item="Lemon Balm")
    
    jump forest009
    
label forest009_marshmarigold:
    $ player_bag.add_item("herb014", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Marsh Marigold",item="Marsh Marigold")
    
    jump forest009
    
label forest009_marshmarigold2:
    $ player_bag.add_item("herb014", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Marsh Marigold",item="Marsh Marigold")
    
    jump forest009
    
label forest009_goldenseal:
    $ player_bag.add_item("herb028", quality=70, custom_tags=["bitter"])
    $ F9Harvest = True
    show screen inventory_popup2(message="Received Goldenseal",item="Goldenseal")
    
    jump forest009
    
label leave_forest009:
    show screen basic_overlay
    show screen overworld02
    $ current_loc = "none"
    $ time_cnt += 1
    
    jump overworld02    
   