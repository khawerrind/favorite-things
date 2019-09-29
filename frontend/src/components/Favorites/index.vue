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
      <v-toolbar-title>Favorite Things</v-toolbar-title>
      <div class="flex-grow-1" />
      <v-btn
        color="success"
        dark
        class="mb-2"
        @click="showCreateUpdateModal = true"
      >
        <v-icon dark>
          mdi-plus
        </v-icon> Add Favorite
      </v-btn>
    </v-app-bar>
    <v-card-text
      class="pa-0 overflow-y-auto"
      style="max-height: 100%"
    >
      <NoResults v-if="!favorites.length && !loading" />
      <Loading v-if="loading" />
      <template v-for="item in favorites">
        <v-col
          :key="item.id"
          cols="12"
        >
          <FavoriteItem
            :favorite="item"
            :on-edit="handleEdit"
            :on-delete="handleDelete"
          />
        </v-col>
      </template>
    </v-card-text>
    <CreateUpdateModal
      :edited-id="editedId"
      :visible="showCreateUpdateModal"
      @close="handleCreateUpdateModalClose"
    />
    <ConfirmDialog
      :on-confirm="handleConfirm"
      :visible="showConfirmModal"
      @close="showConfirmModal=false"
    />
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import Loading from '../Common/Loading.vue';
import NoResults from '../Common/NoResults.vue';
import FavoriteItem from './FavoriteItem.vue';
import CreateUpdateModal from '../Modals/CreateUpdateModal.vue';
import ConfirmDialog from '../Modals/ConfirmDialog.vue';

export default {
  name: 'Favorites',
  components: {
    Loading,
    NoResults,
    FavoriteItem,
    CreateUpdateModal,
    ConfirmDialog
  },
  data() {
    return {
      showCreateUpdateModal: false,
      showConfirmModal: false,
      editedId: 0,
      deletedId: 0
    };
  },
  computed: {
    ...mapState({
      favorites: state => state.favorites.favorites,
      loading: state => state.favorites.loading
    })
  },
  mounted() {
    this.getAllFavorites();
  },
  methods: {
    ...mapActions('favorites', [
      'getAllFavorites',
      'deleteFavorite'
    ]),
    handleEdit(id) {
      this.editedId = id;
      this.showCreateUpdateModal = true;
    },
    handleDelete(id) {
      this.deletedId = id;
      this.showConfirmModal = true;
    },
    handleConfirm() {
      if (this.deletedId) {
        this.deleteFavorite(this.deletedId);
        this.deletedId = 0;
        this.showConfirmModal = false;
      }
    },
    handleCreateUpdateModalClose() {
      this.showCreateUpdateModal = false;
      this.editedId = 0;
    }
  }
};
</script>
