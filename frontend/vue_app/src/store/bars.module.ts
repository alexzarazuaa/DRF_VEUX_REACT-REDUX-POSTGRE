import { BarsService } from "@/common/api.service";
import { ActionsType } from "./actions.type";
import { MutationsType } from "./mutations.type";

export interface State {
  Bars: any[];
  IsLoading: boolean;
  BarsCount: number;
}

export const initialState: State = {
  Bars: [],
  IsLoading: false,
  BarsCount: 0
}

const getters = {
  barsCount: (initialState: any) => {
    return initialState.BarsCount;
  },
  bars: (initialState: any) => {
    return initialState.Bars;
  },
  isLoading: (initialState: any) => {
    return initialState.IsLoading;
  }
};



const actions = {
  [ActionsType.FETCH_BARS]({ commit }: any, params: any ) {
    commit(MutationsType.FETCH_START);
    return BarsService.getBars()
      .then(({ data }: any) => {
        console.log(data)
        commit(MutationsType.FETCH_END, data);
      })
      .catch((error: any) => {
        throw new Error(error);
      });
  }
};

/* eslint no-param-reassign: ["error", { "props": false }] */
const mutations = {
  [MutationsType.FETCH_START](state: any) {
    state.IsLoading = true;
  },
  [MutationsType.FETCH_END](state: any, { bars, barsCount }: any) {
    state.Bars = bars;
    state.BarsCount = barsCount;
    state.isLoading = false;
  },
  [MutationsType.UPDATE_BAR_IN_LIST](state: any, data: any) {
    state.Bars = state.Bars.map((bar: any) => {
      if (bar.slug !== data.slug) {
        return bar;
      }
      // article.favorited = data.favorited;
      // article.favoritesCount = data.favoritesCount;
      return bar;
    });
  }
};

export default {
  initialState,
  getters,
  actions,
  mutations
};