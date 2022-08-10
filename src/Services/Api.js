import axios from "axios";

const errHandler = async (promise) => {
  try {
    const res = await promise;
    return [res, null];
  } catch (err) {
    console.log(err);
    return [null, err];
  }
};

const ApiService = {
  init: (baseUrl) => {
    axios.defaults.baseURL = baseUrl;
  },

  setHeader: () => {
    axios.defaults.headers.common["Authorization"] =
      "Bearer AAAAAAAAAAAAAAAAAAAAAAjSfgEAAAAA0ZhsUmkuVAkcQtYR22n3BEOrhdM%3DXfkFhboNOrokarYncqFNFgCXatIkIuoBkTCoHMbN1c8583CIqo";
  },

  get: (url, config) => {
    return errHandler(axios.get(url, config));
  },

  post: (url, data, config) => {
    return errHandler(axios.post(url, data, config));
  }
};

export default ApiService;
