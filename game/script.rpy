﻿## inventory 1.5 demo

init python hide:
    for file in renpy.list_files():
        if file.startswith('bg/') and file.endswith('.png'):
            name = file.replace('/', ' ').replace('.png','')
            renpy.image(name, Image(file))
            
init python hide:
    for file in renpy.list_files():
        if file.startswith('spr/') and file.endswith('.png'):
            name = file.replace('spr/', '').replace('.png','')
            renpy.image(name, Image(file))
            
init python hide:
    for file in renpy.list_files():
        if file.startswith('cg/') and file.endswith('.png'):
            name = file.replace('cg/', '').replace('.png','')
            renpy.image(name, Image(file))
            
            
# This is the splash screen. Should show my logo, and then the 
# instructions for playing on the Ouya.
label splashscreen:
    show bg black
    $ renpy.pause(0)
    show bg logo
    with dissolve
    with Pause (1.5)
    
    show bg main_menu
    with fade
    with Pause(1.5)
    
    return 
    
      
label start:  
    
    "Game start" 
        
    ## ------------ ESC MENU AND TIME TRACKING --------------------
    
    $ _game_menu_screen = "game_menu" # This code activates the "pause menu" in screens.rpy
    $ calendar = Calendar(6, 1, 2017, 2020) # Calendar(day, month, year, first leap year (can be ignored))
    $ time_cnt = 1
    $ day_cnt = 1
    init python:
        timeofday = "sunrise"
    
    ## If using the crafting feature, add an empty cookbook list after start to keep track of recipes
    $ cookbook = list() 
        
    call items
    jump skip_demo

    #menu:
    #    "Feature demo":
    #        pass
    #    "Skip demo":
    #        jump skip_demo
    
label demo:    
    # Display an inventory by using the inventory object name as the parameter  
    "For this demo the inventory_screen modal has been set to False (line 150 of inventory.rpy)."
    show screen inventory_screen(first_inventory=pc_inv)         
    
    "Let's add some items to Jane's inventory. The format is item, quantity."
    $ pc_inv.take(coin,4)
    $ pc_inv.take(sword)
    $ pc_inv.take(eye)
    $ pc_inv.take(but,2)
    $ pc_inv.take(fabric,3)
    $ pc_inv.take(yarn,2)        
      
    "You can hover over the items to see a description. If you click on the sword you will perform the action associated with that item (show a screen with a message).  You can sort inventory several ways and can switch between a grid and list view. If you're using text items you'll only want to enable the list view."  
    
    "Now, let's remove a coin."
    $ pc_inv.drop(coin)   
    
    "We can also check to see if Jane has a certain item.  The check function returns the quantity, if any."    
    if pc_inv.qty(coin): 
        $ qty = pc_inv.qty(coin)
        "Jane still has [qty] coins. Good job, Jane."
    else:
        "Jane doesn't have any coins. You must have changed this script!"   

    if pc_inv.qty(but):
        $ qty = pc_inv.qty(but)
        "Jane has [qty] buttons."
    else:
        "Jane doesn't have any buttons."
        
    "You can also change an item and modify the name, description, and icon if you need to."
    $ sword.change("Broken sword", "This sword is old and busted.", "inv/broke_sword.png", 50, act=Show("inventory_popup", message="It's broken, be careful!"))
    
    "Now the sword is broken and you can't even wave it around anymore.  Let's sell it and buy something else."
    
    "We'll create a vendor named Mindy and give her money and inventory.  Mindy really likes eyes and buttons. Her barter percentage is 75, so she will only buy items from Jane at 75 percent of their value."
    $ mindy_inv = Inventory("Mindy", 500, 75)
    $ mindy_inv.take(eye,4)
    $ mindy_inv.take(but,3)
    $ mindy_inv.take(coin,2)    
    
    # vendor screen parameters are left-side inventory, right-side inventory
    show screen inventory_screen(first_inventory=pc_inv, second_inventory=mindy_inv)
    
    "Now we'll give Jane some walking-around money."
    $ pc_inv.money = 500    
    
    "The inventory screen can take two inventory parameters and display the inventories side-by-side. You can click an item to buy/sell between the two.  Neither character can buy items if they don't have enough money.  Trade mode allows you to exchange items without money and bank mode allows withdrawing and depositing money."    
    
    $ chest = Inventory("Storage Chest")

    "Using trade and bank modes together, you can create a storage chest."
    show screen inventory_screen(first_inventory=pc_inv, second_inventory=chest, trade_mode=True, bank_mode=True)    
    
    "That's it! Exit to end the demo when you are finished."    
    
    show screen overlay
    
label looping:
    $ renpy.pause()
    jump looping
    
label skip_demo:    
    $ pc_inv.take(herb001,4)
    $ pc_inv.take(herb002)
    $ pc_inv.take(herb003)
    $ pc_inv.take(herb004,2)
    $ pc_inv.take(herb005,3)
    $ pc_inv.take(herb006,2)   
    
    $ pc_inv.money = 500  
    $ mindy_inv = Inventory("Mindy", 500, 75)
    $ mindy_inv.take(herb007,4)
    $ mindy_inv.take(herb008,3)
    $ mindy_inv.take(herb009,2)
    $ mindy_inv.take(herb010)
    
    $ chest = Inventory("Storage Chest")   
    
    "All inventory items have been generated."

    show screen overlay    
    "The overlay screen should be visible now."
    
    show screen calendar
    "The calendar should be visible now."
    
    show bg apothecary
    "Now there is a background image."
    
    "You are in your apothecary shop."
    
label action_test:
    
    "Would you like to exit the shop?"
    menu:
        "Yes.":
            "It is Day [day_cnt]. The time period is [time_cnt]. Leaving the shop will take one time period."
            "You decide to leave the shop. It is several hours before you return home."
            $ time_cnt += 1
            if time_cnt > 5:
                $ time_cnt = 1
                $ day_cnt += 1
                $ calendar.next()
                
            if time_cnt == 1:
                $ timeofday = "sunrise"
                "It is now sunrise."
            elif time_cnt == 2:
                $ timeofday = "morning"
                "It is now morning."
            elif time_cnt == 3:
                $ timeofday = "noon"
                "It is now noon."
            elif time_cnt == 4:
                $ timeofday = "sunset"
                "It is now sunset."
            else:
                $ timeofday = "night"
                "It is now night."
                
            "Time has passed. It is Day [day_cnt]. The time period is [time_cnt]."
            
            jump action_test
        "No.":
            "So you're just going to sit there like a lump? Try again."
            jump action_test
    
   
    jump looping 
    
screen overlay:
    frame:
        yalign 0.0 xalign 1.0
        hbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=pc_inv)
            textbutton "Vendor" action Show("inventory_screen", first_inventory=pc_inv, second_inventory=mindy_inv)
            textbutton "Craft" action Show("inventory_screen", first_inventory=pc_inv)
            textbutton "Storage" action Show("inventory_screen", first_inventory=pc_inv, second_inventory=chest, trade_mode=True, bank_mode=True) 
            textbutton "Exit" action Quit(confirm=False)