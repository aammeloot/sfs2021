# This an automated script using NMAP to scan ports on a host
# And exploiting the results of the scan to send the administrator
# an email informing them of vulnerabilities

import nmap
import smtplib
import datetime
from email.message import EmailMessage

# Variables for the email later down the line
email_content = ''
vuln_found = False

# To scan we need to create a PortScanner object
scanner = nmap.PortScanner()
scanner.scan('localhost')

# Take the host what scanned
current_host = scanner.all_hosts()[0]
scanresult = scanner[current_host]

# Create a list of ports that are 'dangerous'
dangerports = [22, 445]

# Get a list of all the ports that were open
tcp_ports = dict(scanresult['tcp'])
port_list = list(tcp_ports.keys())

# Main loop: check every port
for port in port_list:
    # If a match is found compose the email accordingly
    if port in dangerports:
        port_detail = tcp_ports[port]
        # Add an appropriate message into the email
        email_content += 'We found a vulnerable port:\n\n'
        email_content += 'Port number: ' + str(port) + '\n'
        email_content += 'Protocol: ' + port_detail['name'] + '\n'
        email_content += 'Product:' + port_detail['product'] + '\n\n'

        # Flag up that we have found a vulnerability
        if not vuln_found:
            vuln_found = True


# If we haven't found anything compose the email accordingly
if not vuln_found:
    email_content += 'No vulnerable port found'
        

# Create the email message
msg = EmailMessage()
msg.set_content(email_content)

msg['Subject'] = 'Security Report' + str(datetime.datetime.now())
msg['From'] = 'script@localhost'
msg['To'] = 'aurelien@localhost'

serv = smtplib.SMTP('localhost')
serv.send_message(msg)
serv.quit()



