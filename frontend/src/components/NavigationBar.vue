<script setup>
const links = [
  { name: 'HOME', to: '/' },
  { name: 'ABOUT', to: '/' },
  { name: 'HELP', to: '/' },
]
</script>

<template>
  <header class="fixed top-4 inset-x-0 z-50 flex justify-center px-4">
    <nav
      class="flex items-center gap-1 p-1.5 rounded-full
             bg-blue-200/80 backdrop-blur-md shadow-lg font-display">
      <RouterLink
        v-for="link in links"
        :key="link.name"
        :to="link.to"
        exact-active-class="bg-white text-blue-700 shadow"
        class="px-5 py-2 rounded-full text-sm font-semibold tracking-wide
               text-slate-700 transition duration-300
               hover:bg-white/60 active:scale-95">
        {{ link.name }}
      </RouterLink>
    </nav>
  </header>
</template>
