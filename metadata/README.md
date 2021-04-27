# Metadata

Using the package metadata, especially the `entry_points` specification, to discover plugins allows for maximum fleximbility in terms of naming the actual plugin and where to place them.

If the package is installed via pip and the entry point is specified, the collector can find it wherever it is.


First, to setup this example you have to run once:
```
cd .\wherever\mypackage
python -m pip install -e .
cd ..\..

cd .\wherever2\my2plugin
python -m pip install -e .
cd ..\..
```

Then to start the example run: `python main.py`