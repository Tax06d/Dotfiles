if [[ $(xrandr -q | grep "HDMI-1 connected") ]]; then
	xrandr --output eDP-1 --primary --mode 1366x768 --rotate normal --output HDMI-1 --mode 1600x900 --rotate normal --right-of eDP-1
fi
