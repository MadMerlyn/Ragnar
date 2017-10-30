![Alt text](viking.png?raw=true "Viking")

Viking is a Discord bot written in Python 3 that utilizes [discord.py](https://github.com/Rapptz/discord.py) by [Rapptz](https://github.com/Rapptz).

## Getting Started

You will need to install [Python 3](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads).

## Requirements

You can install the requirements by running:
```
$ pip install -r requirements.txt
```


## Commands

### **Basic Commands**

***coinflip**
* Viking will flip a coin, and choose "Heads" or "Tails". (*eg.* **\*coinflip**)

***echo \<message>**
* Viking will use to text-to-speech to repeat the author's message. (*eg.* **\*echo hello world**)

***eightball \<question>**
* Viking will answer an author's question. (*eg.* **\*eightball is Viking the best?**)

***facts**
* Viking will provide the author with a random fact. (*eg.* **\*facts**)

***hello**
* Viking will respond with a random greeting. (*eg.* **\*hello**)

***quotes**
* Viking will return a random quotation. (*eg.* **\*quotes**)

***repeat \<amount> \<message>**
* Viking will repeat a message a specified amount of times. (*eg.* **\*repeat 5 hello world**)

***reverse \<message>**
* Viking will reverse the words in an author's message. (*eg.* **\*reverse hello world**)

### **Discord Commands**

***clear \<amount>**
* Viking will clear a specified amount of messages from a text channel. (*eg.* **\*clear 25**)

***help**
* Viking will list all available commands in the text channel. (*eg.* **\*help**)

***joined \<member>**
* Viking will return the date of when a specified Discord member joined the server. (*eg.* **\*joined Brayden**)

***members**
* Viking will return the total number of Discord members in the server. (*eg.* **\*members**)

***owner**
* Viking will mention the owner of the Discord server. (*eg.* **\*owner**)

***purge**
* Viking will purge all messages from a text channel. (*eg.* **\*purge**)

### **Games Commands**

***guess**
* Viking will play the Guessing Game. (*eg.* **\*guess**)

***rps**
* Viking will play Rock, Paper, Scissors. (*eg.* **\*rps**)

### **Giphy Commands**

***gif**
* Viking will return a random .gif. (*eg.* **\*gif**)

***search \<query>**
* Viking will return a random .gif that matches the search query. (*eg.* **\*search funny**)

***trending**
* Viking will return a random .gif from the trending page of Giphy. (*eg.* **\*trending**)

### **League of Legends Commands**

***live \<username>**
* Viking will give you a brief overview of everyone in your current game including: everyone's name, level, champion, rank and win/loss ratio (*eg.* **\*live Hiber**)

### **MongoDB Commands**

***monget \<username>**
* Viking will return a specified Discord member's Mongo database entries. (*eg.* **\*monget Brayden**)

***monquery \<query>**
* Viking will return Mongo database entries that match the search query. (*eg.* **\*monquery hello world**)

***monsave \<entry>**
* Viking will save an entry to the Mongo database. (*eg.* **\*monsave hello world**)

### **MySQL Commands**

***get \<username>**
* Viking will return a Discord member's MySQL database entries. (*eg.* **\*get Brayden**)

***register**
* Viking will register the author of the message in the MySQL database. (*eg.* **\*register**)

***save \<entry>**
* Viking will save an entry to the MySQL database. (*eg.* **\*save hello world**)

***users**
* Viking will return all registered Discord members in the MySQL database. (*eg.* **\*users**)

### **Weather Commands**

***forecast \<location>**
* Viking will return the forecast of a specified location. (*eg.* **\*forecast Edmonton AB**)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
