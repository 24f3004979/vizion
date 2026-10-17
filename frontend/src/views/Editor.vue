<!-- src/views/EditorView.vue -->
<script setup>
import { onMounted } from 'vue'
import { useDataset } from '../composables/useDataset'
import UploadZone from '../components/UploadZone.vue'
import DataTable from '../components/DataTable.vue'

const { columns, error, loadPage } = useDataset()

// If the backend already holds a dataset (e.g. you refreshed the page), show it.
// If not, ignore the "no dataset" error and just show the upload zone.
onMounted(async () => {
  await loadPage(1)
  error.value = null
})
</script>

<template>
  <DataTable v-if="columns.length" />
  <UploadZone v-else />
</template>
