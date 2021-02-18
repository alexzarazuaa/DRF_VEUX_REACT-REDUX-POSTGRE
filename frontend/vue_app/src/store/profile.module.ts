import ApiService from "@/common/api.service";
import { ActionsType } from "./actions.type";
import { MutationsType } from "./mutations.type";

const state = {
  errors: {},
  profile: {}
};

const getters = {
  profile(state: any) {
    return state.profile;
  }
};

const actions = {
  [ActionsType.FETCH_PROFILE](context: any, payload: any) {
    const { username } = payload;
    return ApiService.get("profils", username)
      .then(({ data }) => {
        context.commit(MutationsType.SET_PROFILE, data.profile);
        return data;
      })
      .catch((response) => {
        // #todo SET_ERROR cannot work in multiple states
        context.commit(MutationsType.SET_ERROR, response.data.errors)
      });
  }
  
//   ,
//   [ActionsType.FETCH_PROFILE_FOLLOW](context : any, payload : any) {
//     const { username } = payload;
//     return ApiService.post(`profiles/${username}/follow`)
//       .then(({ data }) => {
//         context.commit(MutationsType.SET_PROFILE, data.profile);
//         return data;
//       })
//       .catch((response) => {
//         // #todo SET_ERROR cannot work in multiple states
//         context.commit(MutationsType.SET_ERROR, response.data.errors)
//       });
//   },
//   [ActionsType.FETCH_PROFILE_UNFOLLOW](context : any , payload :  any) {
//     const { username } = payload;
//     return ApiService.delete(`profiles/${username}/follow`)
//       .then(({ data }) => {
//         context.commit(MutationsType.SET_PROFILE, data.profile);
//         return data;
//       })
//       .catch((response) => {
//         // #todo SET_ERROR cannot work in multiple states
//         context.commit(MutationsType.SET_ERROR, response.data.errors)
//       });;
//   }
};

const mutations = {
  [MutationsType.SET_ERROR] (state: any, error: any) {
    state.errors = error
  },
  [MutationsType.SET_PROFILE](state: any, profile:  any) {
    state.profile = profile;
    state.errors = {};
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
