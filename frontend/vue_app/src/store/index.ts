import { createStore } from 'vuex'

import auth from "./auth.module";
import bars from "./bars.module";
import bar from "./bar.module";

export default createStore({
  modules: {
    auth,
    bars,
    bar
  }
})