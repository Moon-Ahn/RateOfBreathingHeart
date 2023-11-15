import xml.etree.ElementTree as ET
import csv

# Parse XML file
tree = ET.parse('export.xml')
root = tree.getroot()

# Open CSV file
with open('heart_rate_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["startDate", "value"])

    # Iterate through each record in the XML file
    for record in root.iter('Record'):
        # Check if the record is heart rate data
        if record.attrib['type'] == 'HKQuantityTypeIdentifierHeartRate':
            # Extract the start date and value
            start_date = record.attrib['startDate']
            value = record.attrib['value']

            # Write the data to the CSV file
            writer.writerow([start_date, value])