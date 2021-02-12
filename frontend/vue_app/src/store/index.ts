import { createStore } from 'vuex'

import auth from "./auth.module";
//import home from

export default createStore({
  modules: {
    auth
  }
})