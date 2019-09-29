<template>
  <v-dialog
    v-model="show"
    scrollable
    max-width="600px"
  >
    <v-card>
      <v-card-title>
        <span class="headline">{{ formTitle }}</span>
      </v-card-title>

      <v-card-text ref="createUpdateModal">
        <v-container>
          <v-row>
            <v-text-field
              v-model.trim="editedItem.title"
              label="Title"
              :error-messages="titleErrors"
              class="required"
              counter
              maxlength="60"
              @input="$v.editedItem.title.$touch()"
              @blur="$v.editedItem.title.$touch()"
            />
          </v-row>
          <v-row>
            <v-select
              v-model="editedItem.category"
              :items="categories"
              label="Category"
              item-value="id"
              item-text="name"
              :error-messages="categoryErrors"
              class="required"
              @change="$v.editedItem.category.$touch()"
            />
            <v-layout align-center>
              <v-btn
                class="mx-2"
                fab
                dark
                x-small
                color="success"
                @click="showCategoryDialog = true"
              >
                <v-icon dark>
                  mdi-plus
                </v-icon>
              </v-btn>
            </v-layout>
          </v-row>
          <v-row>
            <v-text-field
              v-model.trim="editedItem.rank"
              type="number"
              label="Rank"
              :error-messages="rankErrors"
              class="required"
              @input="$v.editedItem.rank.$touch()"
              @blur="$v.editedItem.rank.$touch()"
            />
          </v-row>
          <v-row>
            <v-textarea
              v-model.trim="editedItem.description"
              name="input-7-4"
              label="Description"
              counter
              maxlength="500"
              :error-messages="descriptionErrors"
              @input="$v.editedItem.description.$touch()"
              @blur="$v.editedItem.description.$touch()"
            />
          </v-row>
          <v-row v-if="!editedItem.metadata.length">
            <v-btn
              class="my-2"
              color="success"
              @click="addMetaRow"
            >
              <v-icon dark>
                mdi-plus
              </v-icon>
              Add key/value pair
            </v-btn>
          </v-row>
          <v-row
            v-for="(meta, index) in editedItem.metadata"
            :key="index"
          >
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="3"
              >
                <v-text-field
                  v-model.trim="meta.key_name"
                  label="Key name"
                />
              </v-col>
              <v-col
                v-if="meta.key_type !== 'date'"
                cols="12"
                sm="6"
                md="3"
              >
                <v-text-field
                  v-model.trim="meta.key_value"
                  :type="meta.key_type"
                  label="Key value"
                />
              </v-col>
              <v-col
                v-if="meta.key_type === 'date'"
                cols="12"
                sm="6"
                md="3"
              >
                <v-menu
                  v-model="dateMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="290px"
                >
                  <template v-slot:activator="{ on }">
                    <v-text-field
                      v-model="meta.key_value"
                      label="Key value"
                      readonly
                      v-on="on"
                    />
                  </template>
                  <v-date-picker
                    v-model="meta.key_value"
                    @input="dateMenu = false"
                  />
                </v-menu>
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="3"
              >
                <v-select
                  v-model="meta.key_type"
                  :items="metaTypes"
                  label="Type"
                  item-value="id"
                  item-text="name"
                  @change="meta.key_value = ''"
                />
              </v-col>
              <v-col
                cols="12"
                sm="6"
                md="3"
                class="text-center"
              >
                <v-container fill-height>
                  <v-layout align-center>
                    <v-btn
                      class="mx-2"
                      fab
                      dark
                      x-small
                      color="error"
                      @click="removeMetaRow(index)"
                    >
                      <v-icon dark>
                        mdi-minus
                      </v-icon>
                    </v-btn>
                    <v-btn
                      v-if="(index + 1) === editedItem.metadata.length"
                      class="mx-2"
                      fab
                      dark
                      x-small
                      color="success"
                      @click="addMetaRow"
                    >
                      <v-icon dark>
                        mdi-plus
                      </v-icon>
                    </v-btn>
                  </v-layout>
                </v-container>
              </v-col>
            </v-row>
          </v-row>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <div class="flex-grow-1" />
        <v-btn
          color="blue darken-1"
          text
          @click="show=false"
        >
          Cancel
        </v-btn>
        <v-btn
          color="blue darken-1"
          text
          @click="save"
        >
          Save
        </v-btn>
      </v-card-actions>
      <CategoryDialog
        :visible="showCategoryDialog"
        @close="showCategoryDialog=false"
      />
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex';
import {
  required,
  numeric,
  minLength,
  maxLength,
  minValue,
  maxValue
} from 'vuelidate/lib/validators';
import formMixin from '../../mixins/form';
import { Constants } from '../../utils/constants';
import CategoryDialog from './CategoryDialog.vue';

const metaDataRow = {
  key_name: '',
  key_value: '',
  key_type: 'text'
};

const defaultItem = {
  id: '',
  title: '',
  description: '',
  category: 1,
  rank: 1,
  metadata: []
};

