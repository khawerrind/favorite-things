<template>
  <v-card
    class="mt-2"
    elevation="1"
  >
    <v-card-title class="pl-2 pt-1 pr-2">
      <v-row no-gutters>
        {{ favorite.title }}
      </v-row>
      <span class="grey--text subtitle-1">{{ favorite.date_created | formatDate }}</span>
    </v-card-title>

    <v-card-actions>
      <div class="flex-grow-1" />

      <v-btn
        fab
        x-small
        icon
        @click="onEdit(favorite.id)"
      >
        <v-icon>edit</v-icon>
      </v-btn>

      <v-btn
        fab
        x-small
        icon
        @click="onDelete(favorite.id)"
      >
        <v-icon>delete</v-icon>
      </v-btn>

      <v-btn
        fab
        x-small
        icon
        @click="show = !show"
      >
        <v-icon class="up-down">
          {{ show ? 'keyboard_arrow_up' : 'keyboard_arrow_down' }}
        </v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-card-title class="subtitle-2">
          Category
        </v-card-title>
        <v-card-text>
          {{ favorite.category_name }}
        </v-card-text>

        <v-card-title class="subtitle-2">
          Rank
        </v-card-title>
        <v-card-text>
          {{ favorite.rank }}
        </v-card-text>

        <v-card-title class="subtitle-2">
          Description
        </v-card-title>
        <v-card-text>
          {{ favorite.description || 'N/A' }}
        </v-card-text>

        <v-card-title class="subtitle-2">
          Metadata
        </v-card-title>
        <v-card-text class="metadata">
          <ul v-if="favorite.metadata.length">
            <li
              v-for="item in favorite.metadata"
              :key="item.key_name"
            >
              {{ item.key_name }}: {{ item.key_value }}
            </li>
          </ul>
          <span v-if="!favorite.metadata.length">N/A</span>
        </v-card-text>

        <v-card-title class="subtitle-2">
          Last Modified At
        </v-card-title>
        <v-card-text>
          {{ favorite.date_modified | formatDate }}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: 'FavoriteItem',
  props: {
    favorite: {
      type: Object,
      required: true
    },
    onEdit: {
      type: Function,
      required: true
    },
    onDelete: {
      type: Function,
      required: true
    }
  },
  data() {
    return {
      show: false
    };
  }
};
</script>

<style scoped>
.metadata ul {
	list-style-type: none;
	padding: 0;
}
.metadata ul li {
	display: block;
}
.up-down {
  font-size: 28px;
}
</style>
