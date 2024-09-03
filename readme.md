# Amazon Price Tracker

This script tracks the price of a specific product on Amazon and sends an email notification if the price drops below a specified threshold.

## Overview

This script monitors the price of a Sony Bravia TV on Amazon. It fetches the current price of the product, and if the price drops below 1000.00 EUR, it sends an email notification with the updated price and a link to the product.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `smtplib` library (included with Python's standard library)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   ```

2. **Navigate to the project directory**:
```bash
   cd your-repository```
3. **Install the required Python libraries**:
```bash
   pip install requests beautifulsoup4
 ```

## Setup
1. **Update the script with your email credentials:**
my_email = "your-email@gmail.com"
my_password = "your-app-password"
```bash
  my_email = "your-email@gmail.com"
my_password = "your-app-password"
 ```
2. **Update the product URL(if needed)**
The script currently tracks the price of a Sony Bravia TV. If you want to track a different product, update the PRODUCT_URL variable with the URL of the new product.

```bash
   PRODUCT_URL = "https://www.amazon.es/your-product-url"
   ```


## Usage
To run the script, use the following command:
```bash
   python price_tracker.py
 ```

## How It Works
1. The script sends a request to Amazon and fetches the product's page.
2. It parses the HTML to find the product price.
3. If the price is less than or equal to 1000.00 EUR, it sends an email notification with the updated price and product link.

## Notes
The script uses smtplib to send email notifications via Gmail's SMTP server.
Make sure to handle your email credentials securely and avoid hardcoding sensitive information in your scripts.
Ensure that you have internet access when running the script, and the target product page structure hasn't changed.
## License 
This project is licensed under the MIT License - see the LICENSE file for details.