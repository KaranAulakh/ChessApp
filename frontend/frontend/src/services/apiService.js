// src/services/apiService.js
import axios from "axios";

// Create an instance of axios with the base URL
const API_BASE_URL = "http://localhost:5000";
const api = axios.create({
  baseURL: API_BASE_URL,
});

// Intercept the response to handle errors
api.interceptors.response.use(
  (response) => {
    return {
      success: true,
      data: response.data,
      errorMsg: "",
    };
  },
  (error) => {
    /* todo: send errors
    let errorMsg = "An error occurred";
    if (error.response && error.response.data && error.response.data.message) {
      errorMsg = error.response.data.message;
    }
      */
    return {
      success: false,
      data: {},
      errorMsg: error,
    };
  }
);

// Get calls
const getFromFlask = (path) => {
  return api.get(path);
};

export { getFromFlask };
