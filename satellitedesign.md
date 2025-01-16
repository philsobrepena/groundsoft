# imitating  a few satellites from muon space:
## musat = envsat
## firesat,
## halo = lowsat
## vindler = rfsat

#Goals

## Each satellite is a complete, independent module
## Clear separation of concerns
## Mimic real-world satellite mission organization
## Easy to add new satellite types
## Shared components are clearly separated

project_root/
│
├── satellites/
│   ├── envsat1/
│   │   ├── envsat1_main.py      # Core simulation script
│   │   ├── telemetry.py         # Simulates health and status checks
│   │   ├── sensors.py           # Simulates environmental sensor data
│   │   └── config.yaml          # Configuration file
│   │
│   ├── musat2/
│   │   ├── musat2_main.py       # Core simulation script
│   │   ├── telemetry.py         # Simulates health and status checks
│   │   ├── weather_data.py      # Simulates advanced weather data
│   │   └── config.yaml          # Configuration file
│   │
│   ├── firesat/
│   │   ├── firesat_main.py      # Core simulation script
│   │   ├── telemetry.py         # Simulates health and status checks
│   │   ├── radiation_data.py    # Simulates radiation and wildfire-related data
│   │   ├── real_time_alerts.py  # Simulates real-time wildfire alerts
│   │   └── config.yaml          # Configuration file
│   │
│   ├── lowsat/
│   │   ├── lowsat_main.py       # Core simulation script
│   │   ├── telemetry.py         # Simulates health and status checks
│   │   ├── mission_data.py      # Simulates data from customizable payloads
│   │   └── config.yaml          # Configuration file
│   │
│   ├── rfsat/
│   │   ├── rfsat_main.py        # Core simulation script
│   │   ├── telemetry.py         # Simulates health and status checks
│   │   ├── rf_monitoring.py     # Simulates RF signal monitoring data
│   │   ├── spectrum_analysis.py # Simulates spectrum analysis and interference patterns
│   │   ├── geolocation.py       # Simulates geolocation of signal sources
│   │   └── config.yaml          # Configuration file
│
├── shared/
│   ├── data_pipeline.py         # Handles common data transmission and downlink logic
│   ├── utils.py                 # Utility functions shared across satellites
│   ├── logger.py                # Centralized logging system for all satellites
│   ├── constants.py             # Common constants (e.g., frequency bands, units)
│   └── telemetry_template.py    # Base class or template for telemetry data
│
├── tests/
│   ├── test_envsat1.py          # Unit tests for envsat1 scripts
│   ├── test_envsat2.py          # Unit tests for envsat2 scripts
│   ├── test_firesat.py          # Unit tests for FireSat scripts
│   ├── test_lowsat.py           # Unit tests for lowsat scripts
│   ├── test_rfsat.py            # Unit tests for rfsat scripts
│   └── test_shared.py           # Unit tests for shared components
│
├── data/
│   ├── raw/                     # Stores raw simulated data from satellites
│   ├── processed/               # Stores processed and aggregated data
│   ├── logs/                    # Logs from simulation runs
│   └── config_examples/         # Example configuration files for satellites
│
└── README.md                    # Project documentation