export default {
  name: 'CreateUpdateModal',
  components: {
    CategoryDialog
  },
  mixins: [formMixin],
  props: {
    visible: {
      type: Boolean,
      required: true,
      default: false
    },
    editedId: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      dateMenu: false,
      showCategoryDialog: false,
      metaTypes: Constants.META_TYPES,
      editedItem: { ...defaultItem }
    };
  },
  validations: {
    editedItem: {
      title: {
        required,
        minLength: minLength(3),
        maxLength: maxLength(60)
      },
      category: {
        required
      },
      rank: {
        required,
        numeric,
        minValue: minValue(1),
        maxValue: maxValue(5000)
      },
      description: {
        minLength: minLength(10),
        maxLength: maxLength(500)
      }
    }
  },
  computed: {
    ...mapState({
      categories: state => state.categories.categories
    }),
    ...mapGetters('favorites', [
      'getFavorite'
    ]),
    show: {
      get() {
        return this.visible;
      },
      set(value) {
        if (!value) {
          this.$emit('close');
        }
      }
    },
    formTitle() {
      return this.editedItem.id ? 'Update' : 'New Favorite Thing';
    },
    titleErrors() {
      const errors = [];
      if (!this.$v.editedItem.title.$dirty) return errors;
      if (!this.$v.editedItem.title.required) errors.push('Title is required.');
      if (!this.$v.editedItem.title.minLength) errors.push(`Title must have at least ${this.$v.editedItem.title.$params.minLength.min} letters.`);
      if (!this.$v.editedItem.title.maxLength) errors.push(`Title cannot be greater than ${this.$v.editedItem.title.$params.maxLength.max} letters.`);
      return errors;
    },
    categoryErrors() {
      const errors = [];
      if (!this.$v.editedItem.category.$dirty) return errors;
      if (!this.$v.editedItem.category.required) errors.push('Category is required.');
      return errors;
    },
    rankErrors() {
      const errors = [];
      if (!this.$v.editedItem.rank.$dirty) return errors;
      if (!this.$v.editedItem.rank.required) errors.push('Rank is required.');
      if (!this.$v.editedItem.rank.numeric) errors.push('Rank should be of numeric value.');
      if (!this.$v.editedItem.rank.minValue) errors.push(`Rank cannot be less than ${this.$v.editedItem.rank.$params.minValue.min}.`);
      if (!this.$v.editedItem.rank.maxValue) errors.push(`Rank cannot be greater than ${this.$v.editedItem.rank.$params.maxValue.max}.`);
      return errors;
    },
    descriptionErrors() {
      const errors = [];
      if (!this.$v.editedItem.description.$dirty) return errors;
      if (!this.$v.editedItem.description.minLength) errors.push(`Description must have at least ${this.$v.editedItem.description.$params.minLength.min} letters.`);
      if (!this.$v.editedItem.description.maxLength) errors.push(`Description cannot be greater than ${this.$v.editedItem.description.$params.maxLength.max} letters.`);
      return errors;
    }
  },
  watch: {
    editedItem(currVal, prevVal) {
      if (currVal && prevVal && currVal.metadata.length > prevVal.metadata.length) {
        this.scrollToBottom();
      }
    },
    show(currVal, prevVal) {
      if (!currVal && prevVal) {
        this.editedItem = { ...defaultItem };
        this.$v.$reset();
      }
      if (currVal && !prevVal) {
        this.scrollToTop();
        if (this.editedId) {
          const item = this.getFavorite(this.editedId) || {};
          this.editedItem = { ...this.editedItem, ...item };
        }
      }
    }
  },
  methods: {
    ...mapActions('favorites', [
      'createFavorite',
      'updateFavorite'
    ]),
    save() {
      this.$v.editedItem.$touch();
      if (this.$v.editedItem.$invalid) {
        this.scrollToTop();
        return;
      }

      let payload = { ...this.editedItem };
      payload = {
        ...payload,
        metadata: payload.metadata.reduce(this.validateMetadata, [])
      };

      if (this.editedItem.id) {
        this.updateFavorite(payload);
      } else {
        this.createFavorite(payload);
      }

      this.show = false;
    },
    validateMetadata(filtered, item) {
      if (item.key_type === 'number'
        && item.key_name.trim().length
        && parseInt(item.key_value, 10) > 0) {
        const option = {
          ...item,
          key_value: parseInt(item.key_value, 10)
        };
        filtered.push(option);
      } else if (item.key_type !== 'number'
        && item.key_name.trim().length
        && item.key_value.trim().length) {
        filtered.push(item);
      }
      return filtered;
    },
    addMetaRow() {
      this.editedItem = {
        ...this.editedItem,
        metadata: [...this.editedItem.metadata, { ...metaDataRow }]
      };
    },
    removeMetaRow(metaIndex) {
      this.editedItem = {
        ...this.editedItem,
        metadata: this.editedItem.metadata.filter((item, index) => index !== metaIndex)
      };
    },
    scrollToBottom() {
      this.$nextTick(() => {
        this.$refs.createUpdateModal.scrollTop = this.$refs.createUpdateModal.scrollHeight;
      });
    },
    scrollToTop() {
      this.$nextTick(() => {
        this.$refs.createUpdateModal.scrollTop = 0;
      });
    }
  }
};
</script>
