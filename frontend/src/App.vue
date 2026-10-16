<script setup lang="ts">

import { ref, onMounted } from 'vue';

const data = ref("");

onMounted(async () => {
  const response = await fetch("http://localhost:8000/editor/data");
  const result = await response.json();
  data.value = result.data;
})

</script>

<template>
  <h1> Data Set fetch </h1>
  Data : {{ data }}

</template>

<style scoped></style>
