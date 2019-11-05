alias reg-modem='atc at+cops?'
alias init-modem='atc at+cpin? && atc at+cimi && atc at+cops? && modem-cmd /dev/ttyACM1 at^smoni 2 && modem-cmd /dev/ttyACM1 at^swwan=1,1 3'
alias usb0ip='ip a sh dev wwan0'
alias modemip='atc at+cgpaddr'
alias showip='usb0ip && modemip && ip r'
alias ap-state='watch -n 3 -dc systemctl status hostapd' 
alias ap-stop='sudo systemctl stop hostapd' 
alias ap-start='sudo systemctl start hostapd' 
alias ap-enable='sudo systemctl enable hostapd' 
alias ap-disable='sudo systemctl disable hostapd' 
alias els81man-state='watch -n 3 -dc systemctl status els81-wwan-manager.service'
alias els81man-stop='sudo systemctl stop els81-wwan-manager'
alias els81man-start='sudo systemctl start els81-wwan-manager'
alias reset-els81='sudo els81-reset && sudo systemctl restart els81-wwan-manager &&  watch -n 10 -dc sudo systemctl status els81-wwan-manager.service'
alias plas9man-state='watch -n 3 -dc systemctl status plas9-wwan-manager.service'
alias plas9man-stop='sudo systemctl stop plas9-wwan-manager'
alias plas9man-start='sudo systemctl start plas9-wwan-manager'
alias reset-plas9='sudo plas9-reset && sudo systemctl restart plas9-wwan-manager &&  watch -n 10 -dc sudo systemctl status plas9-wwan-manager.service'
alias slog='tail -f /var/log/syslog'
