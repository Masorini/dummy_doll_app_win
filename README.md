# Intelligent Cockpit Child Left-Behind Target Control System

## Project Structure Documentation

### Directory Tree
```bash
dummyDoll/
├── README.md
├── main.py                     # Application entry point
│
├── app/                        # Frontend Application
│   ├── core/                   # Core framework components
│   │   ├── __init__.py
│   │   ├── config.py           # UI configuration (fonts/colors/etc)
│   │   ├── main_window.py      # Main window management
│   │   ├── pages/              # Control pages
│   │   │   ├── __init__.py
│   │   │   ├── base_page.py    # Base page class
│   │   │   ├── library.py      # Motion library management
│   │   │   ├── manual.py       # Manual control
│   │   │   ├── offline.py      # Offline mode
│   │   │   ├── posture.py      # Posture configuration
│   │   │   ├── realtime.py     # Real-time debugging
│   │   │   └── teaching.py     # Teaching programming
│   │   │
│   │   └── widgets/            # Custom widgets
│   │       ├── __init__.py
│   │       ├── param_input.py  # Parameter input component
│   │       ├── joint_slider.py # Joint slider with limits
│   │       └── status_led.py   # Status indicator light
│   │
│   ├── resources/              # Frontend resources
│   │   └── icons/
│   │       ├── warning.png
│   │       └── warning2.png
│   │
│   └── views/                  # Composite views
│       ├── connection_view.py  # Device connection view
│       └── dashboard_view.py   # Data dashboard
│
├── backend/                    # Backend Services
│   ├── services/               # Core services
│   │   ├── control_service.py  # Motion control service
│   │   └── device_manager.py   # Device connection management
│   ├── protocols/              # Communication protocols
│   │   ├── doll_v1_protocol.py # Protocol V1
│   │   └── doll_v2_protocol.py # Protocol V2 (extensible)
│   ├── drivers/                # Hardware drivers
│   │   ├── motor_driver.py     # Motor driver interface
│   │   ├── serial_adapter.py   # Serial communication
│   │   ├── wifi_driver.py      # WiFi communication
│   │   └── bluetooth_driver.py # Bluetooth communication
│   └── utils/                  # Utilities
│       ├── logger.py           # Logging system
│       └── config_loader.py    # Configuration loader
│
├── config/                     # Configuration files
│   ├── device_config.yaml      # Device parameters (baud rate/joint mapping)
│   ├── ui_config.json          # UI layout configuration
│   └── style_config.py         # Style configuration (upgraded from core/config.py)
│
├── hardware/                   # Hardware Interface Simulation
│   └── dummy_mcu/              # MCU simulator
│       ├── firmware.py         # Virtual firmware
│       └── serial_emulator.py  # Virtual serial port
│
├── tests/                      # Testing modules
│   ├── unit/                   # Unit tests
│   └── integration/            # Integration tests
│
└── docs/                       # Documentation
    └── protocol_spec.md        # Protocol specification
```
**Key Terminology**:
- **Frontend Application**: User interface components

- **Backend Services**: Background processing and hardware communication

- **Protocols**: Communication specifications between software and hardware

- **Drivers**: Hardware interface implementations

- **MCU**: Microcontroller Unit (the doll's control board)

- **Posture Configuration**: Body position/movement setup

- **Teaching Programming**: Motion path recording/playback system

This structure follows modern software development practices with clear separation of concerns between presentation layer (app), business logic (backend), and configuration. The hardware simulation module enables development without physical devices.

### File Responsibilities

| File/Directory             | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `main.py`                | Application entry point, initializes QApplication and main window          |
| `core/main_window.py`     | Main window implementation containing:<br>• Navigation management<br>• Page stack layout<br>• Global state control |
| `core/config.py`          | Central configuration management:<br>• UI stylesheets (StyleSheet)<br>• Component dimensions (Dimensions) |
| `core/pages/base_page.py` | Base page class providing:<br>• Unified layout standards<br>• Common component methods |
| `core/pages/offline.py`   | Offline control page features:<br>• Status monitoring table<br>• Action loading control<br>• Power management |
| `core/pages/realtime.py`  | Real-time debugging page features:<br>• Parameter input validation<br>• Action execution control<br>• Data communication management |
| `core/widgets/`           | Custom component library:<br>• Parameter input fields<br>• Status indicators<br>• Industrial-style buttons |
| `resources/`              | Resource file storage:<br>• Icon resources (.ico/.png)<br>• Localization files<br>• Documentation templates |

## Operation Instructions

### Environment Requirements
```bash
Python 3.8+ 
PyQt5 == 5.15.4
```
### Launch Application
```bash
python3 main.py
```
### Configuration Guide
1. Modify UI styles in core/config.py under StyleSheet class
2. Adjust component dimensions in Dimensions class constants
3. Add new pages:
   - Create new module in pages directory 
   - Implement page logic inheriting from BasePage 
   - Register page in main_window.py
