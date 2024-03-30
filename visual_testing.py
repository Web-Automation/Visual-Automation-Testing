# Use this automation script for visual regression testing with Percy. 
# It uses basic selenium automation for crawling all the URLs along with that uses Percy for capturing screenshot and sending to percy dashboard using percy project token via API.
# It reads URLs from CSV files (live or UAT based on environment), launches Chrome in incognito mode, visits each URL, captures screenshots using Percy, and uploads them for comparison against baselines.
from percy import percy_snapshot
from selenium import webdriver
import sys
import csv
import os


# Function to read URLs from a CSV file
def read_urls_from_csv(file_path):
    urls = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row:
                urls.append(row[0])
    return urls

def main():
    # Determine build type based on environment variable or script argument (adapt as needed)
    is_live_build = (
        # Replace the variable $PERCY_BUILD_TAG in your terminal environment to capture the screenshot of particular URLs set i.e. UAT or Live/Production as per your need
        os.getenv("PERCY_BUILD_TAG") == "live"
        or "--build-tag live" in sys.argv
    ) 

    # Define separate CSV file paths for live and UAT environments
    live_csv_path = 'add the path of the csv file having live urls'
    uat_csv_path = 'add the path of the csv file having uat urls'

    # Read URLs from CSV files
    if is_live_build:
        urls = read_urls_from_csv(live_csv_path)
    else:
        urls = read_urls_from_csv(uat_csv_path)

    # Set up Selenium WebDriver with Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)

    try:
        # Capture and upload snapshots for URLs
        print("Capturing Snapshots...")
        for url in urls:
            driver.get(url)
            driver.implicitly_wait(10)
            # Capture snapshot with informative label
            snapshot_name = os.path.basename(url)
            percy_snapshot(driver, name=snapshot_name)

    finally:
        # Quit the driver
        driver.quit()

if __name__ == '__main__':
    main()
