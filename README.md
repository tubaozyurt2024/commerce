
## Product Price Listing Web Application
A simple web application that displays a list of products and their details fetched from an external API. 
Built using Next.js for the frontend and Python (Fast API) for the backend, this application provides an 
efficient way to view products and view detailed information.

## Features
- **Product List:** Displays a list of products with real-time data fetched from an external API.
- **Product Details:** View detailed information about each product on its own page.
- **Responsive Design:** Fully responsive design ensures smooth user experience across devices.
- **External API Integration:** Fetches product data from a third-party API and integrates it into the app.

## Setup Instructions
## Install Dependencies

### Frontend:
Navigate to the frontend directory and install the necessary dependencies.

```bash
cd frontend
npm install
```
### Backend:
Navigate to the backend directory and install the necessary dependencies.

```bash
cd backend
pip install -r requirements.txt
```

## Run the Application
### Frontend:
To run the frontend, use the following command:

```bash
npm run dev
```

### Backend:
To start the backend server, use:

```bash
uvicorn main:app --reload
```
