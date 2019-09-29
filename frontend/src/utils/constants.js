import keyMirror from 'keymirror';

// Actions
export const Actions = keyMirror({
  GET_FAVORITES: null,
  CREATE_FAVORITES: null,
  GET_CATEGORIES: null
});

// Mutations
export const Mutations = keyMirror({
  SET_FAVORITES: null,
  SET_CATEGORIES: null
});

// Getters
export const Getters = keyMirror({
  FAVORITES: null,
  CATEGORIES: null
});

export const Constants = {
  API_URL: process.env.VUE_APP_API_URL || 'http://localhost:8000',
  META_TYPES: [
    { id: 'text', name: 'Text' },
    { id: 'number', name: 'Number' },
    { id: 'date', name: 'Date' }
  ]
};
