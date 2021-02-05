"use strict";

// import Vue from "vue";
import axios from "axios";
// import store from "../store";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

axios.defaults.baseURL = SERVER_URL;
// Full config:  https://github.com/axios/axios#request-config
//  axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// let config = {
//   baseURL: `${process.env.baseURL}`,
//   // baseURL: process.env.baseURL || process.env.apiUrl || ""
//   timeout: 60 * 1000, // Timeout
//   withCredentials: true // Check cross-site Access-Control
// };

// const axios = axios.create(config);

// Add a request interceptor
axios.interceptors.request.use(
  function(config) {
    // // Do something before request is sent

    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
axios.interceptors.response.use(
  function(response) {
    console.log(response);
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    return error;
  }
);

// Plugin.install = function(Vue) {
//   Vue.axios = _axios;
//   window.axios = _axios;
//   Object.defineProperties(Vue.prototype, {
//     axios: {
//       get() {
//         return _axios;
//       }
//     },
//     $axios: {
//       get() {
//         return _axios;
//       }
//     }
//   });
// };

// Vue.use(Plugin);

export default axios;
