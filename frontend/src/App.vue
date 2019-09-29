<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Favorite</span>
        <span class="font-weight-light">THINGS</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-content>
      <Main />
    </v-content>
  </v-app>
</template>

<script>
import Main from './components/Main.vue';

export default {
  name: 'App',
  components: {
    Main
  },
  data: () => ({})
};
</script>
<style>
  @import './assets/css/custom.css';
</style>
