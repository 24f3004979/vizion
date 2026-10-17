import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Editor from '../views/Editor.vue'

const routes = [
  {
    path : '/',
    name : 'home',
    component : Home
  },
  {
    path : '/editor',
    name : 'editor',
    component : Editor
  }
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})
export default router
