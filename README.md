# Parallelized Python Image Conversion

A script to augment images using python.

### Prerequisites

* Python3
* Python packages
	* Standard library
	* numpy
	* matplotlib

```
pip install numpy
pip install matplotlib
```

### Arguments

* --conversion_type	(-C)
	* B		Black-and-white
	* G		Greyscale
	* I 	Invert
	* R		Redshift
* --processes		(-P)
	* (int)	Number of processes to use
* --help			(-H)
	* Display help menu

## Usage

### This converts example1.JPG to a black-and-white version. 
```
python convert.py example1.JPG -C B
```

![alt text](examples/bw.JPG)


### This converts example1.JPG to a greyscale version. 
```
python convert.py example1.JPG -C G
```

![alt text](examples/greyscale.JPG)


### This converts example1.JPG to an inverted version. 
```
python convert.py example1.JPG -C I
```

![alt text](examples/invert.JPG)


This converts example1.JPG to a redshift version. 
```
python convert.py example1.JPG -C R
```

![alt text](examples/redshift.JPG)


This displays the help menu
```
python convert.py -h

### Authors

* **Nathan Brooks** - *development* - [N8Brooks](https://github.com/N8Brooks)
* **Curtis Bean** - *development* - [westlin3](https://github.com/westlin3)

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details