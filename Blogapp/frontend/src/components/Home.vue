<template>
<div class = "container mt-4">
    <div v-for="article in articles" :key="article.pk">
        <h5 class="mb-0"> <h4 style='background-color:green; width:10%; color:white'>Author:  {{article.author}} </h4>
            <span class="badge bg-primary">
           
            </span>
             </h5>
         <h3><router-link 
         class="link-style" 
         :to="{name:'details',params:{slug:article.slug}}">  
               {{article.title}}
              </router-link> 
              </h3>
         <small style='background-color:black; width:10%; color:white'> {{article.created_at}} </small>
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
                })    
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
.link-style {
    font-weight:bold;
    color:black;
     text-decoration:none;
}
.link-style:hover
{
    text-decoration:none;
    color:gray;
}
</style>