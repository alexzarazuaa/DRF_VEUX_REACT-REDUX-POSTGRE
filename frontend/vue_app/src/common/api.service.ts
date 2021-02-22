import axios from "axios";
import API_URL from "./config";
import JwtService from "./jwt.service";

const ApiService = {
  setHeader() {
    axios.defaults.headers.common[
      "Authorization"
    ] = `Token ${JwtService.getToken()}`;
  },

  query(resource: string, params: any) {
    return axios.get(resource, params).catch((error: any) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  get(resource: string, slug = "") {
    // console.log('entra',resource)
    return axios.get(`${resource}/${slug}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  post(resource: string, params: any) {
    // console.log(resource)
    return axios.post(`${API_URL}/${resource}`, params);
  },

  update(resource: string, slug: string, params: any) {
    return axios.put(`${resource}/${slug}`, params);
  },

  delete(resource: string) {
    //console.log(resource, "delete bar");
    return axios.delete(`${API_URL}/${resource}`).catch((error: any) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
};

export default ApiService;

export const UserService = {
  getUser(resource: string, slug = "") {
    // console.log('entra',resource)
    return axios.get(`${API_URL}/${resource}/${slug}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
}

export const ProfileService = {
  
  getProfile(resource: string, params: any) {
    //console.log("entra profile", resource);
    return axios.get(`${API_URL}/${resource}${params}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

}

export const PaginationSerice = {
  getPag(resource: string, params: any) {
    // console.log('entra',resource)
    return axios.get(`${API_URL}/${resource}?${params}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
}

export const BarsService = {
  getBars() {
    //GET ALLS
    return ApiService.get(`${API_URL}/bars`);
  },

  getBar(slug: string) {
    //GET ONE BAR
    return ApiService.get(`${API_URL}/bars/${slug}`);
  },

  addBarFavorite(slug: string) {
    //FAVORITE BAR
    return ApiService.post(`bars/${slug}/favorite`, "");
  },
  removeBarFavorite(slug: string) {
    // UNFAVORITE BAR
    return ApiService.delete(`bars/${slug}/favorite`);
  },
};
