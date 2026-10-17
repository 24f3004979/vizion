<template>
  <main class="min-h-screen bg-slate-50 flex flex-col items-center justify-center gap-10 px-6">

    <div class="text-center">
      <h1 class="text-4xl font-display font-bold tracking-tight text-slate-800">
        Your projects
      </h1>
      <p class="mt-2 text-slate-500">Start something new or pick up where you left off.</p>
    </div>

    <button
      class="group w-60 h-60 rounded-3xl
             bg-gradient-to-br from-white to-blue-400
             shadow-lg shadow-blue-200
             flex flex-col items-center justify-center gap-3
             transition duration-300
             hover:-translate-y-2 hover:shadow-xl active:scale-95">

      <span class="text-5xl font-display font-bold tracking-wider text-slate-800">
        VIZION
      </span>

      <span class="text-sm font-semibold tracking-widest text-blue-700
                   transition group-hover:tracking-[0.25em]">
        <a href="/editor"> + NEW PROJECT </a>
      </span>
    </button>

  </main>
</template>
