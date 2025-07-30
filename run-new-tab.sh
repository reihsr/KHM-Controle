#!/bin/bash
WID=$(xdotool search --name "khm")
echo $WID
xdotool windowfocus $WID
xdotool key "Return"
sleep 4