// src/composables/useDataset.js
import { ref } from 'vue'

const API = 'http://localhost:8000/editor'

// declared outside the function so every component shares the same data
const columns = ref([])
const rows = ref([])
const meta = ref({ page: 1, page_size: 50, total_rows: 0, total_pages: 1, offset: 0,
                   can_undo: false, can_redo: false })
const loading = ref(false)
const error = ref(null)

async function call(path, options) {
  const res = await fetch(`${API}${path}`, options)
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new Error(body.detail || `Server error ${res.status}`)
  }
  return res.json()
}

function apply(data) {
  columns.value = data.columns
  rows.value = data.rows
  meta.value = data
}

export function useDataset() {
  async function loadPage(page = meta.value.page) {
    loading.value = true
    error.value = null
    try {
      apply(await call(`/data?page=${page}&page_size=${meta.value.page_size}`))
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  async function upload(file) {
    const form = new FormData()
    form.append('file', file)
    loading.value = true
    error.value = null
    try {
      apply(await call('/upload', { method: 'POST', body: form }))
    } catch (e) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  // After any change we re-fetch the current page, so the screen always matches the backend
  async function editCell(rowOnPage, column, value) {
    try {
      await call('/cell', {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ row: meta.value.offset + rowOnPage, column, value }),
      })
      error.value = null
      await loadPage()
    } catch (e) {
      error.value = e.message
    }
  }

  async function undo() { await call('/undo', { method: 'POST' }); await loadPage() }
  async function redo() { await call('/redo', { method: 'POST' }); await loadPage() }

  return { columns, rows, meta, loading, error, loadPage, upload, editCell, undo, redo }
}
