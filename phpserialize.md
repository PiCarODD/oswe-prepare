* Due to serialize() and deserialize() functions
* to recontruct object 
	- b:<i>; where b mean boolean and <i> can be 0 or 1
	- s:<i>:"<s>"; where s mean string and <i> is length of string and <s> is string value
	- a:<i>:{<e>} where a stand for array and <i> is length of array and <e> is the element between array.
	- O:<i>:"<s>":<i>:{<p>} where O stand for Object and first <i> for length of object string second <i> stand for number of object properties and <s> stand for object name.<p> stand for properties.
* Vulnerable php classes
	* serialize Magic methods
	- __construct()
	- __sleep()
	- __toString()
	* Unserialize Magic Methods
	- __toString()
	- __destruct()
	- __wakeUp()
* PHP Magic methods https://culttt.com/2014/04/16/php-magic-methods/
* PHPgcc which can generate payload for deserialization attack like ysoserial https://github.com/ambionics/phpggc
**References**
https://www.exit.wtf/vrd/2019/04/04/Insecure_Deserialization.html
https://portswigger.net/web-security/deserialization/exploiting