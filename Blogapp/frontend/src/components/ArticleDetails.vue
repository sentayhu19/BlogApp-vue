<template>
  <div class="container">
<h3>{{article.title}} </h3>
  </div>
</template>

<script>
import {csrftoken} from '../csrf/csrf_token';
export default {
    data()
    {
        return {
            article: {}
            }
    },
    props: {
        slug:{
            type:String,  
            required:true,
        }
    },
    methods: {
        getArticleData()
        {
            fetch(`/api/articles/${this.slug}/`,{ 
                method:"GET",
                headers:{
                    'Contenet-Type':'application/json',
                'X-CSRFTOKEN':csrftoken 
                }
                })    //ch
            .then(resp=>resp.json())
           .then((data)=> {
               this.article = data
               console.log(data) 
           })
           .catch(error=>console.log(error))
        }
    },
    created()
    {
        this.getArticleData()
    }

}
</script>

<style>

</style>