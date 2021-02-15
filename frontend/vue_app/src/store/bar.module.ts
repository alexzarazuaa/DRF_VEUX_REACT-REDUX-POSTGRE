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
  }
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