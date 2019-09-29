<template>
  <v-container>
    <v-row no-gutters>
      <v-col sm="7">
        <Favorites />
      </v-col>
      <v-col sm="1" />
      <v-col sm="4">
        <AuditLogs />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex';

import AuditLogs from './AuditLogs/index.vue';
import Favorites from './Favorites/index.vue';

export default {
  name: 'Main',
  components: {
    AuditLogs,
    Favorites
  },
  data() {
    return {};
  },
  mounted() {
    this.getAllFavorites();
    this.getAllCategories();
    this.getAllLogs();
  },
  methods: {
    ...mapActions('favorites', [
      'getAllFavorites'
    ]),
    ...mapActions('categories', [
      'getAllCategories'
    ]),
    ...mapActions('auditLogs', [
      'getAllLogs'
    ])
  }
};
</script>
