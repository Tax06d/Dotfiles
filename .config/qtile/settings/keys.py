from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "h", lazy.layout.grow()),
    ([mod, "shift"], "l", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "z", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    #([mod], "d", lazy.spawn("rofi -show drun")),

    # Window Nav
    #([mod, "shift"], "d", lazy.spawn("dmenu_run")),

    # Browser
    #([mod], "w", lazy.spawn("google-chrome-stable")),

    # File Explorer
    #([mod], "f", lazy.spawn("pcmanfm")),

    # Terminal
    #([mod], "Return", lazy.spawn("alacritty")),
    #([mod, "shift"], "Return", lazy.spawn("tilix")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 3500")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------
    
    # code
    #([mod], "s", lazy.spawn("code")),

    # wallpaper
    #([mod], "m", lazy.spawn("nitrogen")),

    # volume F
    ([mod], "F8", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%")), 
    ([mod], "F9", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%")), 
    ([mod], "F10", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # multimedia
    #([mod], "F5", lazy.spawn("playerctl stop")),
    #([mod], "F6", lazy.spawn("playerctl previous")),
    #([mod], "F7", lazy.spawn("playerctl play-pause")),
    #([mod], "F8", lazy.spawn("playerctl next")),

    # brillo
    #([mod], "F9", lazy.spawn("brightnessctl set 5%-")),
    #([mod], "F10", lazy.spawn("brightnessctl set +5%")), 

    # Volume
    #([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    #([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    #([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Brightness
    #([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    #([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
