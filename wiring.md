# Hardware Wiring & Power Integration

This document details the hardware setup for the custom ESP32 vision payload.

## Camera Module Integration
The system utilizes an **OV2640 Camera Module**. 
* **Connection:** The camera interfaces directly with the ESP32 development board via the onboard FPC (Flexible Printed Circuit) connector. 
* **Data Pins:** Utilizes the standard D0-D7 parallel camera interface, along with SCCB (I2C) for sensor configuration.

## Power Delivery
Because the flight platform and the vision payload operate independently, careful consideration was given to power delivery to ensure the ESP32 does not draw excessive current from the drone's primary flight controller.

* **ESP32 Power:** [**Note for you: Update this sentence depending on what you actually did!** e.g., "The ESP32 is powered via a dedicated 3.7V LiPo battery stepped down to 3.3V, ensuring clean power separate from the noisy motor lines." OR "The ESP32 draws power directly from the drone's 5V auxiliary pad, regulated down to 3.3V on the development board."]

> **⚠️ Engineering Note:** The payload is electrically isolated from the flight controller's logic circuits. The ESP32 does not interface with the drone's motor PWM signals or IMU data, operating strictly as a stand-alone computer vision and transmission node.