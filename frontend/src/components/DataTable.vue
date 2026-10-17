<!-- src/components/DataTable.vue -->
<script setup>
import { ref, onMounted } from 'vue'
import { useDataset } from '../composables/useDataset'

const { columns, rows, meta, loading, error, loadPage, editCell, undo, redo } = useDataset()

const editing = ref(null)   // { r: rowIndexOnPage, c: columnName }
const draft = ref('')

onMounted(() => loadPage(1))

function startEdit(r, c, current) {
  editing.value = { r, c }
  draft.value = current ?? ''
}

async function commit() {
  if (!editing.value) return
  const { r, c } = editing.value
  editing.value = null
  await editCell(r, c, draft.value)
}
</script>

<template>
  <div class="mx-auto max-w-6xl px-6 pt-28 pb-12">

    <!-- toolbar -->
    <div class="mb-4 flex items-center justify-between">
      <p class="text-slate-600">
        {{ meta.total_rows }} rows · {{ columns.length }} columns
      </p>
      <div class="flex gap-2">
        <button @click="undo" :disabled="!meta.can_undo"
                class="rounded-full bg-blue-100 px-4 py-2 text-sm font-semibold text-blue-700
                       transition hover:bg-blue-200 disabled:opacity-40">Undo</button>
        <button @click="redo" :disabled="!meta.can_redo"
                class="rounded-full bg-blue-100 px-4 py-2 text-sm font-semibold text-blue-700
                       transition hover:bg-blue-200 disabled:opacity-40">Redo</button>
      </div>
    </div>

    <p v-if="error" class="mb-4 rounded-xl bg-red-50 p-3 text-red-600">{{ error }}</p>

    <!-- table -->
    <div class="overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow"
         :class="{ 'opacity-60': loading }">
      <table class="w-full text-left text-sm">
        <thead class="bg-slate-100 text-slate-600">
          <tr>
            <th class="px-3 py-3 text-slate-400">#</th>
            <th v-for="col in columns" :key="col.name" class="px-4 py-3 font-semibold">
              {{ col.name }}
              <span class="ml-1 text-xs font-normal text-slate-400">{{ col.dtype }}</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, r) in rows" :key="meta.offset + r"
              class="border-t border-slate-100 hover:bg-blue-50">
            <td class="px-3 py-2 text-slate-400">{{ meta.offset + r + 1 }}</td>

            <td v-for="col in columns" :key="col.name"
                @dblclick="startEdit(r, col.name, row[col.name])"
                class="px-4 py-2">
              <input
                v-if="editing && editing.r === r && editing.c === col.name"
                v-model="draft"
                @keyup.enter="commit"
                @keyup.esc="editing = null"
                @blur="editing = null"
                autofocus
                class="w-full rounded border border-blue-400 px-2 py-1 outline-none" />
              <span v-else :class="row[col.name] === null ? 'text-slate-300 italic' : ''">
                {{ row[col.name] ?? 'null' }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- pagination -->
    <div class="mt-4 flex items-center justify-center gap-4 text-sm">
      <button @click="loadPage(meta.page - 1)" :disabled="meta.page <= 1"
              class="rounded-full bg-white px-4 py-2 shadow transition hover:bg-blue-50 disabled:opacity-40">
        ← Prev
      </button>
      <span class="text-slate-600">Page {{ meta.page }} of {{ meta.total_pages }}</span>
      <button @click="loadPage(meta.page + 1)" :disabled="meta.page >= meta.total_pages"
              class="rounded-full bg-white px-4 py-2 shadow transition hover:bg-blue-50 disabled:opacity-40">
        Next →
      </button>
    </div>
  </div>
</template>
