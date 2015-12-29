#!/bin/bash

# while-menu-dialog: a menu driven system information program

DIALOG_CANCEL=1
DIALOG_ESC=255
HEIGHT=0
WIDTH=0


display_result() {
  dialog --title "$1" \
    --no-collapse \
    --msgbox "$result" 0 0
}


dialog_wrap() {
      exec 3>&1
      selection=$($1 2>&1 1>&3)
      exit_status=$?
      exec 3>&-
      case $exit_status in
        $DIALOG_CANCEL)
          clear
          echo "Program terminated."
          exit
          ;;
        $DIALOG_ESC)
          clear
          echo "Program aborted." >&2
          exit 1
          ;;
      esac
      echo $selection
}


main() {
    while true; do
      exec 3>&1
      selection=$(dialog \
        --backtitle "System Information" \
        --title "Menu" \
        --clear \
        --cancel-label "Exit" \
        --menu "Where would you like to go today?" $HEIGHT $WIDTH 4 \
        config "Fetch OpenVPN configuration" \
        update "force software update" \
        restart "restart" \
        2>&1 1>&3)
      exit_status=$?
      exec 3>&-
      case $exit_status in
        $DIALOG_CANCEL)
          clear
          echo "Program terminated."
          exit
          ;;
        $DIALOG_ESC)
          clear
          echo "Program aborted." >&2
          exit 1
          ;;
      esac
      case $selection in
        0 )
          clear
          echo "Program terminated."
          ;;
        config )
          result=$(echo "Hostname: $HOSTNAME"; uptime)
          display_result "System Information"
          ;;
        update )
          result=$(df -h)
          display_result "Disk Space"
          ;;
        restart )
          if [[ $(id -u) -eq 0 ]]; then
            result=$(du -sh /home/* 2> /dev/null)
            display_result "Home Space Utilization (All Users)"
          else
            result=$(du -sh $HOME 2> /dev/null)
            display_result "Home Space Utilization ($USER)"
          fi
          ;;
      esac
    done
}


dialog_wrap dialog \
        --backtitle "System Information" \
        --title "Menu" \
        --clear \
        --cancel-label "Exit" \
        --menu "Where would you like to go today?" $HEIGHT $WIDTH 4 \
        config "Fetch OpenVPN configuration" \
        update "force software update" \
        restart "restart" \

