<template>
  <v-row justify="center">
    <v-dialog
      v-model="show"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">
          {{ title }}
        </v-card-title>
        <v-card-text>
          {{ message }}
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1" />
          <v-btn
            color="green darken-1"
            text
            @click="show = false"
          >
            {{ cancelText }}
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="onConfirm"
          >
            {{ confirmText }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: 'ConfirmDialog',
  props: {
    visible: {
      type: Boolean,
      required: true
    },
    onConfirm: {
      type: Function,
      required: true
    },
    title: {
      type: String,
      default: 'Confirm'
    },
    message: {
      type: String,
      default: 'Are you sure you want to perform this action?'
    },
    cancelText: {
      type: String,
      default: 'Cancel'
    },
    confirmText: {
      type: String,
      default: 'Confirm'
    }
  },
  data() {
    return {};
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
    }
  }
};
</script>
