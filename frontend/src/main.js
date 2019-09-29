import Vue from 'vue';
import moment from 'moment';

import App from './App.vue';
import vuetify from './plugins/vuetify';

import store from './store';

Vue.config.productionTip = false;

Vue.filter('formatDate', value => value ? moment(String(value)).format('ddd, MMM DD, YYYY') : '');

new Vue({
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app');
