import Vue from 'vue';
import Vuex from 'vuex';
import favorites from './modules/favorites';
import categories from './modules/categories';
import auditLogs from './modules/auditLogs';

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  modules: {
    favorites,
    categories,
    auditLogs
  },
  strict: debug
});
