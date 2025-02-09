# Receipt Processor

This project implements a web service that processes receipts and calculates points based on specific rules. The API endpoints include:

- `POST /receipts/process`: Process a receipt and return a unique receipt ID.
- `GET /receipts/{id}/points`: Retrieve the points awarded for a specific receipt by ID.

The API is defined in the [api.yml](./api.yml) file and adheres to the provided specification.

---

## Prerequisites

To run this application, you need:
- **Docker** installed on your machine.

---

## Running the Application with Docker

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tjc15b/receipt-processor-challenge.git
   cd receipt-processor-challenge
   ```

2. **Build the Docker Image:**
   Run the following command in the project root directory (where the `Dockerfile` is located):
   ```bash
   docker build -t receipt-processor-app .
   ```

3. **Run the Docker Container:**
   Start the container with the following command:
   ```bash
   docker run -p 8000:8000 --name receipt-processor-container receipt-processor-app
   ```

4. **Access the API:**
   - The application will be accessible at [http://localhost:8000](http://localhost:8000).
   - View the interactive API documentation at:
     - [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
     - [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)

---

## API Endpoints

### 1. **Process Receipts**
- **Endpoint:** `POST /receipts/process`
- **Description:** Accepts a JSON receipt and returns a unique ID.
- **Example Request:**
   ```json
   {
       "retailer": "Target",
       "purchaseDate": "2022-01-01",
       "purchaseTime": "13:01",
       "items": [
           {
               "shortDescription": "Mountain Dew 12PK",
               "price": "6.49"
           }
       ],
       "total": "6.49"
   }
   ```
- **Example Response:**
   ```json
   { "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
   ```

### 2. **Get Points**
- **Endpoint:** `GET /receipts/{id}/points`
- **Description:** Returns the points awarded for a receipt by ID.
- **Example Response:**
   ```json
   { "points": 32 }
   ```

---

## Stopping and Cleaning Up

To stop and remove the Docker container:
```bash
docker stop receipt-processor-container
docker rm receipt-processor-container
```

To remove the Docker image:
```bash
docker rmi receipt-processor-app
```


## Notes

- All data is stored in memory and will be lost when the application stops.

---
