<template>
  <v-row
    class="fill-height"
    align-content="center"
    justify="center"
  >
    <v-col
      class="subtitle-1 text-center"
      cols="12"
    >
      Loading
    </v-col>
    <v-col cols="6">
      <v-progress-linear
        color="blue dark"
        indeterminate
        rounded
        height="6"
      />
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'Loading'
};
</script>
