<template>
<div class = "container mt-4">
    <div v-for="article in articles" :key="article.pk">
        <p class="mb-0">Author:
            <span class="badge bg-primary">
            {{article.author}}
            </span>
             </p>
         <h3>    {{article.title}} </h3>
         <small> {{article.created_at}} </small>
           <hr>
      </div>
     
</div>
 </template>

<script>
import {csrftoken} from '../csrf/csrf_token';
export default {
    data()
    {
        return {
            articles:[]
        }
    },
    methods:{
        getAllArticles()
        {
            fetch('api/articles/',{ 
                method:"GET",
                headers:{
                    'Contenet-Type':'application/json',
                'X-CSRFTOKEN':csrftoken 
                }
                })    //ch
            .then(resp=>resp.json())
           .then((data)=> {
               this.articles.push(...data)
              // console.log(data)
           })
           .catch(error=>console.log(error))
            }
        },
        created ()
        {
            this.getAllArticles()
        }
    }


</script>

<style>

</style>