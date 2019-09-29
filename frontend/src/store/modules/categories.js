/* eslint-disable no-shadow */
import Axios from 'axios';
import { Constants } from '../../utils/constants';

const { API_URL } = Constants;

// initial state
const state = {
  categories: [],
  loading: true,
  errored: false
};

// getters
const getters = {};

// actions
const actions = {
  getAllCategories: async ({ commit }) => {
    const { data } = await Axios.get(`${API_URL}/api/categories/`);
    commit('setCategories', data);
  },
  createCategory: async ({ commit }, payload) => {
    const res = await Axios.post(`${API_URL}/api/categories/`, payload);
    commit('createCategory', res.data);
  }
};

// mutations
const mutations = {
  setCategories(state, data) {
    state.categories = data;
  },
  createCategory(state, data) {
    state.categories = [...state.categories, data];
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
