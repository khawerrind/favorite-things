<template>
  <v-dialog
    v-model="show"
    max-width="500px"
  >
    <v-card>
      <v-card-title>
        New Category
      </v-card-title>
      <v-card-text>
        <v-text-field
          v-model.trim="categoryName"
          label="Category name"
          :error-messages="categoryNameErrors"
          required
          counter
          maxlength="10"
          @input="$v.categoryName.$touch()"
          @blur="$v.categoryName.$touch()"
        />
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
    </v-card>
  </v-dialog>
</template>

<script>
import { mapActions } from 'vuex';
import {
  required,
  minLength,
  maxLength
} from 'vuelidate/lib/validators';
import formMixin from '../../mixins/form';

export default {
  name: 'CategoryDialog',
  mixins: [formMixin],
  props: {
    visible: {
      type: Boolean,
      required: true,
      default: false
    }
  },
  data() {
    return {
      categoryName: ''
    };
  },
  validations: {
    categoryName: {
      required,
      minLength: minLength(3),
      maxLength: maxLength(10)
    }
  },
  computed: {
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
    categoryNameErrors() {
      const errors = [];
      if (!this.$v.categoryName.$dirty) return errors;
      if (!this.$v.categoryName.required) errors.push('Category name is required.');
      if (!this.$v.categoryName.minLength) errors.push(`Category name must have at least ${this.$v.categoryName.$params.minLength.min} letters.`);
      if (!this.$v.categoryName.maxLength) errors.push(`Category name cannot be greater than ${this.$v.categoryName.$params.maxLength.max} letters.`);
      return errors;
    }
  },
  watch: {
    show(currVal, prevVal) {
      if (!currVal && prevVal) {
        this.categoryName = '';
        this.$v.$reset();
      }
    }
  },
  methods: {
    ...mapActions('categories', [
      'createCategory'
    ]),
    save() {
      this.$v.categoryName.$touch();
      if (this.$v.categoryName.$invalid) {
        return;
      }

      const payload = {
        name: this.categoryName
      };
      this.createCategory(payload);

      this.show = false;
    }
  }
};
</script>
