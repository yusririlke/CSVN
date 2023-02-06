screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "stats_idle.png"
        hover "stats_hover.png"
        action ShowMenu("StatsUI")
screen StatsUI:
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Knowledge" size 40
                text "Stress" size 40
                text "Money" size 40

            vbox:
                spacing 10
                text "[knowledge]" size 40
                text "[stress]" size 40
                text "[money]" size 40

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "stats_bg.png"
        hover "stats_bg.png"
        action Return()
