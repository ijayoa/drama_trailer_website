# South Korean Drama Trailer Website

This project generates a website that displays a list of South Korean dramas. What to expect? It will; 
- Display drama title and poster.
- Show drama trailer video from youtube.

# How to run this project

_This document assumes you are using a MAC, if you are on Linux or Windows the commands will vary, but you should be able to search google for alternatives given the explanation provided here._

### Getting started

- Install Python version 2.7 - [Download and install](https://www.python.org/downloads/)
- Download a code editor - [Sublime text 3](https://www.sublimetext.com/3)
- Install a web browser - I personally recommend using [Google Chrome](https://www.google.com/chrome/)
- Use [git](https://help.github.com/articles/fork-a-repo/) to clone this respository and save a local copy on your machine.

Once you have all the tools listed above installed, there are two ways you can run this project, from [Python's Idle](https://docs.python.org/2/library/idle.html) or Sublime Text 3

### Using Python Idle

1. Open `Spotlight`, type in `Idle` and hit `Enter`
1. On the top navigation tab, click File > Open
1. Navigate to the project folder, select the file `entertainment_center.py` and click Open
1. Again, On the nav tab, click Run > Run Module

This should open your web browser and generate the website.

### Using Sublime Text 3

1. Open `Spotlight`, type in `Sublime Text` and hit `Enter`
1. On the top navigation tab click File > Open
1. Navigate and select to the project folder, select the file `entertainment_center.py` and click Open
1. On the top nav, click Tools > Build

This should open your web browser and generate the website.

# Possible Issues

- Running two versions of python on your PC? This may cause some troubles, so ensure you are using Python 2's Idle to run this.
- The trailers are loaded from youtube, so you'll need good wifi connection.

# Customization Tips
- You can create more or delete drama instances in `entertainment_center.py`. 
- Add more attributes of a drama like cast or reviews by changing `media.py`'s  `__init__` function.

