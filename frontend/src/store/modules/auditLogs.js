/* eslint-disable no-shadow */
import Axios from 'axios';
import { Constants } from '../../utils/constants';

const { API_URL } = Constants;

// initial state
const state = {
  logs: [],
  loading: true
};

// getters
const getters = {};

// actions
const actions = {
  getAllLogs: async ({ commit }) => {
    const { data } = await Axios.get(`${API_URL}/api/audit/`);
    commit('setLogs', data);
  }
};

// mutations
const mutations = {
  setLogs(state, data) {
    state.logs = data;
    state.loading = false;
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
