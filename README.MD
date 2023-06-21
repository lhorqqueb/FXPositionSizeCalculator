# FXPositionSizeCalculator

A comprehensive Forex trading tool developed in Python for calculating the position size of a trade. This application helps manage risk by determining the correct position size based on account balance, risk percentage, stop loss, and real-time currency pair prices. It features a simple graphical user interface and utilizes Alpha Vantage API for real-time forex data.

## Features

- Enter account balance, risk percentage, and stop loss in pips.
- Provides real-time currency pair prices using Alpha Vantage API.
- Calculates the amount at risk in USD.
- Determines the position size in units and lots (standard, mini, micro).

## Installation

Ensure that you have Python 3 and pip installed on your system. You can download and install Python from the official website: https://www.python.org/

1. Clone this repository into your local machine:

```git clone https://github.com/yourusername/FXPositionSizeCalculator.git```

2. Navigate to the project directory:

```cd FXPositionSizeCalculator```

3. Install the necessary Python packages:

```pip install -r requirements.txt```

4. Run the application:

```python main.py```


Note: The executable version of this program can be created using `PyInstaller`.

## How to Use

1. Enter your account balance, risk percentage, stop loss, and the currency pair for the trade.
2. Click "Calculate" to compute the position size and risk amount.
3. Results are displayed in terms of amount at risk (USD), position size (units), standard lots, mini lots, and micro lots.

## Contributing

Contributions are welcome! Here are a few ways you can help:

- Report bugs: Open an issue detailing the bug and how to reproduce it.
- Suggest enhancements: Open an issue detailing your ideas for how to improve the project.
- Submit pull requests: Fork this repository, make changes, and submit a pull request. We'll review it and get back to you.

Before contributing, please read our Contributing Guidelines and Code of Conduct.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


