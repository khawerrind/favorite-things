<template>
  <v-card
    class="fixed-col"
    flat
  >
    <v-app-bar
      color="primary"
      dark
      absolute
      flat
    >
      <v-toolbar-title>Audit Logs</v-toolbar-title>
    </v-app-bar>
    <v-card-text
      class="pa-0 overflow-y-auto"
      style="max-height: 100%"
    >
      <NoResults v-if="!logs.length && !loading" />
      <Loading v-if="loading" />
      <v-list two-line>
        <v-list-item-group>
          <template v-for="(item, index) in logs">
            <AuditLogItem
              :key="index"
              :log="item"
              :index="index"
              :total="logs.length"
            />
          </template>
        </v-list-item-group>
      </v-list>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import Loading from '../Common/Loading.vue';
import NoResults from '../Common/NoResults.vue';
import AuditLogItem from './AuditLogItem.vue';

export default {
  name: 'AuditLogs',
  components: {
    Loading,
    NoResults,
    AuditLogItem
  },
  data() {
    return {};
  },
  computed: {
    ...mapState({
      loading: state => state.auditLogs.loading,
      logs: state => state.auditLogs.logs
    })
  },
  mounted() {
    this.getAllLogs();
  },
  methods: {
    ...mapActions('auditLogs', [
      'getAllLogs'
    ])
  }
};
</script>
