<!-- src/components/UploadZone.vue -->
<script setup>
import { ref } from 'vue'
import { useDataset } from '../composables/useDataset'

const { upload, loading, error } = useDataset()
const dragging = ref(false)

function onDrop(e) {
  dragging.value = false
  const file = e.dataTransfer.files[0]
  if (file) upload(file)
}

function onPick(e) {
  const file = e.target.files[0]
  if (file) upload(file)
  e.target.value = ''   // lets you pick the same file again later
}
</script>

<template>
  <div class="mx-auto max-w-xl space-y-4 px-6 pt-40">
    <label
      @dragover.prevent="dragging = true"
      @dragleave="dragging = false"
      @drop.prevent="onDrop"
      :class="dragging ? 'border-blue-500 bg-blue-50' : 'border-slate-300 bg-white'"
      class="flex h-56 cursor-pointer flex-col items-center justify-center gap-2
             rounded-3xl border-2 border-dashed transition duration-300 hover:border-blue-400">
      <span class="text-xl font-semibold text-slate-700">
        {{ loading ? 'Uploading…' : 'Drop your CSV here' }}
      </span>
      <span class="text-sm text-slate-500">or click to browse</span>
      <input type="file" accept=".csv" class="hidden" @change="onPick" />
    </label>

    <p v-if="error" class="rounded-xl bg-red-50 p-3 text-center text-red-600">{{ error }}</p>
  </div>
</template>
