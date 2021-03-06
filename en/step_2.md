## Draw a path

First let's draw the path that your character must follow.

+ Open the Tightrope Starter Trinket: <a href="http://jumpto.cc/tightrope-go" target="_blank">jumpto.cc/tightrope-go</a>.

    __The code to set up the Sense HAT has been included for you.__

+ Let's start by creating variables to store the colours you want to use. Remember that to set the colour of an individual LED, you need to say how much red, green and blue it should have.

	To create yellow, you'll need maximum red and green, and no blue:

	![screenshot](images/tightrope-yellow.png)

	(If you prefer, you can go to [jumpto.cc/colours](http://jumpto.cc/colours) and choose any colour you like!

+ You'll also need black pixels (or any colour you like) around the path.

	![screenshot](images/tightrope-black.png)

+ To draw your path, you first need to create a list containing the colour of each pixel.

	![screenshot](images/tightrope-path.png)

    __To save typing, you can copy the code from `snippets.py` in your project.__

	![screenshot](images/tightrope-snippets.png)

+ Next, you need to call `set_pixels` to display your path image on the Sense HAT.

	![screenshot](images/tightrope-set-pixels.png)

+ Click 'Run' to test your code. You should see a yellow pixel in the places that you've used your `y` variable, and no colour in the places that you've used `x`.

	![screenshot](images/tightrope-path-test.png)

