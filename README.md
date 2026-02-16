# 🚇 MBTA Real-Time Tracker

A command-line application for tracking real-time MBTA arrivals in Boston. Built with Python and the official MBTA V3 API.

## Features

- **Real-time predictions** for subway and bus arrivals
- **Auto-refresh** every 30 seconds
- **Multiple stop support** including:
  - North Station
  - Harvard Square
  - Kenmore
  - Ruggles
  - Northeastern (Green Line)
  - Bus 39 stops
- **Clean terminal display** with arrival times in minutes
- **Color-coded route information**

## Screenshots
```
🚇 MBTA Tracker
Select a stop:
1. North Station
2. Harvard Square
3. Kenmore
4. Ruggles
5. Northeastern (Green Line)
6. Bus 39 - Longwood Medical

Enter number: 5

🚌 Northeastern (Green Line - E)
==================================================
Green-E  →       2 min
Green-E  →       8 min
Green-E  →      15 min
```

## Requirements

- Python 3.7 or higher
- `requests` library
- `python-dotenv` library
- MBTA API key (free)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mbta-tracker.git
cd mbta-tracker
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Get your MBTA API key**
   - Visit https://api-v3.mbta.com/
   - Register for a free API key

5. **Configure your API key**

Create a `.env` file in the project root:
```
MBTA_API_KEY=your_api_key_here
```

## Usage

Run the tracker:
```bash
python mbta_tracker.py
```

Select a stop by entering its number, and the app will display real-time predictions that auto-refresh every 30 seconds.

Press `Ctrl+C` to exit.

## Project Structure
```
mbta-tracker/
├── mbta_tracker.py      # Main application
├── requirements.txt     # Python dependencies
├── .env                 # API key (not tracked in git)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Configuration

### Adding Custom Stops

To add your own stops, find the stop ID from the MBTA API and add it to the `stops` dictionary in `main()`:
```python
stops = {
    "1": ("stop-id-here", "Stop Name"),
}
```

Find stop IDs at: https://api-v3.mbta.com/stops

### Available Stops in This Version

- **North Station** - Major transit hub
- **Harvard Square** - Red Line
- **Kenmore** - Green Line B/C/D
- **Ruggles** - Orange Line
- **Northeastern University** - Green Line E
- **Bus 39 - Longwood Medical** - Connects Mission Hill to Back Bay

## API Information

This project uses the [MBTA V3 API](https://api-v3.mbta.com/). The API provides:
- Real-time vehicle predictions
- Schedule information
- Route details
- Stop locations

Rate limit: 1000 requests per minute (more than enough for this app)

## Future Improvements

- [ ] Add more bus routes (1, 8, 47, CT2)
- [ ] Save favorite stops
- [ ] Desktop notifications for arriving trains
- [ ] Web interface version
- [ ] Display train direction/destination
- [ ] Filter by specific route at multi-route stops
- [ ] Show service alerts and delays

## Troubleshooting

**"requests module not found"**
```bash
pip install -r requirements.txt
```

**"No predictions available"**
- Check if the T is running (late night service ends ~12:30 AM)
- Verify your API key is correct in `.env`
- Some stops may have no scheduled service at certain times

**API key errors**
- Make sure `.env` file exists in the project root
- Check that the API key has no extra spaces
- Verify the key is still valid at https://api-v3.mbta.com/

## Contributing

Feel free to fork this project and submit pull requests! Some ideas:
- Add more Boston-area stops
- Implement filtering by route
- Add color-coded route badges
- Create a GUI version

## Author

**Valentina** - Computer Science & Music Technology @ Northeastern University

Built as part of a portfolio of Python projects demonstrating API integration and real-time data handling.

## License

MIT License - feel free to use and modify for your own projects.

## Acknowledgments

- MBTA for providing the excellent V3 API
- Northeastern University community for inspiration
