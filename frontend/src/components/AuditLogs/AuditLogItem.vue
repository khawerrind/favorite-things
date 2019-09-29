<template>
  <div>
    <v-list-item disabled>
      <template>
        <v-list-item-content>
          <v-list-item-title v-text="'Title: ' + log.title" />
          <v-list-item-subtitle v-text="heading" />
        </v-list-item-content>

        <v-list-item-action>
          <v-list-item-action-text>{{ log.date_created | formatDate }}</v-list-item-action-text>
          <v-icon
            :color="color"
            v-text="icon"
          />
        </v-list-item-action>
      </template>
    </v-list-item>

    <v-divider
      v-if="index + 1 < total"
      :key="index"
    />
  </div>
</template>

<script>
export default {
  name: 'AuditLogItem',
  props: {
    log: {
      type: Object,
      required: true
    },
    index: {
      type: Number,
      required: true
    },
    total: {
      type: Number,
      required: true
    }
  },
  computed: {
    icon() {
      if (this.log.action === 'updated') return 'mdi-pencil-circle';
      if (this.log.action === 'deleted') return 'mdi-delete-circle';
      return 'mdi-check-circle';
    },
    color() {
      if (this.log.action === 'updated') return 'orange';
      if (this.log.action === 'deleted') return 'red';
      return 'teal';
    },
    heading() {
      if (this.log.action === 'updated') return 'You updated a favorite thing';
      if (this.log.action === 'deleted') return 'You delete a favorite thing';
      return 'You created a new favorite thing';
    }
  }
};
</script>
