# Mutstring

## Make your Python strings mutable

please never use this ever oh god please

### Quick Example

```py
import mutstring

a = "hello"
a.capitalize()
print(a)  # Hello

mutstring.cleanup()
```

### Installation

#### Linux/macOS

```
python3 -m pip install -U mutstring
```

#### Windows

```
py -3 -m pip install -U mutstring
```

### Features

-   Bad code
-   Segfaults
-   Breaks about every library to exist

### Why does this exist?

i don't know. see [my other library](https://github.com/ZeroIntensity/pointers.py), which this is built on top of.

### Usage

If you want to use this awful library, just import it and call cleanup at the end of your script to prevent a segfault:

```py
import mutstring

"hello {}".format("world")
print("hello {}")  # hello world

mutstring.cleanup()
```
