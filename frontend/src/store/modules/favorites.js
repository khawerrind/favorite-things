/* eslint-disable no-shadow */
import Axios from 'axios';
import { Constants } from '../../utils/constants';

const { API_URL } = Constants;

// initial state
const state = {
  favorites: [],
  loading: true
};

// getters
const getters = {
  getFavorite: state => id => state.favorites.find(item => item.id === id)
};

// actions
const actions = {
  getAllFavorites: async ({ commit }) => {
    const { data } = await Axios.get(`${API_URL}/api/favorites/`);
    commit('setFavorites', data);
  },
  createFavorite: async ({ commit, dispatch }, payload) => {
    const res = await Axios.post(`${API_URL}/api/favorites/`, payload);
    commit('addFavorite', res.data);
    dispatch('getAllFavorites');
    dispatch('auditLogs/getAllLogs', null, { root: true });
  },
  updateFavorite: async ({ commit, dispatch }, payload) => {
    const res = await Axios.put(`${API_URL}/api/favorites/${payload.id}/`, payload);
    commit('updateFavorite', res.data);
    dispatch('getAllFavorites');
    dispatch('auditLogs/getAllLogs', null, { root: true });
  },
  deleteFavorite: async ({ commit, dispatch }, id) => {
    await Axios.delete(`${API_URL}/api/favorites/${id}/`);
    commit('deleteFavorite', id);
    dispatch('auditLogs/getAllLogs', null, { root: true });
  }
};

// mutations
const mutations = {
  setFavorites(state, data) {
    state.favorites = data;
    state.loading = false;
  },
  addFavorite(state, favoriteItem) {
    state.favorites = [favoriteItem, ...state.favorites];
  },
  updateFavorite(state, updatedItem) {
    state.favorites = [
      ...state.favorites.map(item => item.id !== updatedItem.id
        ? item : { ...item, ...updatedItem })
    ];
  },
  deleteFavorite(state, id) {
    state.favorites = [
      ...state.favorites.filter(item => item.id !== id)
    ];
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
