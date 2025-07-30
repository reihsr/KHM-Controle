#!/bin/bash
WID=$(xdotool search --name "khm")
echo $WID
xdotool windowactivate $WID
xdotool key --window $WID "Return"