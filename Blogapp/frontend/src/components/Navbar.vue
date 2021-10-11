<template>
<nav>
   <ul>
  <li> <router-link class="btn btn-primary" to="/">Home</router-link></li>
  <li> <router-link class="btn btn-sucess" to="/create">Publish new Article</router-link></li>
  <li> <a class="btn btn-outline-danger" href="/accounts/logout/">Logout </a></li>
</ul>
</nav>

</template>

<script>
export default {

}
</script>

<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
</style>