# Assignment 4: Textual and Spatial Searching in MongoDB

## Objective
The assignment involves performing textual and spatial searches on business data stored in a MongoDB database.

## Setup Instructions

### Prerequisites
- MongoDB installed and running locally.
- Python with `pymongo` installed.

### Database Setup
1. Ensure MongoDB is running on `localhost:27017`.
2. Create a new database and collection, and load the `testData.json` file into MongoDB.

### Environment Setup
1. Place the provided `testData.json` file in the same directory as the script.
2. Ensure the `Assignment4_Interface.py` and `Assignment4_Tester.py` files are in the same directory.

## Execution

**Load the Data and Execute Functions:**
   - Run the `tester.py` script to:
     - Load business data into MongoDB.
     - Find businesses based on city and location criteria.
   - The results will be saved in `findBusinessBasedOnCity.txt` and `findBusinessBasedOnLocation.txt`.

   ```bash
   python tester.py
   ```

## Skills Gained
- Working with MongoDB in Python.
- Textual and spatial data querying using MongoDB.
- Basic geospatial calculations.
