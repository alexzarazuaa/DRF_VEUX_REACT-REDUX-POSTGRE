import axios from "axios";
import { Bar } from '../models/Bars';
import API_URL from './config'
import JwtService from './jwt.service';

const ApiService = {

  // setHeader() {
  //   axios.defaults.headers.common[
  //     "Authorization"
  //   ] = `Token ${JwtService.getToken()}`;
  // },

  // query(resource: string, params: any) {
  //   return axios.get(resource, params).catch((error: any) => {
  //     throw new Error(`[RWV] ApiService ${(error)}`);
  //   });
  // },

  // get(resource: string,) {
  //   //return axios.get('http://0.0.0.0:8001/api/bars/').catch((error: any) => {
  //     return axios.get(`${API_URL}/`).catch((error: any) => {
  //     throw new Error(`[RWV] ApiService ${error}`);
  //   });
  // },

  get(resource: string, slug = "") {
    console.log("GET API SERVICE")
    return axios.get(`${resource}/${slug}`).catch(error => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  // get(resource: string, ) {
  //   fetch('http://0.0.0.0:8001/api/bars/')
  //   .then(res => res.json())
  //   .then(data => {
  //    console.log(data)
  //   })
  //   .catch(rejected => {
  //       console.log(rejected);
  //   });
  // },


  // post(resource: string, params: any) {
  //   return axios.post(`${resource}`, params);
  // },

  // update(resource: string, slug: string, params: any) {
  //   return axios.put(`${resource}/${slug}`, params);
  // },

  // put(resource: string, params: any) {
  //   return axios.put(`${resource}`, params);
  // },

  // delete(resource: string) {
  //   return axios.delete(resource).catch((error: any) => {
  //     throw new Error(`[RWV] ApiService ${error}`);
  //   });
  // }
};

export default ApiService;

export const BarsService = {

  // deleteBar(bar: Bar) {
  //   return axios.delete(`${API_URL}/bar/${bar.slug}`);
  // },
  // getBars() {
  //   console.log('JJA F AXIOS');
  //   //return axios.get(`${API_URL}`);
  //   return axios.get('http://0.0.0.0:8001/api/bars');
  // }



//   getBars() {
//     return ApiService.get('/bars');
// }

getBars() {
  console.log("GET BARS API SERVICE")
  return ApiService.get(`${API_URL}/bars`);
}
  //GET ONE BAR 

  // getBars(slug) {
  //   return axios.get<Bar[]>(`${API_URL}/bar/${bar.slug}`);
  // }
  // addBar(bar: Bar) {
  //   return axios.post(`${API_URL}/bars/`, { bar });
  // },
  // updateBar(bar: Bar) {
  //   return axios.put(`${API_URL}/bars/${bar.slug}`, { bar });
  // }
}
