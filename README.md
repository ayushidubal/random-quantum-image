# random-quantum-image
Generates an image that consists of red, blue and green pixels randomly generated by IBM's quantum computer. The probabilities of the colours can be varied to approximate the desired shade.

This code was written in an attempt to build a logo for the [quantum chessboard](https://github.com/SEDSCelestiaBPGC/quantum-chess.git).

### What the code does

Generates an approximation to the colour you want using randomly generated red/blue/green dots generated with the probability of the ratio of the colour in its hex code. The generation is truly random as it is done using a [quantum random number generator](https://quantumcomputinguk.org/tutorials/16-qubit-random-number-generator) run on the [IBM Quantum Experience](https://quantum-computing.ibm.com/). This makes this code a very basic application of a QRNG.

### Requirements

**Qiskit** (supported by Python 3.5 or later)

Get it by running the following command
```
pip install qiskit
```

**Pygame**

Get it by running the following command
```
pip install pygame
```

### How to use this code

Run the `Random_colours.py` file on the [IBM Quantum Experience](https://quantum-computing.ibm.com/). This should take about 5 minutes to give you a result, since we are generating 40,000 random numbers using the quantum circuit!

Copy and paste the output into the `generated_cols` list in the file `QuantumLogo.py`.

Run! You should find a file named `Colour.jpeg` saved in the directory where `QuantumLogo.py` is saved.

The current circuit is set to a probability of 25%, 37.5% and 37.5% for r,g,b respectively. That means that the generated image should approximate this colour, which has an rgb value of (64, 96, 96):

![](https://github.com/ayushidubal/random-quantum-image/blob/main/Samples/Expected.jpg)

This is what we get:

![](https://github.com/ayushidubal/random-quantum-image/blob/main/Samples/Colour.jpeg)

It's not a great result, but I was still proud :)

### Changes you can make

Feel free to play around with the circuit to approximate the colour that you want by checking its rgb code and computing the relative measure of each r/g/b value and mapping it to an output state. You can also change the order of elements in `clrs` for convenience. (It's currently set to [r,g,b]).

You can increase the accuracy of the generated colour to what you want by increasing the 'resolution'. You can do this by increasing the number of random numbers generated by tweaking the code in a couple of places.

Have fun!
