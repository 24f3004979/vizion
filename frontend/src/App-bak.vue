<script setup>
import { onMounted, ref } from 'vue'

const raw = ref(null)
const rows = ref([])
const error = ref(null)

onMounted(async () => {
  try {
    const response = await fetch("http://localhost:8000/editor/data")
    if (!response.ok) throw new Error(`HTTP ${response.status}`)

    const raw_fetch = await response.json()
    let result = raw_fetch.data

    // Backend sent JSON as a string, so parse it into an object
    if (typeof result === 'string') {
      result = JSON.parse(result)
    }

    raw.value = result

    // Column-oriented -> row-oriented
    rows.value = Object.keys(result.id).map(key => ({
      id: result.id[key],
      name: result.name[key],
      city: result.city[key],
    }))

    console.table(rows.value)
  } catch (e) {
    error.value = e.message
    console.error(e)
  }
})
</script>

<template>
  <div>
    <p v-if="error" style="color: red">Error: {{ error }}</p>

    <h3>Cleaned rows</h3>
    <table border="1" cellpadding="6">
      <thead>
        <tr><th>ID</th><th>Name</th><th>City</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in rows" :key="row.id">
          <td>{{ row.id }}</td>
          <td>{{ row.name }}</td>
          <td>{{ row.city }}</td>
        </tr>
      </tbody>
    </table>

    <h3>Raw data</h3>
    <pre>{{ raw }}</pre>
  </div>
</template>
