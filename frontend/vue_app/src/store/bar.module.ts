import { BarsService } from "@/common/api.service";
import { ActionsType } from "./actions.type";
import barsModule from "./bars.module";
import { MutationsType } from "./mutations.type";

export interface State {
  Bar: any;
}

export const InitialState: State = {
  Bar : {}
};

export const actions = {

  async [ActionsType.FETCH_BAR](context: any, barSlug: any) {
    const { data } = await BarsService.getBar(barSlug);
    context.commit(MutationsType.SET_BAR, data);
    return data;
  },
  async [ActionsType.FAVORITE_ADD](context: any, barSlug: any) {
    //console.log("lo hara favorito");
    const { data } = await BarsService.addBarFavorite(barSlug);
    //console.log(data);
    context.commit(MutationsType.SET_BAR, data.bar);
  },
  async [ActionsType.FAVORITE_REMOVE](context: any, barSlug: any) {
    //console.log("entra borra fav");
    const { data } = await BarsService.removeBarFavorite(barSlug);
    //console.log(data);
    context.commit(MutationsType.SET_BAR, data.bar);
  },


  async [ActionsType.BOOK_ADD](context: any, barSlug: any) {
    console.log("RESERVA",barSlug);
    const { data } = await BarsService.postBook(barSlug);
    // console.log(data);
    context.commit(MutationsType.SET_BAR, data.bar);
  },
  async [ActionsType.BOOK_REMOVE](context: any, barSlug: any) {
    console.log(" borra RESERVA" , barSlug);
    const { data } = await BarsService.deleteBook(barSlug);
    //console.log(data);
    context.commit(MutationsType.SET_BAR, data.bar);
  },


};

export const mutations = {
  [MutationsType.SET_BAR](state: State, bar: any) {
    state.Bar = bar;
  },
};

const getters = {
  bar(state: State) {
    return state.Bar;
  },
};

export default {
  InitialState,
  actions,
  mutations,
  getters,
};
