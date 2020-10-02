* __construct() method
	- if object is created it automatically called 
	```
	class ObjectInjection(){ // this is Object 
		public $data
		public function __construct($data){
			$this->data = $data
		}
	}
	$obj = new ObjectInjectio();
	}
	```
	- this mean that once you called new object, method all automatically load
* __destruct()
	- it execute __construct method inside him.
	```
	<?php
		class Fruit {
		  public $name;
		  public $color;
		  function __construct($name) {
		    $this->name = $name; 
		  }
		  function __destruct() {
		    echo "The fruit is {$this->name}.";  // name come from __construct method , i suppose that name inside __construct is global variable for __destruct.
		  }
		}
		$apple = new Fruit("Apple");
	?>
	```
	- use of maliciouse functions inside __destuct is leading to vulnerable
* __get
	- is read data from inaccessable properties 
	```
	$kid1= new kids;
	$kid1->wtf= 45; // where wtf is property, 45 = value
	``` 
	- 