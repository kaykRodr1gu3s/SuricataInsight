# SuricataInsight

This is a data analisys and data visualization project, this project treat a csv file to visualization with python.

# Index
+ [Requirements](#requirements)
+ [Instalation](#instalation)
+ [Configuration](#configuration)




## Requirements

First of all you need to install some tools and python libraries.

### Tools
+ [Suricata](https://suricata.io/)
+ [jq](https://jqlang.github.io/jq/)

## Python libraries
+ Pandas
+ matplotlib


## Instalation

### Suricata
For install suricata and jq, execute this code on Linux terminal
```bash
sudo apt-get update
sudo apt-get install jq
sudo apt-get install suricata
```
### Python libraries

```python3
pip install -r requirements.txt
```


## Configuration
For the configuration, you only need create a directory and upgrade the suricata. For upgrade the suricata is very simple, you just need to upgrade the rules and move the suricata.rules, for a directory created . Moving this suricata.rules, will be easier to execute and found this file

#### making directory

```
cd Documents
mkdir suricata
```

#### Suricata upgrade
 ```bash
sudo apt-get upgrade suricata
```
when execute this code, all your rules was upgrade, your rules file is located on /var/lib/suricata/rules

#### Copying the rules

We will copy the suricata.rules to our directory that was created.

```bash
cd /var/lib/suricata/rules

cp suricata.rules ~/Documents/suricata
```




## Execution

In this code, I left 2 pcaps as example, they are: [2022-03-14-Qakbot-with-Cobalt-Strike-and-VNC-module](https://www.malware-traffic-analysis.net/2022/03/16/index.html) and [2023-11-20-DarkGate-infection-traffic.pcap](https://www.malware-traffic-analysis.net/2023/11/20/index.html). All these pcap are avaliable on [malware-traffic-analysis](https://www.malware-traffic-analysis.net). You can use any pcap, might be your or any that you have downloaded.

### executing suricata
Now that we downloaded and created all that we need, let's execute the suricata.

```bash
suricata -r 2022-03-14-Qakbot-with-Cobalt-Strike-and-VNC-module.pcap  -S suricata.rules -v -l .

```

```
aaaaaaaa
```





