import { createStore } from 'vuex'

import auth from "./auth.module";
import bars from "./bars.module";
import bar from "./bar.module";
import profile from "./profile.module";

export default createStore({
  modules: {
    auth,
    bars,
    bar,
    profile
  }
})