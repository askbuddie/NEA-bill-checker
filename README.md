# NEA-bill

## Requirements

Required:

1. requests

## Installation

First, install pip:

```
sudo apt install python-pip
```

Then, clone the repository with `git clone` and you are ready to go.

```
git clone https://github.com/askbuddie/NEA-bill-checker.git
```

After cloning the repository, change the directory to ./NEA-bill-checker:

```
cd NEA-bill-checker
```

Now, you should install the requirements.

```
pip install requests
```

## Usage

1. Run the NEA Bill Checker:

```
python nea.py
```

It will display the current date and ask you to enter the **Sc. no.** from your bill.

2. Enter your **Sc. no.** and press enter and then it will ask you to enter your **Customer ID**.

3. Enter your **Customer ID** and then press enter.

4. Now, you should enter your **NEA Location** as in your Bill (for example; **BHARATPUR DC**) and then press enter.

Finally, you would be able to get the results on whether the Amount has been paid or not.
