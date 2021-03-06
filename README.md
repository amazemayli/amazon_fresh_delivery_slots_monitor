# Amazon Fresh Delivery Slots Monitor

Tired of swiping over and over again to see if Amazon Fresh slots are available? Use a script to do the heavy-lifting for you. Solution leverages the following:

  - Python 3.8.2
  - Selenium
  - Twilio

Forked from: https://github.com/bryan3189/amazonfresh_delivery_slot_alerts

Original article: https://medium.com/better-programming/build-amazonfresh-delivery-slot-alerts-c9e12a429e23

### Twilio Configuration

Get a free Twilio account here: https://www.twilio.com/referral/RJhglh

### Setup Instructions For Brand New Machine

1. Install Chrome: https://www.google.com/chrome/

2. Install Python: https://www.python.org/downloads/

3. Install iTerm2: https://www.iterm2.com/

4. Open iTerm2 and run the following:

Install Command Line Tools

```sh
$ xcode-select --install
```

Install PIP

```sh
$ sudo easy_install pip
```

Install Twilio

```sh
$ sudo pip install twilio --ignore-installed six
```

Install rest of the required packages

```sh
$ sudo pip install -r requirements/requirements.txt
```

5. Configure the application, please open and edit config.py 

6. Run the script

```sh
$ cd amazon
$ python fresh.py
```

### Checkout Experience Compatability

Unlike this Apple Script solution (https://github.com/ahertel/Amazon-Fresh-Whole-Foods-delivery-slot-finder/), which only works with select Amazon Fresh subscribers, this Python version out-of-the-box works with users who get the following check out experience.

![Bay Area](https://i.imgur.com/KVRw0oA.png)

If your Amazon Fresh checkout experience looks a bit different, it's possible inspect the elements on the page and change a few lines of the Python code to accommodate.

### 2FA Compatability

Furthermore, this Python version takes into consideration reserving sufficient time for passing 2FA. The amount of seconds the script waits can be adjusted easily.
