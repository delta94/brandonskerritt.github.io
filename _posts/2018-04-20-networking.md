---
title: "Learning how to hack networks"
categories:
- University
---

Learn the fundamentals of networking by hacking. My name's Brandon. I have a level 4 HNC in Networking and a Microsoft Technology Assiocate qualfication in Networking.

# What is a network?

A network is a series of interleaved computers that each talk to eachother. Networks allow the __sharing__ of resources and __knowledge__.

Networks underpin everything we do in our day to day lives. Banks, blockchain, cryptocurrencies, phones, computers, the device you're reading this on all require networking.

# Where did networks come from?

Networks aren't only just computers. Networks exist in the human world. We have networks of friends, networks of family, road networks, light networks. Networks underpin everything.

Originally the computer network came from what is known as **ARPANET** (pronounced AR-PA-NET). ARPANET was the original computer network and the first network to implement all the rules and functions that make a network, a network.

![img](https://en.wikipedia.org/wiki/ARPANET#/media/File:Arpanet_map_1973.jpg)

This is an image of the ARPA network in 1973. There were so little computers on the network that the computer scientists and universities that used ARPANET kept a physical document of every device on the network. Now the internet is mind boggingly big.

When a user wanted to share a file with another user instead of meeting up in person they could just lay a bunch of wires and send them to eachother. This is the basis of the internet as we know it.

ARPANET was entirely wired. There were no wireless technologies in this network. It would well for North America where everything was connected by roads. When the internet (at the time it wasn't called the internet) tried to expand to Hawaii, Hawaii couldn't possibly lay down hundreds of wires over the sea. 

This is where **ALOHAnet** came in

# Centralised vs Decentralised networking

A centralised network is the current system of networking must often used by people. It is often called a **client-server** setup. You normally have 1 singular server dealing with multiple clients.

When you go to Google.com you are contacting Google's severs.

Decentralised networking is where every device talks to eachother and there are no servers. This is most used in pirating, Tor, Bitcoin, Blockchain and more. The internet started out as a decentralised entity but soon became centralised.

![img](https://qzprod.files.wordpress.com/2016/12/arpanet-logical-map-of-the-internet-september-1973.gif?w=633)

Here's what the internet used to look like. It was a purely peer to peer system. Let's say you wanted to know what the HTTP protocol did so you look for documentation. Easy right? Just go to a search engine and.. Oh. No search engines? Okay. That's easy. We'll just ask every single device on the internet where we can find the documentation for this protocol. It's easy because there's so little nodes on the network.

Let's say the network expands to 500 nodes and you all get sick and tired of asking every device if they have the file. So you put it on one single node and you say to every node "This file is at this node". So now whenever you want to find a file, you just simply tell people it's on this one node in the decentralised system.

Now let's remember that saving is expensive. This is a really slow internet era. So saving files is expensive, so we try not to save files when we can. Which is why we don't distribute the file and have every computer save it - hard drive space is precious in this time  and so is the internet speed. 

If everyone knows the file is at this node we don't need to save it or remember where the file was, we simply just visit this node.

Another file is needed, but this time it's on node 2. Not a problem. You simply tell everyone the file is on node 2. Still a decentralised system, just you know where the files are.

Eventually you get sick and tired of having to redownload this text file that tells you where all the usful files are, because hard drive space is precious and internet speed is slow. 

So you choose a new node to have a single text file of every single file and where that file is. This node writes some simple code. You send a message to the node "Hey, I want to know where ACDC_Lyrics.txt is" and the node uses an algorithm to reply "Hey, no worries! It's at node 6".

So now whenever someone new joins the network and they ask "hey! Where can I find this file?" You just point them at special-searching node which points them at the node which has the file.

Eventually parts of the network get sick with having network requests 24/7 for files, they don't want to constantly be giving out files. They're also confused in their own mini-network. Does Tim's computer have this file or Laurence's? So they make a new node which only deals with files and they don't have to deal with this problem anymore.

Everyone is really happy that they don't have to save a textfile of every single file on the network, that they can just ask this one single node who only deals with searching to find the file and it does it for them. This saves them so much space and time and memory.

Parts of the network are extremely pleased that they no longer have to have their personal computers on 24/7 when they can just have this special file computer do it all for them.

Now this is currently the state of the internet. We have Google (our searching node) and companies servers (file nodes). Even though we made completely logical steps to make our decentralisd system better we ended up with a centralised system. At some point the internet stopped being decentralised and it became centralised which in turn improved the whole network.

Having centralised servers inherently brings around a security risk. Instead of having to compromise 51% of the network (known as a [51% attack](https://learncryptography.com/cryptocurrency/51-attack)) a company has to protect a small family of servers from the outside world. The servers of Google are highly targeted.

# Networking Protocols

A protocol is a set of rules. Imagine speaking English to someone and they have a completely different set of gramatical rules to you.

You say:

> How are you?

And they say

> body your health?

Kinda confusing, right?

Well grammar allows us to speak the same language and understand one another.
Protocols allow applications to speak to each other in the same grammar and language.

Protocols are defined formally in a document called a Request for Comments (RFC). An RFC is created by the Internet Engineering Task Force (IEFT) that is the result of multiple meetings and reviews by third parties.

Really this is just a bunch of people getting together and discussing how exactly this protocol is going to work and putting it onto paper.

Any protocol that is widely used will be detailed in an RFC.

IEFT also releases an April Fools RFC since 1978. https://www.wikiwand.com/en/April_Fools%27_Day_Request_for_Comments

Protocols are interesting because if a vulnrabillity is found in a widely used protocol then any device implementing that protocol is suspectible to being hacked.
https://www.wired.com/story/krack-wi-fi-wpa2-vulnerability/

** Wireshark **

# IP

The Internet Protocol is a protocol which assigns addresses to every device on the internet.

# MAC

# OSI model