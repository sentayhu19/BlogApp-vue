import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import CreateArticle from './components/CreateArticle.vue'
import ArticleDetails from './components/ArticleDetails.vue'
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
  },
  {
    path:'/details/:slug',
    name:"details",
    component:ArticleDetails,
    props:true,
},
 
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;