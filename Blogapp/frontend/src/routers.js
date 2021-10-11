import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import CreateArticle from './components/CreateArticle.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  }, 
  {
      path:"/create",
      name:"create",
      component:CreateArticle,
  }
 
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;