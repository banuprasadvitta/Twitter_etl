# X ETL Pipeline

## Overview
This project extracts posts from a specific user's timeline (Elon Musk in this case) using the X API v2, processes the data, and saves it as a CSV file. The ETL pipeline is built using Python and Tweepy.

## Features
- Fetches the latest posts from a user's timeline
- Extracts key details such as text, likes, reposts, and timestamps
- Saves the cleaned data as a CSV file for further analysis
- Uses environment variables for secure API key management

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- `pip` (Python package manager)
- An X Developer account with API access

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/x-etl.git
   cd x-etl
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your X API keys:
   - Create a `.env` file in the project directory.
   - Add the following credentials:
     ```env
     X_CONSUMER_KEY=your_consumer_key
     X_CONSUMER_SECRET=your_consumer_secret
     X_ACCESS_KEY=your_access_key
     X_ACCESS_SECRET=your_access_secret
     ```

## Usage
Run the script to fetch and store posts:
```bash
python x_etl.py
```

If successful, a CSV file containing the post data will be generated in the project directory.

## Error Handling
- **401 Unauthorized**: Check if your API keys are correct and have the right permissions.
- **403 Forbidden**: Your X account might not have access to the v1.1 or v2 endpoints.
- **Rate Limits**: If you're making too many requests, you might need to wait or apply for Elevated Access in the X Developer Portal.

## Future Enhancements
- Store data in a database (e.g., PostgreSQL, MongoDB)
- Automate the ETL process using Apache Airflow
- Perform sentiment analysis on posts

## License
This project is licensed under the MIT License.

---
Feel free to contribute or reach out with any questions!

