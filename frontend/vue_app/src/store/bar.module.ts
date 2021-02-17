import { BarsService } from "@/common/api.service";
import { ActionsType } from "./actions.type";
import { MutationsType } from "./mutations.type";


export interface State {
  Bar: any;
}

export const InitialState: State = {
  Bar: {
    name: "",
    description: "",
    owner: "",
  }
};


export const actions = {
  async [ActionsType.FETCH_BAR](context: any, barSlug: any) {
    // avoid extronuous network call if article exists
    const { data } = await BarsService.getBar(barSlug);
    context.commit(MutationsType.SET_BAR, data);
    return data;
  },
  async [ActionsType.FAVORITE_ADD](context: any, barSlug: any) {
    console.log('lo hara favorito')
    const { data } = await BarsService.addBarFavorite(barSlug);
    console.log(data)
    //ontext.commit(MutationsType.UPDATE_BAR_IN_LIST, data, { root: true });
     context.commit(MutationsType.SET_BAR, data);
  },
  async [ActionsType.FAVORITE_REMOVE](context: any, barSlug: any) {
    console.log('entra borra fav')
    const { data } = await BarsService.removeBarFavorite(barSlug);
     console.log(data)
    // Update list as well. This allows us to favorite an article in the Home view.
    context.commit(MutationsType.SET_BAR, data);
  },

};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [MutationsType.SET_BAR](state: State, bar: any) {
    state.Bar = bar;
  }
};

const getters = {
  bar(state: State) {
    return state.Bar;
  }
};

export default {
  InitialState,
  actions,
  mutations,
  getters
};