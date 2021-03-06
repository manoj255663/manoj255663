#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Jan 23, 2020 06:37:02 PM IST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}



    menu .pop46 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(pr,menubgcolor) \
        -font $vTcl(actual_gui_font_menu_desc) -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop46" "Popupmenu1" vTcl:WidgetProc "" 1
    menu .pop47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(pr,menubgcolor) \
        -font $vTcl(actual_gui_font_menu_desc) -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop47" "Popupmenu2" vTcl:WidgetProc "" 1

proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+417+47
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm iconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    canvas $top.can50 \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -closeenough 1.0 \
        -height 353 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 463 
    vTcl:DefineAlias "$top.can50" "Canvas1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.can50
    message $site_3_0.mes51 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {To Start Your Jarvis Program Click 
on start Button and say password} \
        -width 230 
    vTcl:DefineAlias "$site_3_0.mes51" "Message1" vTcl:WidgetProc "Toplevel1" 1
    frame $site_3_0.fra52 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 205 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 445 
    vTcl:DefineAlias "$site_3_0.fra52" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.fra52
    button $site_4_0.but53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Start Jarvis} 
    vTcl:DefineAlias "$site_4_0.but53" "Button1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent54 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black 
    vTcl:DefineAlias "$site_4_0.ent54" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but53 \
        -in $site_4_0 -x 150 -y 30 -width 147 -relwidth 0 -height 94 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.ent54 \
        -in $site_4_0 -x 130 -y 130 -width 184 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes51 \
        -in $site_3_0 -x 120 -y 40 -width 230 -relwidth 0 -height 73 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.fra52 \
        -in $site_3_0 -x 10 -y 140 -width 445 -relwidth 0 -height 205 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can50 \
        -in $top -x 70 -y 40 -width 463 -relwidth 0 -height 353 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

