### 2. Updated `BOM.md` (Bill of Materials)
This now focuses strictly on what you added, acknowledging the drone as a single component.

```markdown
# Bill of Materials (BOM)

This document outlines the hardware components used for the custom vision payload and the carrier platform.

| Component | Quantity | Purpose in System |
| :--- | :--- | :--- |
| **Commercial Drone Platform** | 1 | Carrier vehicle providing stable flight and lifting capacity for the payload. |
| **ESP32 Development Board** | 1 | Core payload microcontroller, handling visual data processing and Wi-Fi transmission. |
| **OV2640 Camera Module** | 1 | Captures visual data for structural crack detection. |
| **Custom Payload Mount** | 1 | [e.g., 3D printed bracket, zip ties, etc.] secures the ESP32 system to the drone chassis. |
| **Payload Power Source** | 1 | [Specify if you used a separate small LiPo (e.g., 3.7V 500mAh) or tapped into the drone's main battery] powers the ESP32 independently of the flight controller. |