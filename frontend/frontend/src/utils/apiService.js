// src/services/apiService.js
import axios from "axios";

// Create an instance of axios with the base URL
const API_BASE_URL = "http://localhost:5001";
const api = axios.create({
  baseURL: API_BASE_URL,
});

// Intercept the response to handle errors and API formatting
api.interceptors.response.use(
  (response) => {
    return {
      success: true,
      data: response.data,
      errorMsg: "",
    };
  },
  (error) => {
    return {
      success: false,
      data: {},
      errorMsg: error,
    };
  }
);

// Handle Get Calls from the api
const apiServiceGET = (path) => {
  return api.get(path);
};

export { apiServiceGET };
