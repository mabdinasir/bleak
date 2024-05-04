# BLE Device Scanner and Model Number Reader

This Python project demonstrates how to scan for Bluetooth Low Energy (BLE) devices, connect to a specific device, and read its characteristic using the Bleak library.

## Installation

1. Clone the repository:
   - ` git clone https://github.com/mabdinasir/bleak.git `
2. Navigate to the project directory:
  - ` cd bleak `
3. Install the required dependencies: Bleak
  - pip3 install bleak

## Usage

1. Run the scanner script to scan for BLE devices and read the device name and characteristic. Modify and provide desired device name.
2. Run the main script to both scan for BLE devices and try a connection. Modify and provide desired device address and model number UUID.


## Project Structure

- `main.py`: The main script that orchestrates the scanning and connecting functionalities.
- `scanner.py`: Module containing functions to scan for BLE devices using BleakScanner.
- `connect.py`: Module containing functions to connect to a specific BLE device and read its model number using BleakClient.

## Configuration

- Modify the constants in `main.py` and `scanner.py` to customize the name, address and UUID of the desired BLE device, as well as the UUID of the model number characteristic.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](https://opensource.org/licenses/MIT) page for details.

## Acknowledgments

- [Bleak](https://github.com/hbldh/bleak) - A Bluetooth Low Energy (BLE) library for Python.



