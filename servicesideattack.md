* Also can me mark as SSRF,corss site request forgery
* SSRF can lead to 
	- Sensitive information disclosure
	- Stealing authentication information
	- File read/ inclusion
	- Remote Code Execution
* SSRF environments 
	- API specification imports (WSDL imports)
	- File imports
	- Connection to remote servers 
	- ping or alivecheck utilities
	- request that inclue URLs
* URL schemes for php
	- file:// -- Accessing local filesystem
	- http:// - access http urls
	- ftp:// - accessing ftp
	- php:// - accessing various I/I streams
	- zlib:// - compression streams
	- data:// - data(RFC 2397)
	- glob:// - find pathanme matching pattern
	- phar:// - PHP archive
	- ssh2:// - ssh
	- rar:// - rar
	- ogg:// audio
	- expect:// - process interaction streams
*
***REFERENCES***
- https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM/edit