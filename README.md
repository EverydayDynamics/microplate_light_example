# microplate_light_example

An example repository that shows how you can drive the microplate light on a Raspberry Pi using NeoPixels. This tutorial walks you through configuring the Pi, setting up Python, installing dependencies, and running the example script.

---

## Step 1: Configure PWM for NeoPixels

NeoPixels require precise timing via the Pi’s PWM hardware. Disable the onboard audio to free up the PWM channel.

Run:

```
sudo nano /boot/firmware/config.txt
```

Add this line at the end of the file:

```
dtoverlay=disable-audio
```

Save with Ctrl+O and exit with Ctrl+X, then reboot:

```
sudo reboot
```

---

## Step 2: Install Python Development Tools

Install the necessary Python development headers and virtual environment support:
```
sudo apt install python3-dev -y  
sudo apt install python3-venv -y
```
---

## Step 3: Create a Python Virtual Environment

Inside your project folder, create a virtual environment:
```
python3 -m venv .venv
```
Activate it:
```
source .venv/bin/activate
```
---

## Step 4: Install Dependencies

With the virtual environment active, install required Python packages:
```
pip install -r requirements.txt
```
These packages include:

- rpi_ws281x – the low-level NeoPixel driver  
- adafruit-circuitpython-neopixel – a user-friendly Python library for NeoPixels

---

## Step 5: Run the Example Script

NeoPixels require root access to control the GPIO hardware, so run the script with sudo:
```
sudo ./.venv/bin/python src/microplate_light_test.py
```
You should see your microplate light LEDs cycle through red, green, and blue.

---

You are now ready to experiment with your microplate light and build custom animations!

