<script setup>

  import { ref, onMounted } from 'vue'

  const error = ref(null)
  const rows = ref([])

  const keys = ref([])

  // on Mounted hook with baccked fetching sequence
  onMounted(async() => {
    try{
      const response = await fetch("http://localhost:8000/editor/data")
      console.log(response)

      const fetched = (await response.json()).data
      // With json fetch we can parse into object
      const result = JSON.parse(fetched)


      // Fetch out all column names to render with
      const columns = []
      for (var key in result){
        columns.push(key)
      }

      keys.value = columns

     // Align the extract into row formating
      rows.value = Object.keys(result.id).map(key =>({
      id: result.id[key],
      name : result.name[key],
      city : result.city[key],
      }))
      // Loaded nested dictionary into row format

    }catch(e){
      console.log(`Error Raised as ${e}`)
    }
  })

</script>

<template>
  <div>
    <table class="w-full text-sm text-left rtl:text-right text-body"">
      <thead>
        <tr>
          <th v-for="key in keys">{{ key }} </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in rows">
          <td v-for="elem in row"> {{ elem }} </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
