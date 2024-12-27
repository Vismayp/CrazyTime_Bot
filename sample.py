import requests
from datetime import datetime
import os

def fetch_and_save_webpage():
    # Create 'logs' directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Generate timestamp for filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'logs/tracksino_response_{timestamp}.txt'
    
    try:
        # Make the request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get('https://tracksino.com/crazytime', headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Save the response to a file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'Timestamp: {timestamp}\n')
            f.write(f'Status Code: {response.status_code}\n')
            f.write('Headers:\n')
            for key, value in response.headers.items():
                f.write(f'{key}: {value}\n')
            f.write('\nContent:\n')
            f.write(response.text)
            
        print(f'Response saved to {filename}')
        
    except requests.RequestException as e:
        error_filename = f'logs/error_log_{timestamp}.html'
        with open(error_filename, 'w', encoding='utf-8') as f:
            f.write(f'Error occurred at {timestamp}\n')
            f.write(str(e))
        print(f'Error occurred: {str(e)}')
        print(f'Error details saved to {error_filename}')

if __name__ == "__main__":
    fetch_and_save_webpage()