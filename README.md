# SuricataInsight

## Project Overview:

Name: SuricataInsight

Type: Data analysis and data visualization project

Purpose: Treat a CSV file for visualization using Python with Suricata and jq.

# Index
+ [Requirements](#requirements)
+ [Instalation](#instalation)
+ [Configuration](#configuration)
+ [Suricata execution](#suricata-execution)
+ [Python execution](#python-execution)
+ [How to contribute](#how-to-contribute)
+ [Contact](#contact)

## Requirements

First of all you need to install some tools and python libraries.

### Tools
+ [Suricata](https://suricata.io/)
+ [jq](https://jqlang.github.io/jq/)
+ [Poetry](https://python-poetry.org/)

## Python libraries
+ Pandas
+ matplotlib


## Instalation

### Poetry
For install the Poetrym use the command bellow: 
```bash
curl -sSL https://install.python-poetry.org | python3 -

```


### Suricata
For install suricata and jq, execute this code on Linux terminal
```bash
sudo apt-get update
sudo apt-get install jq
sudo apt-get install suricata
```
### Python libraries

For install the python libraries, you need to be in the same directory that the files: README.md, poetry.lock and pyproject.toml. After you are in the directory, use the command bellow:
```python3
poetry install
```


## Configuration
For the configuration, you only need create a directory and upgrade the suricata. For upgrade the suricata is very simple, you just need to upgrade the rules and move the suricata.rules, for a directory created . Moving this suricata.rules, will be easier to execute and found this file

#### Creating directory

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




## Suricata execution

In this code, I left 2 pcaps as [example](https://github.com/kaykRodr1gu3s/SuricataInsight/tree/main/csv_file), they are: [2022-03-14-Qakbot-with-Cobalt-Strike-and-VNC-module](https://www.malware-traffic-analysis.net/2022/03/16/index.html) and [2023-11-20-DarkGate-infection-traffic.pcap](https://www.malware-traffic-analysis.net/2023/11/20/index.html). All these pcap are avaliable on [malware-traffic-analysis](https://www.malware-traffic-analysis.net). You can use any pcap, might be your or any that you have downloaded.

### Executing suricata
Now that we downloaded and created all that we need, let's execute the suricata.

```bash
suricata -r 2022-03-14-Qakbot-with-Cobalt-Strike-and-VNC-module.pcap  -S suricata.rules -v -l .

```
### Jq parser

After that you [execute the suricata](#executing-suricata) will generate some files, the file that we will use, will be the eve.json. The eve.json is a json file that contanis all the packet in the pcap file saved as json. We will parse this json usin the jq tool, colleting all the alerts and saving this alerts in csv.


For parse the json, use this code:


```bash
jq -r 'select(.event_type == "alert") | [.timestamp, .src_ip, .src_port, .dest_ip, .dest_port, .event_type, .alert.severity, .alert.signature] | @csv' eve.json | sort -d > ~/Documentos/Suricata_rules/pcap_content.csv

```


## Python execution

Now that all the datas is prepared for analysis , just need to execute the [python code](https://github.com/kaykRodr1gu3s/SuricataInsight/blob/main/Main.py).

The code will import all the [libraries](#python-libraries) and will import some code that are saved on [tools directory](https://github.com/kaykRodr1gu3s/SuricataInsight/tree/main/tools).The tools is the code that are used for change the [current directory](https://github.com/kaykRodr1gu3s/SuricataInsight/blob/main/tools/directory_helper.py) and for [plot all datas](https://github.com/kaykRodr1gu3s/SuricataInsight/blob/main/tools/plot.py) with matplotlib.

When the code finished, will open some window on your computer, it's all data that was plot, just need to close the window for the outhers plots be completed. All the plots is saved on [visualization](https://github.com/kaykRodr1gu3s/SuricataInsight/blob/main/tools/plot.py).



## how to contribute
 1. Fork the repository.
 2. Create a branch for your contribution: `git checkout -b feature-nova`.
 3. Make the desired changes and commit: `git commit -m "Add new functionality"`.
 4. Push to your branch: `git push origin new-feature`.
 5. Open a pull request.




## Contact

- Linkedin: [Kayk Rodrigues](https://www.linkedin.com/in/kayk-rodrigues-504a03273)
- Telegram: [Kayk Rodrigues](https://t.me/kaykRodrigues)
