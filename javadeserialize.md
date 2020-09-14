* Possible Serialization environments
	- Communication data to differnet syste/process, message brokers, web services
	- File systems, Cache Servers
	- Tokens, Cookies, HTML form, API auth tokens  
* Deserialized object start with "ac ed 00 05" in hexa format.Its signature like image magic header.Also can be note in base64 "rO0AB"
* Serialization in java is used of ObjectOutputStream to read user datas.Desrailzation is redObject() class.
* ClassNotFountException is signature to detect derserialization like sql injection.java.io.IOException mean our payload work.
* Java.lang.Runtime.getRuntime.exec(,,whoami) // commend execute with java
* Understand Object's Property 
	- Object.one.two
		- One is property of Object 
		- Two is a property of one
* Every property or method that is part of a nested exploit object is called a gadget
* to choose gadget is professional way.Ysoserial.jar https://github.com/frohoff/ysoserial can help noob like you.
* List of Java Object Types 
	- 0x71 - TC_REFERENCE
	- 0x72 - TC_CLASSDESC
	- 0x73 - TC_OBJECT
	- 0x74 - TC_STRING
	- 0x75 - TC_ARRAY
	- 0x76 - TC_CLASS
	- 0x7B - TC_EXCEPTION
	- 0x7C - TC_LONGSTRING
	- 0x7D - TC_PROXTCLASSDESC
	- 0x7E - TC_ENUM
	above type can be assum as pseudo codes in reverse engineering to exe.its just example for noob.
* We can get above types format using [!Java Serialization Dumper](https://github.com/NickstaDB/SerializationDumper) tools.
* extract serialization string from pcap network flow where 6666 is port number.
	```
	tshark -r deserialization.pcap -T fields -e tcp.srcport -e
	data -e tcp.dstport -E separator=, | grep -v ',,' | grep '^6666,'
	| cut -d',' -f2 | tr '\n' ':' | sed s/://g
	```
* Playground https://github.com/NickstaDB/DeserLab

***All these information are based on my opinion,so welcome to discuess about wrong useage, misunderstanding and any others***