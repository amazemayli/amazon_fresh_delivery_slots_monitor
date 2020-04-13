# Amazon Fresh Delivery Slots Monitor

Tired of swiping over and over again to see if Amazon Fresh slots are available? Use a script to do the heavy-lifting for you. Uses the following:

  - Python 3.6
  - Selenium
  - Twilio

Forked from: https://github.com/bryan3189/amazonfresh_delivery_slot_alerts

Original article: https://medium.com/better-programming/build-amazonfresh-delivery-slot-alerts-c9e12a429e23

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

5. Configure the application, please config.py 

6. Run the script

```sh
$ cd amazon
$ python fresh.py
```
